import os
import json
def read_txt(self, txt_abs_path=None, second_someParts=None):
    """
    读取txt内容 下载
    :param txt_abs_path:
    :param second_someParts:第二项 为指定下载的某几P
    :return:
    """
    if txt_abs_path is None:
        txt = '网址.txt'
    else:
        txt = txt_abs_path

    try:
        with open(txt, "r", encoding="utf-8") as f:
            url_list = f.readlines()

    except Exception as e:
        print(e, '当前文件异常')

    # re_str = r'video/\w.+'
    # re_com = re.compile(re_str)
    for u in url_list:

        # txt的url、画质、下载某几P  使用空格来间隔
        if u.find(' ') != -1:

            # 第二项为画质
            if second_someParts is None:

                qn = u[u.find(' '):]
                qn = qn.strip()

                # 指定某几P
                if qn.find(' ') != -1:

                    some_parts = json.loads(qn[qn.find(' '):].strip())
                    print('指定下载：{}'.format(some_parts))
                    qn = json.loads(qn[:qn.find(' ')])

                # 不指定某几P
                else:
                    some_parts = None
                print('指定画质：{}'.format(qn))

            # 第二项为 下载的某几P，不指定画质
            else:
                some_parts = json.loads(u[u.find(' '):].strip())
                print('指定下载：{}'.format(some_parts))
                qn = None

            u = u[: u.find(' ')]

        # 只有url【没有画质、下载的某几P】
        else:
            qn = None
            some_parts = None

        # url处理
        if u.find('/?') != -1:
            u = u[: u.find('/?')]
        elif u.find('?') != -1:
            u = u[: u.find('?')]
        u = u.replace('\n', '')
        print(u)

        # print(re_com.search(u))
        # print(re_com.search(u).group())

        # 解析HTML，获取name\宽高
        name_list, w_h_list = self.get_name_list(url=u)

        # 只一个name [单个视频]
        if len(name_list) == 1:
            if qn is None:
                qn = self.return_format(w_h_list[0])
            else:
                qn = self.change_format(int(qn))

            print(qn)
            self.down_one(url=u, txt_format_qn=qn)

        # 多个name [此url 多P视频]
        else:
            if qn is None:
                if second_someParts is not None:
                    # index 不适合
                    # w_h = list(filter(lambda x: w_h_list.index(x) in some_parts, w_h_list))
                    w_h_list = [w_h_list[s] for s in some_parts]

                qn = [self.return_format(wh) for wh in w_h_list]
            else:
                qn = [self.change_format(int(q)) for q in qn]

            print(qn)
            self.down_multipart(url=u, txt_qn=qn, some_parts=some_parts)

def down_one(self, url, format_qn: int = None, down_path=r'F:\bili', txt_format_qn=None):
    """
    下载某url
    :param url:
    :param format_qn:
    :param down_path:
    :param txt_format_qn：读取txt文件 画质
    :return:
    """
    # 脚本直接使用
    if txt_format_qn is None:
        assert format_qn is not None
        format_str = self.change_format(format_qn=format_qn)

    # txt使用
    else:
        format_str = txt_format_qn

    cmd = """you-get {} {} -o {} --no-caption""".format(format_str, url, down_path)
    print(cmd)
    os.system(cmd)

    # cmd = 'explorer {}'.format(down_path)
    # os.system(cmd)

def down_multipart(self, url, format_qn_list=None, root_path=r'c:\bili', rename_file=None, some_parts=None, txt_qn=None):
    """
    批量下载
    :param url:请求url
    :param format_qn_list:画质
    :param root_path:下载路径
    :param rename_file:默认为None，不用重命名
    :param some_parts: 下载某p；传list
    :param txt_qn:读取txt文件 拿到的画质
    :return:
    """
    os.chdir(root_path)
    new_dir = url.split('/')[-1]
    if not os.path.exists(new_dir):
        os.mkdir(new_dir)
    down_path = os.path.join(root_path, new_dir)

    # 不使用txt，脚本执行【不推荐】
    if format_qn_list is not None:
        assert txt_qn is None

        # 相同画质[使用一个qn]、文件名不重复
        # 【使用某画质，有可能会出现画质不对的情况】
        if isinstance(format_qn_list, int) and rename_file is None:
            format_str = self.change_format(format_qn=format_qn_list)
            cmd = """you-get {} --playlist {} -o {} --no-caption --debug""".format(format_str, url, down_path)
            print(cmd)
            os.system(cmd)

    # 使用txt的内容【推荐】
    else:
        format_qn_list = txt_qn

        if rename_file is not None:
            fact_name_list = self.get_name_list(url=url)[0]
            assert len(fact_name_list) == len(format_qn_list)

        for index, i in enumerate(format_qn_list):
            format_str = i

            if some_parts is not None:
                assert len(some_parts) == len(format_qn_list)
                url_index = some_parts[index]
            else:
                url_index = index + 1

            new_url = ''.join([url, '?p={}'.format(url_index)])
            cmd = """you-get {} {} -o {} --no-caption""".format(format_str, new_url, down_path)
            print(cmd)
            os.system(cmd)

            # txt不支持 重命名
            if rename_file is None:
                continue

            else:
                # 极少出现文件名重复的情况，若出现，请脚本执行，给rename_file传参

                name = fact_name_list[index]
                os.chdir(down_path)
                all_files = os.listdir(down_path)
                all_files = [i for i in all_files if i.endswith(('mp4', 'flv'))]
                down_file_last = sorted(all_files, key=lambda x: os.path.getmtime(x))[-1]
                file_type = os.path.splitext(down_file_last)[1]

                os.rename(down_file_last, ''.join([name, file_type]))

    # cmd = 'explorer {}'.format(down_path)
    # os.system(cmd)

def down_up_all_videos(self, up_mid, root_path=r'F:\bili'):
    bvid = self.get_up_videos_BV(up_mid=up_mid)
    down_url = [''.join(['https://www.bilibili.com/video/', bv]) for bv in bvid]
    print(down_url)

    up_mid = str(up_mid)
    os.chdir(root_path)
    if not os.path.exists(up_mid):
        os.mkdir(up_mid)
    down_path = os.path.join(root_path, up_mid)
    print(down_path)
    print()

    for d in down_url:
        name_list, w_h_list = self.get_name_list(url=d)
        if len(name_list) == 1:
            qn = self.return_format(w_h_list[0])
            self.down_one(url=d, down_path=down_path, txt_format_qn=qn)

        else:
            qn = [self.return_format(wh) for wh in w_h_list]

            self.down_multipart(url=d, root_path=down_path, txt_qn=qn)
