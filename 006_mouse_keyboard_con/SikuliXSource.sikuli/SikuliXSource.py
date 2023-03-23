import sys
print(sys.version)
# SeedPath="C:/sikulix-2.0.3/seed.txt"
SeedPath = "seed.txt"
file = open(SeedPath)
for line in file.xreadlines():
    click(Region(636, 83, 45, 17))  # 离线下载
    click(Region(745, 473, 222, 22))  # 单击输入框

    name = line.decode("utf-8")
    paste(name)
    click(Region(1124, 622, 81, 25))  # 单击下载
    wait(20)
    click(Region(1035, 734, 69, 21))  # 单击下载
    wait(10)
    click(Region(1145, 680, 63, 23))  # 单击后台下载
    wait(5)
    click(Region(1147, 680, 63, 18))  # 单击后台运行
