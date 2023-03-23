# -*- coding:utf-8 -*-
# @FileName  :52pojieUI_douyin.py
# @AuThor    :neteast@52pojie

import os
import re
import subprocess
import threading
import time
import tkinter as tk
import tkinter.font as tkFont
import warnings
from datetime import datetime

import requests

LOG_LINE_NUM = 0


class App:
    def __init__(self, root):
        self.test = False
        self.initUi(root)
        self.initData()
        self.testData()

    def testData(self):
        if (self.test):
            self.GLineEdit_332.insert(0, '2p5EEc9')  # 2sWmMkb
            self.GButton_333['state'] = 'active'

    def initData(self):

        self.nickname = '未找到该ID用户或者暂未发布作品'
        self.status_download = True
        self.tag = 'odd'
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': "Mozilla/5.0 (iPhone; U; CPU like Mac OS X; en) AppleWebKit/420+ (KHTML, like Gecko) Version/3.0 Mobile/1C28 Safari/419.3"})
        self.starurl = None
        self.baseurl = 'https://v.douyin.com/'
        self.baseinfo = 'https://www.iesdouyin.com/web/api/v2/user/info/?'
        self.userinfourl = None

    def initUi(self, root):
        # setting title
        root.title("DYDownloader neteast@52pojie")
        # setting window size
        width = 897
        height = 533
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        ft = tkFont.Font(family='宋体', size=10)
        GLabel_515 = tk.Label(root)
        GLabel_515["font"] = ft
        GLabel_515["justify"] = "center"
        GLabel_515["text"] = "作者ID"
        GLabel_515.place(x=20, y=10, width=47, height=30)

        self.GLineEdit_508 = tk.Entry(root)
        self.GLineEdit_508["borderwidth"] = "1px"
        self.GLineEdit_508["justify"] = "center"
        self.GLineEdit_508["text"] = "path"
        self.GLineEdit_508['state'] = 'readonly'
        self.GLineEdit_508.place(x=90, y=50, width=610, height=30)

        self.GLineEdit_332 = tk.Entry(root)
        self.GLineEdit_332["borderwidth"] = "1px"
        self.GLineEdit_332["justify"] = "center"
        self.GLineEdit_332["text"] = "url"
        self.GLineEdit_332.place(x=90, y=10, width=231, height=30)

        self.GButton_333 = tk.Button(root)
        self.GButton_333["justify"] = "center"
        self.GButton_333["text"] = "开始下载"
        self.GButton_333.place(x=710, y=50, width=90, height=30)
        self.GButton_333['state'] = 'disable'
        self.GButton_333["command"] = self.GButton_333_command

        ft2 = tkFont.Font(family='宋体', size=12)
        self.GLineEdit_428 = tk.Text(root)
        self.GLineEdit_428["borderwidth"] = "1px"
        self.GLineEdit_428["font"] = ft2
        self.GLineEdit_428.place(x=10, y=90, width=881, height=427)

        self.GButton_676 = tk.Button(root)
        self.GButton_676["font"] = ft
        self.GButton_676["justify"] = "center"
        self.GButton_676["text"] = "停止下载"
        self.GButton_676['state'] = 'disable'
        self.GButton_676.place(x=810, y=50, width=74, height=30)
        self.GButton_676["command"] = self.GButton_676_command

        GButton_701 = tk.Button(root)
        GButton_701["font"] = ft
        GButton_701["justify"] = "center"
        GButton_701["text"] = "获取信息"
        GButton_701.place(x=330, y=10, width=70, height=30)
        GButton_701["command"] = self.GButton_701_command

        GLabel_100 = tk.Label(root)
        GLabel_100["font"] = ft
        GLabel_100["justify"] = "center"
        GLabel_100["text"] = "昵称"
        GLabel_100.place(x=410, y=10, width=43, height=30)

        GLabel_1 = tk.Label(root)
        GLabel_1["font"] = ft
        GLabel_1["justify"] = "center"
        GLabel_1["text"] = "条作品"
        GLabel_1.place(x=790, y=10, width=76, height=30)

        self.GLineEdit_690 = tk.Entry(root)
        self.GLineEdit_690["borderwidth"] = "1px"
        self.GLineEdit_690["font"] = ft
        self.GLineEdit_690["justify"] = "center"
        self.GLineEdit_690["text"] = "条作品"
        self.GLineEdit_690['state'] = 'readonly'
        self.GLineEdit_690.place(x=710, y=10, width=90, height=30)

        self.GLineEdit_281 = tk.Entry(root)
        self.GLineEdit_281["borderwidth"] = "1px"
        self.GLineEdit_281["font"] = ft
        self.GLineEdit_281["fg"] = "#333333"
        self.GLineEdit_281["justify"] = "center"
        self.GLineEdit_281["text"] = "昵称"
        self.GLineEdit_281['state'] = 'readonly'
        self.GLineEdit_281.place(x=460, y=10, width=240, height=31)

        GButton_55 = tk.Button(root)
        GButton_55["bg"] = "#efefef"
        GButton_55["font"] = ft
        GButton_55["fg"] = "#000000"
        GButton_55["justify"] = "center"
        GButton_55["text"] = "保存路径"
        GButton_55["relief"] = "groove"
        GButton_55.place(x=10, y=50, width=70, height=30)
        GButton_55["command"] = self.GButton_55_command

    def GButton_55_command(self):  # 打开文件夹
        path = self.GLineEdit_508.get()
        if path:
            self.open_fp(path)

    def GButton_701_command(self):  # 获取信息
        authorId = self.GLineEdit_332.get()
        self.status_download = True
        if authorId:
            self.starurl = self.baseurl + authorId

            self._log(f'{"-" * 20}开始查询，请稍等{"-" * 20}')
            obj1 = threading.Thread(target=self.analysis, args=({False}))
            obj1.setDaemon(True)
            obj1.start()
        else:
            self._log("请输入作者ID")

    def GButton_676_command(self):  # 停止下载
        self.status_download = False
        self.GButton_676['state'] = 'disable'

    def GButton_333_command(self):  # 开始下载
        self.status_download = True
        authorId = self.GLineEdit_332.get()
        if authorId:
            self.starurl = self.baseurl + authorId
            self._log(f'{"-" * 20}准备下载，请稍等{"-" * 20}')
            self.GButton_333['state'] = 'disable'
            self.GButton_676['state'] = 'active'
            self.pcursor = ''
            obj1 = threading.Thread(target=self.analysis, args=({True}))
            obj1.setDaemon(True)
            obj1.start()
        else:
            self._log("请输入作者ID")

    def analysis(self, flag):
        req = self._requests('get', self.starurl, decode_level=3)
        sp = req.url.split('?')
        if len(sp) == 2:
            param = sp[1]
        else:
            self._log(f'{"-" * 20}获取数据失败,请检查主播ID是否正确{"-" * 20}')
            return
        self.userinfourl = self.baseinfo + param
        userinfo = self._requests('get', self.userinfourl, decode_level=2)
        self.nickname = userinfo['user_info']['nickname']
        aweme_count = userinfo['user_info']['aweme_count']
        if not flag:
            self._log(f'{"-" * 20}查询完成！{"-" * 20}')
            filepath = os.getcwd() + '\\' + 'dydownloads' + '\\' + self.nickname
            self.GLineEdit_690['state'] = 'normal'
            self.GLineEdit_281['state'] = 'normal'
            self.GLineEdit_508['state'] = 'normal'
            self.GLineEdit_508.delete(0, 'end')
            self.GLineEdit_281.delete(0, 'end')
            self.GLineEdit_690.delete(0, 'end')
            self.GLineEdit_690.insert(0, f'{aweme_count}')
            self.GLineEdit_281.insert(0, f'{self.nickname}')
            self.GLineEdit_508.insert(0, f'{filepath}')
            self.GLineEdit_690['state'] = 'readonly'
            self.GLineEdit_281['state'] = 'readonly'
            self.GLineEdit_508['state'] = 'readonly'
            self.GButton_333['state'] = 'active'
        else:
            self._log(f'{"-" * 20}开始下载{"-" * 20}')
            max_cursor = 0
            video_has_more = True
            icount = 0;
            while video_has_more and self.status_download:
                json_url = f'https://www.iesdouyin.com/web/api/v2/aweme/post/?{param}&' \
                           f'count=21&max_cursor={max_cursor}'
                req = self._requests('get', json_url, decode_level=2)
                video_has_more = req['has_more']
                max_cursor = req['max_cursor']
                video_list = req['aweme_list']
                for video in video_list:
                    if not self.status_download:
                        self._log(f'{"-" * 20}已停止下载video!{"-" * 20}')
                        break
                    icount += 1
                    self.download_video(video, icount)
            self._log(f'{"-" * 20}全部{aweme_count}个视频已下载完成{icount}个!{"-" * 20}')

    def download_video(self, video, num=0):
        try:
            filepath = os.getcwd() + '/' + 'dydownloads' + '/' + self.nickname
            caption = video['desc']  # title
            vid = video['video']['vid']  # video link
            caption = re.sub('[ \\/:*?"<>|\n\t]', '', caption)
            likeCount = video['statistics']['digg_count']
            comment_count = video['statistics']['comment_count']
            caption = caption[:40] if len(caption) > 40 else caption
            self._log(f'{num:0>3d}{caption} {comment_count}评论 {likeCount}人点赞')
            caption = caption[:28] if len(caption) > 28 else caption
            if caption:
                download_url = f'https://aweme.snssdk.com/aweme/v1/play/?video_id={video["video"]["vid"]}&ratio=1080p'
                video_data = self._requests('get', download_url, decode_level=3).content
                self.save_video(os.path.normpath(filepath),
                                f'{num:0>3d}_' + caption + '_' + video["video"]["vid"] + '.mp4', video_data,
                                download_url)
        except Exception as e:
            print(e)
            self._log(f'获取数据失败,请检查主播ID是否正确,也可能cookies已过期!')

    def save_video(self, path, filename, video_data, url):
        if not os.path.exists(path):
            os.makedirs(path)
        with open(os.path.normpath(os.path.join(path, filename)), 'wb') as f:
            f.write(video_data)
            now_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self._log(f'  状态:[下载完成]')

    def open_fp(self, fp):
        """
        打开文件或文件夹
        :param fp: 需要打开的文件或文件夹路径
        """
        import platform
        systemType: str = platform.platform()  # 获取系统类型
        if 'mac' in systemType:  # 判断以下当前系统类型
            fp: str = fp.replace("\\", "/")  # mac系统下,遇到`\\`让路径打不开,不清楚为什么哈,觉得没必要的话自己可以删掉啦,18行那条也是
            subprocess.call(["open", fp])
        else:
            fp: str = fp.replace("/", "\\")  # win系统下,有时`/`让路径打不开
            try:
                os.startfile(fp)
            except:
                self._log(f'{"-" * 20}文件还未下载{"-" * 20}')

    def _requests(self, method, url, decode_level=1, retry=0, timeout=15, **kwargs):
        if method in ["get", "post"]:
            for _ in range(retry + 1):
                try:
                    warnings.filterwarnings('ignore')
                    response = getattr(self.session, method)(url, timeout=timeout, verify=False, **kwargs)
                    return response.text if decode_level == 1 else response.json() if decode_level == 2 else response
                except Exception as e:
                    self._log(e)

        return None

    def _log(self, logmsg):
        global LOG_LINE_NUM
        current_time = self.get_current_time()
        logmsg_in = str(current_time) + " " + str(logmsg) + "\n"  # 换行
        self.GLineEdit_428.tag_config("even", background='#e0e0e0')
        self.GLineEdit_428.tag_config("odd", background='#ffffff')
        self.tag = 'odd' if self.tag == 'even' else 'even'
        if LOG_LINE_NUM <= 22:

            self.GLineEdit_428.insert('end', logmsg_in, self.tag)
            LOG_LINE_NUM = LOG_LINE_NUM + 1
        else:
            self.GLineEdit_428.delete(1.0, 2.0)
            self.GLineEdit_428.insert('end', logmsg_in, self.tag)

    def get_current_time(self):
        current_time = time.strftime('%H:%M:%S', time.localtime(time.time()))
        return current_time


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()