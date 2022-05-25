def init_paste():
    click(Region(1323,716,47,19))#click baoxiao
    wait(2)
    click(Region(1841,12,17,9))#quanping
    wait(0.5)
    click(Region(441,386,36,8))#fapiao xingshi

    wait(0.1)
    click(Region(440,460,91,15))#quan zhizhi fapiao
    wait(0.1)
    click(Region(1247,353,90,20))#baoxiao dan fenlei
    wait(0.1)
    click(Region(1247,385,63,17))#shinei jiaotong fapiao
    wait(0.1)
    click(Region(1242,384,110,20))#fapiao shuliang
    wait(0.1)
    paste('6')
    wait(0.1)
    click(Region(419,420,35,19))#shifou jiekuan
    wait(0.1)
    click(Region(429,460,11,13))#fou
    for i in range(6):
        wait(0.1)
        click(Region(1698,445,28,28))#++

init_paste()
