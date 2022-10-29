from tokenize import Number
import os



def generateTestData(config_list):
    try:
        os.mkdir(config_list[5])
    except:
        pass
    for k in range(config_list[2]):
        f= open(config_list[5]+"/"+str(k+1)+".txt","w", encoding="utf-8")
        for i in range(config_list[0]):
            for j in range(config_list[1]):
                if i==0:



                    if config_list[4]==1:

                        f.write(str(k)+"\n")
                    if config_list[4]==2:
                        f.write(str(k)+" ")
                elif i==1:
                    if config_list[4]==1:

                        f.write(str(config_list[3])+"\n")
                    if config_list[4]==2:
                        f.write(str(config_list[3])+" ")
                else:
                    if j%2==1:
                        if config_list[4]==1:

                            f.write(str(i)+"\n")
                        if config_list[4]==2:
                            f.write(str(i)+" ")
                    else:
                        if config_list[4]==1:

                            f.write(str(j)+"\n")
                        if config_list[4]==2:
                            f.write(str(j)+" ")
            if config_list[4]==1:

                pass
            if config_list[4]==2:
                f.write("\n")


if __name__== '__main__':
    calibritionNA=[256,256,132,2,1,"calibritionNA"]
    fastAlign=[256,256,24,4,1,"fastAlign"]
    fasZernike=[256,256,46,5,1,"fastZernike"]
    pupil=[256,256,8,6,1,"pupil"]
    testcase1=[4,4,3,9,1,"testcase1"]
    # generateTestData(calibritionNA)
    # generateTestData(fastAlign)
    # generateTestData(fasZernike)
    # generateTestData(pupil)
    generateTestData(testcase1)