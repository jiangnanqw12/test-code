import os


def down_one(format_str, url, down_path=r'c:\bili', proxy=r"--no-proxy"):

    cmd = """you-get {} {} -o {} {} --debug""".format(
        format_str, url, down_path, proxy)
    print(cmd)
    os.system(cmd)

    # cmd = 'explorer {}'.format(down_path)
    # os.system(cmd)


down_path = os.getcwd()
f1 = open(down_path+"/re.downlist", 'r')
linelist = f1.readlines()
for line in linelist:
    down_one("", "\""+line[:-1]+"\"", down_path=r'c:\bili')
    # down_one("", "\""+line[:-1]+"\"", down_path=r'c:\bili',
    #          proxy="-s 127.0.0.1:1024")
    # down_one("", "\""+line[:-1]+"\"", down_path=r'c:\bili',
    #          proxy="--socks-proxy 127.0.0.1:10809")
