import os
# coding=<utf-8>
replace_list = [
        ["", " $$\sigma$ "],
    ["ĂÂ˘Ăâ ĂÂĄ2","$$\sqrt\{2\}$"],
    ["Ëx","$$\hat x$"],
    ["","$$\\alpha$"],
    ["","$$\\beta$"],
    ["f(x)\=sin⁡(x)x2f(x) = \\\\frac{\\\\sin(x)}{x^2}","f(x) = \\\\frac{\\\\sin(x)}{x^2}"],
    [" f(x)\=x2f(x) = x^2"," f(x) = x^2"],
    [" 7×6\=427 \\\\times 6 = 42"," 7 \\\\times 6 = 42"],
    [" xx"," x"],
    [" x\=2x = 2"," x = 2"],
    [" dfdf"," df"],
    [" dxdx"," dx"],
    [" dfdx\\\\frac{df}{dx}"," \\\\frac{df}{dx}"],
    [" x2x^2"," x^2"],
    [" f(x)\=x2f(x)=x^2"," f(x)=x^2"],
    [" x\=2x=2"," x=2"],
    [" 00"," 0"],
    [" 11"," 1"],
    [" 22"," 2"],
    [" 33"," 3"],
    [" 44"," 4"],
    [" 55"," 5"],
    [" 66"," 6"],
    [" 77"," 7"],

    [" x\=1x = 1"," x = 1"],
    [" 0.010.01"," 0.01"],
    [" 2⋅x⋅dx2 \\\\cdot x \\\\cdot dx"," 2 \\\\cdot x \\\\cdot dx"],
    [" 33"," 3"],
    [" 2⋅3⋅0.012 \\\\cdot 3 \\\\cdot 0.01"," 2 \\\\cdot 3 \\\\cdot 0.01"],
    [" 0.060.06"," 0.06"],
    [" dx2dx^2"," dx^2"],
    [" df\=2x⋅dx+(dx)2df = 2x \\\\cdot dx + (dx)^2"," df = 2x \\\\cdot dx + (dx)^2"],
    ["dfdx\=2x⋅dx+(dx)2dx\=2x+dx\\\\frac{df}{dx} = \\\\frac{2x \\\\cdot dx + (dx)^2}{dx} = 2x + dx","\\\\frac{df}{dx} = \\\\frac{2x \\\\cdot dx + (dx)^2}{dx} = 2x + dx"],
    ["\"dd\"","\"d\""],
    [" dx→0dx \\\\to 0"," dx \\\\to 0"],
    [" (dx)2(dx)^2"," (dx)^2"],
    [" 0.00010.0001"," 0.0001"],
    ["dfdx\=2x\\\\frac{df}{dx} = 2x","dfdx\=2x\\\\frac{df}{dx} = 2x"],

    [" f(x)\=x3f(x) = x^3"," f(x) = x^3"],
    [" x3x^3"," x^3"],
    [" x+dxx + dx"," x + dx"],
    [" x2⋅dxx^2 \\\\cdot dx"," x^2 \\\\cdot dx"],
    [" dx3dx^3"," dx^3"],
    ["(x+dx)3\=x3+3x2dx+3xdx2+dx3(x + dx)^3 = x^3 + \\\\color{#fc6255} 3x^2 \\\\color{black} dx \\\\color{#AAAAAA} + 3xdx^2 + dx^3","(x + dx)^3 = x^3 + \\\\color{#fc6255} 3x^2 \\\\color{black} dx \\\\color{#AAAAAA} + 3xdx^2 + dx^3"],
    [" 3x23x^2"," 3x^2"],
    [" f(x)\=xnf(x) = x^n"," f(x) = x^n"],
    [" f(x)\=x1f(x) = x^1"," f(x) = x^1"],
    [" f(x)\=x2f(x) = x^2"," f(x) = x^2"],
    [" f(x)\=x3f(x) = x^3"," f(x) = x^3"],
    [" f(x)\=x4f(x) = x^4"," f(x) = x^4"],
    [" f(x)\=x5f(x) = x^5"," f(x) = x^5"],
    [" (x+dx)1\=x+1dx(x + dx)^1 = x + \\\\color{#fc6255}{1} \\\\color{black} dx"," (x + dx)^1 = x + \\\\color{#fc6255}{1} \\\\color{black} dx"]
    ,[" (x+dx)2\=x2+2xdx+dx2(x + dx)^2 = x^2 + \\\\color{#fc6255} 2x \\\\color{black} dx \\\\color{#AAAAAA} + dx^2"," (x + dx)^2 = x^2 + \\\\color{#fc6255} 2x \\\\color{black} dx \\\\color{#AAAAAA} + dx^2"]
,[" (x+dx)4\=x4+4x3dx+6x2dx2+4xdx3+dx4(x + dx)^4 = x^4 + \\\\color{#fc6255} 4x^3 \\\\color{black} dx \\\\color{#AAAAAA} + 6x^2dx^2 + 4xdx^3 + dx^4"," (x + dx)^4 = x^4 + \\\\color{#fc6255} 4x^3 \\\\color{black} dx \\\\color{#AAAAAA} + 6x^2dx^2 + 4xdx^3 + dx^4"],
[" (x+dx)5\=x5+5x4dx+10x3dx2+10x2dx3+5xdx4+dx5(x + dx)^5 = x^5 + \\\\color{#fc6255} 5x^4 \\\\color{black} dx \\\\color{#AAAAAA} + 10x^3dx^2 + 10x^2dx^3 + 5xdx^4 + dx^5"," (x + dx)^5 = x^5 + \\\\color{#fc6255} 5x^4 \\\\color{black} dx \\\\color{#AAAAAA} + 10x^3dx^2 + 10x^2dx^3 + 5xdx^4 + dx^5"]
    ,[" f(x)\=3x2f(x)= 3x^2"," f(x)= 3x^2"],
    [" f(x)\=1xf(x) = \\\\frac{1}{x}"," f(x) = \\\\frac{1}{x}"],
    [" −1\-1"," \-1"],
    [" −2\-2"," \-2"],
    [" −3\-3"," \-3"],
    [" −4\-4"," \-4"],
    [" −5\-5"," \-5"],
    [" −6\-6"," \-6"],
    [" 1x\\\\frac{1}{x}"," \\\\frac{1}{x}"],
    [" x−1x^{-1}"," x^{-1}"],
    [" 13\\\\frac{1}{3}"," \\\\frac{1}{3}"],
    [" 12\\\\frac{1}{2}"," \\\\frac{1}{2}"],
    [" 1/x1/x"," 1/x"],
    [" d(1/x)d(1/x)"," d(1/x)"],
    [" d(1/x)/dxd(1/x)/dx"," d(1/x)/dx"],
    [" f(x)\=xf(x) = \\\\sqrt{x}"," f(x) = \\\\sqrt{x}"],
    ["x12x^{\\\\frac{1}{2}}","x^{\\\\frac{1}{2}}"],
    [" sin⁡(0.8)\\\\sin(0.8)"," \\\\sin(0.8)"],
    [" θ\=0.8\\\\theta = 0.8"," \\\\theta = 0.8"],
    [" 0.80.8"," 0.8"],
    [" sin⁡(θ)\\\\sin(\\\\theta)"," \\\\sin(\\\\theta)"],
    [" cos⁡(θ)\\\\cos(\\\\theta)"," \\\\cos(\\\\theta)"],
    [" θ\\\\theta"," \\\\theta"],
    [" dθd \\\\theta"," d \\\\theta"]

    ]
def text_replace(path):
    listdir = os.listdir(path)

    #replace_list.append(["", " $$\sigma$ "])
    for i in range(len(listdir)):

        filename = listdir[i]
        filenamelist = filename.split(sep=".")
        if filenamelist[-1] == "md":

            f = open(path+filename, 'r', encoding='UTF-8')
            linelist = f.readlines()

            # print(linelist)
            f2 = open(path+"des/"+filenamelist[0]+".md", "w", encoding='UTF-8')
            for i in range(len(linelist)):


                line=linelist[i]
                for j in range(len(replace_list)):
                    # idx = line.find(replace_list[j][0])
                    # idx2 = line.find("Ëx")
                    # print(idx2)
                    line = line.replace(
                        replace_list[j][0], replace_list[j][1])
                f2.write(line)

                # print(linelist[i][-1])
                # idx = line.find("")
                # print(idx)
                # if idx != -1:
                #     print(line)
                #     f2.write(line)
                #     f2.write("$$\sigma$$")
                #     line.replace("", "$$\sigma$$")
                #     print(line)
                #     f2.write(line)
                # f2.write(linelist[i])


if __name__ == '__main__':
    path = os.getcwd()+"/"
    text_replace(path)
