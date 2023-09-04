import subprocess

# 获取本机wifi列表
output = subprocess.run(['netsh', 'wlan', 'show', 'profiles'], capture_output=True).stdout.decode('gbk').split('\n')
#print(output)
wifi_list = [item.split(':')[1][1:-1] for item in output if "所有用户配置文件" in item]

#print(wifi_list)
# 获取 wifi 密码
for wifi in wifi_list:
    ret = subprocess.run(['netsh', 'wlan', 'show', 'profile', f'name={wifi}', 'key=clear'],
                             capture_output=True).stdout.decode('gbk', errors='ignore').split('\n')

    #print(ret)
    results = [item.split(':')[1][1:-1] for item in ret if "关键内容" in item]
    print(f'{wifi} 密码:{results[0] if len(results)>0 else "无" }')