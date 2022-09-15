import os
def down_one( format_str,url, down_path=r'c:\bili'):


    cmd = """you-get {} {} -o {} --no-proxy""".format(format_str, url, down_path)
    print(cmd)
    os.system(cmd)

    # cmd = 'explorer {}'.format(down_path)
    # os.system(cmd)

down_path=os.getcwd()
f1=open(down_path+"/re.downlist",'r')
linelist=f1.readlines()
for line in linelist:
    down_one( "-l",line, down_path=r'c:\bili')