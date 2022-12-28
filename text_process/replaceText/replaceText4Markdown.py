import os
# coding=<utf-8>
# replace text with given list
# Generate 26 uppercase English letters and lowercase English letters in string format
def generate_multi_number_replace_list(num,num_base):
    replace_list_multi_number = []

    for i in range(num_base):
        replace_list_multi_number.append([" "+num*str(i), " "+str(i)])
    return replace_list_multi_number

def generate_multi_charater_repalce_list(num):
    replace_list_multi_charactor = []
    replace_data = []
    space_str = " "
    # Iterate through all the English letters
    for i in range(65, 91):

        # Convert the integer to a character
        c = chr(i).encode('utf-8')
        # print(c+c+c)

        c2 = str(c)[2]
        # print(c2[2])
        replace_data.append(space_str+num*c2)
        replace_data.append(space_str+c2)
        replace_list_multi_charactor.append(replace_data)
        replace_data = []
    for i in range(97, 97+26):
        c = chr(i).encode('utf-8')
        # Convert the integer to a character
        c2 = str(c)[2]
        # print(c2[2])
        replace_data.append(space_str+num*c2)
        replace_data.append(space_str+c2)
        replace_list_multi_charactor.append(replace_data)
        replace_data = []
    # print(("A".encode('utf-8')).decode('utf-8'))
    #print(replace_list_multi_charactor)
    return replace_list_multi_charactor


def replaceText(file_path, replace_list):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    for i in range(len(replace_list)):
        text = text.replace(replace_list[i][0], replace_list[i][1])
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(text)


def text_replace(path, replace_list):
    listdir = os.listdir(path)

    #replace_list.append(["", " $$\sigma$ "])
    for i in range(len(listdir)):

        filename = listdir[i]
        filenamelist = filename.split(sep=".")
        if filenamelist[-1] == "md":

            f = open(path+filename, 'r', encoding='UTF-8')
            linelist = f.readlines()

            # print(linelist)
            if os.path.isdir(path + 'des/'):
                pass
            else:
                os.mkdir(path + 'des/')
            f2 = open(path+"des/"+filenamelist[0]+".md", "w", encoding='UTF-8')
            for i in range(len(linelist)):

                line = linelist[i]
                for j in range(len(replace_list)):
                    # idx = line.find(replace_list[j][0])
                    # if replace_list[j][0]==' fff':
                    #     print(replace_list[j])
                    #     idx2 = line.find(' fff')
                    #     if idx2!=-1:
                    #         print(line)
                    #         print(idx2)

                    line = line.replace(
                        replace_list[j][0], replace_list[j][1])
                f2.write(line)


replace_list_back = [
    ["", " $$\sigma$ "],
    ["Ã¢Ë†Å¡2", "$$\sqrt\{2\}$"],
    ["ˆx", "$$\hat x$"],
    ["", "$$\\alpha$"],
    ["", "$$\\beta$"],
    ["f(x)\=sin?(x)x2f(x) = \\\\frac{\\\\sin(x)}{x^2}",
        "f(x) = \\\\frac{\\\\sin(x)}{x^2}"],
    [" f(x)\=x2f(x) = x^2", " f(x) = x^2"],
    [" 7�6\=427 \\\\times 6 = 42", " 7 \\\\times 6 = 42"],
    [" xx", " x"],
    [" x\=2x = 2", " x = 2"],
    [" dfdf", " df"],
    [" dxdx", " dx"],
    [" dfdx\\\\frac{df}{dx}", " \\\\frac{df}{dx}"],
    [" x2x^2", " x^2"],
    [" f(x)\=x2f(x)=x^2", " f(x)=x^2"],
    [" x\=2x=2", " x=2"],
    [" 00", " 0"],
    [" 11", " 1"],
    [" 22", " 2"],
    [" 33", " 3"],
    [" 44", " 4"],
    [" 55", " 5"],
    [" 66", " 6"],
    [" 77", " 7"],

    [" x\=1x = 1", " x = 1"],
    [" 0.010.01", " 0.01"],
    [" 2?x?dx2 \\\\cdot x \\\\cdot dx", " 2 \\\\cdot x \\\\cdot dx"],
    [" 33", " 3"],
    [" 2?3?0.012 \\\\cdot 3 \\\\cdot 0.01", " 2 \\\\cdot 3 \\\\cdot 0.01"],
    [" 0.060.06", " 0.06"],
    [" dx2dx^2", " dx^2"],
    [" df\=2x?dx+(dx)2df = 2x \\\\cdot dx + (dx)^2",
     " df = 2x \\\\cdot dx + (dx)^2"],
    ["dfdx\=2x?dx+(dx)2dx\=2x+dx\\\\frac{df}{dx} = \\\\frac{2x \\\\cdot dx + (dx)^2}{dx} = 2x + dx",
     "\\\\frac{df}{dx} = \\\\frac{2x \\\\cdot dx + (dx)^2}{dx} = 2x + dx"],
    ["\"dd\"", "\"d\""],
    [" dx?0dx \\\\to 0", " dx \\\\to 0"],
    [" (dx)2(dx)^2", " (dx)^2"],
    [" 0.00010.0001", " 0.0001"],
    ["dfdx\=2x\\\\frac{df}{dx} = 2x", "dfdx\=2x\\\\frac{df}{dx} = 2x"],

    [" f(x)\=x3f(x) = x^3", " f(x) = x^3"],
    [" x3x^3", " x^3"],
    [" x+dxx + dx", " x + dx"],
    [" x2?dxx^2 \\\\cdot dx", " x^2 \\\\cdot dx"],
    [" dx3dx^3", " dx^3"],
    ["(x+dx)3\=x3+3x2dx+3xdx2+dx3(x + dx)^3 = x^3 + \\\\color{#fc6255} 3x^2 \\\\color{black} dx \\\\color{#AAAAAA} + 3xdx^2 + dx^3",
     "(x + dx)^3 = x^3 + \\\\color{#fc6255} 3x^2 \\\\color{black} dx \\\\color{#AAAAAA} + 3xdx^2 + dx^3"],
    [" 3x23x^2", " 3x^2"],
    [" f(x)\=xnf(x) = x^n", " f(x) = x^n"],
    [" f(x)\=x1f(x) = x^1", " f(x) = x^1"],
    [" f(x)\=x2f(x) = x^2", " f(x) = x^2"],
    [" f(x)\=x3f(x) = x^3", " f(x) = x^3"],
    [" f(x)\=x4f(x) = x^4", " f(x) = x^4"],
    [" f(x)\=x5f(x) = x^5", " f(x) = x^5"],
    [" (x+dx)1\=x+1dx(x + dx)^1 = x + \\\\color{#fc6255}{1} \\\\color{black} dx", " (x + dx)^1 = x + \\\\color{#fc6255}{1} \\\\color{black} dx"], [" (x+dx)2\=x2+2xdx+dx2(x + dx)^2 = x^2 + \\\\color{#fc6255} 2x \\\\color{black} dx \\\\color{#AAAAAA} + dx^2", " (x + dx)^2 = x^2 + \\\\color{#fc6255} 2x \\\\color{black} dx \\\\color{#AAAAAA} + dx^2"], [
        " (x+dx)4\=x4+4x3dx+6x2dx2+4xdx3+dx4(x + dx)^4 = x^4 + \\\\color{#fc6255} 4x^3 \\\\color{black} dx \\\\color{#AAAAAA} + 6x^2dx^2 + 4xdx^3 + dx^4", " (x + dx)^4 = x^4 + \\\\color{#fc6255} 4x^3 \\\\color{black} dx \\\\color{#AAAAAA} + 6x^2dx^2 + 4xdx^3 + dx^4"],
    [" (x+dx)5\=x5+5x4dx+10x3dx2+10x2dx3+5xdx4+dx5(x + dx)^5 = x^5 + \\\\color{#fc6255} 5x^4 \\\\color{black} dx \\\\color{#AAAAAA} + 10x^3dx^2 + 10x^2dx^3 + 5xdx^4 + dx^5",
        " (x + dx)^5 = x^5 + \\\\color{#fc6255} 5x^4 \\\\color{black} dx \\\\color{#AAAAAA} + 10x^3dx^2 + 10x^2dx^3 + 5xdx^4 + dx^5"], [" f(x)\=3x2f(x)= 3x^2", " f(x)= 3x^2"],
    [" f(x)\=1xf(x) = \\\\frac{1}{x}", " f(x) = \\\\frac{1}{x}"],
    [" ?1\-1", " \-1"],
    [" ?2\-2", " \-2"],
    [" ?3\-3", " \-3"],
    [" ?4\-4", " \-4"],
    [" ?5\-5", " \-5"],
    [" ?6\-6", " \-6"],
    [" 1x\\\\frac{1}{x}", " \\\\frac{1}{x}"],
    [" x?1x^{-1}", " x^{-1}"],
    [" 13\\\\frac{1}{3}", " \\\\frac{1}{3}"],
    [" 12\\\\frac{1}{2}", " \\\\frac{1}{2}"],
    [" 1/x1/x", " 1/x"],
    [" d(1/x)d(1/x)", " d(1/x)"],
    [" d(1/x)/dxd(1/x)/dx", " d(1/x)/dx"],
    [" f(x)\=xf(x) = \\\\sqrt{x}", " f(x) = \\\\sqrt{x}"],
    ["x12x^{\\\\frac{1}{2}}", "x^{\\\\frac{1}{2}}"],
    [" sin?(0.8)\\\\sin(0.8)", " \\\\sin(0.8)"],
    [" ?\=0.8\\\\theta = 0.8", " \\\\theta = 0.8"],
    [" 0.80.8", " 0.8"],
    [" sin?(?)\\\\sin(\\\\theta)", " \\\\sin(\\\\theta)"],
    [" cos?(?)\\\\cos(\\\\theta)", " \\\\cos(\\\\theta)"],
    [" ?\\\\theta", " \\\\theta"],
    [" d?d \\\\theta", " d \\\\theta"],
    [" sin?(x)\\\\sin(x)", " \\\\sin(x)"],
    [" f(x)\=g(x)+h(x)f(x) = g(x) + h(x)", " f(x) = g(x) + h(x)"],
    [" f(x)\=sin?(x)+x2f(x) = \\\\sin(x) + x^2", " f(x) = \\\\sin(x) + x^2"],
    [" x\=0.5x = 0.5", " x = 0.5"],
    [" 0.5+dx0.5 + dx", " 0.5 + dx"],
    [" d(sin?(x))d\\\\left(\\\\sin(x)\\\\right)",
     " d\\\\left(\\\\sin(x)\\\\right)"],
    [" d(x2)d(x^2)", " d(x^2)"],
    [" cos?(x)?dx\\\\cos(x) \\\\cdot dx", " \\\\cos(x) \\\\cdot dx"],
    [" 2x?dx2x \\\\cdot", " 2x \\\\cdot"],
    [" cos?(x)+2x\\\\cos(x)+2x", " \\\\cos(x)+2x"],
    [" sin?(x)?x2\\\\sin(x) \\\\cdot x^2", " \\\\sin(x) \\\\cdot x^2"],
    [" d(sin?(x))d\\\\left( \\\\sin(x)\\\\right)",
     " d\\\\left( \\\\sin(x)\\\\right)"],
    [" cos?(x)dx\\\\cos(x)dx", " \\\\cos(x)dx"],
    [" f(x)\=g(x)h(x)f(x) = g(x)h(x)", " f(x) = g(x)h(x)"],
    [" sin?(x2)\\\\sin(x^2)", " \\\\sin(x^2)"],
    [" d(sin?(h))d\\\\left(\\\\sin(h)\\\\right)",
     " d\\\\left(\\\\sin(h)\\\\right)"],
    [" sin?(h)\\sin(h)", " \\sin(h)"],
    ["", ""],
    ["times", "\\times"],
    [", \\times", "\\times"],

    ["\\left\\[", ""],
    ["\\right\\]", ""],
    ["", ""],
    ["xyxyx, y", "xy"],
    ["\\left[", ""],
    ["\\right]", ""],
    [" \\vec{\\textbf{v}}vstart bold text, v, end bold text, with, vector, on top",
        " $\\vec{\\textbf{v}}$"],


    ["{array}", "{bmatrix}"],
    ["{bmatrix}{c}", "{bmatrix}"],
    ["{bmatrix}{cc}", "{bmatrix}"],
    ["{bmatrix}{ccc}", "{bmatrix}"],
    ["{bmatrix}{cccc}", "{bmatrix}"],
    # color+A  \textcolor{color} todolist
    ["\\blueD", "\\textcolor{#11accd}"],
    ["\\blueE", "\\textcolor{#0c7f99}"],
    ["\\greenD", "\\textcolor{green}"],
    ["\\greenE", "\\textcolor{#0d923f}"],
    ["\\maroonD", "\\textcolor{maroon}"],
    ["\\goldD", "\\textcolor{gold}"],
    ["\\redD", "\\textcolor{#e84d39}"],
    ["\\redE", "\\textcolor{#bc2612}"],
    ["\\_", "_"],
    ["start color #11accd, \\imath, with, hat, on top, end color #11accd",
        "\\textcolor{blue}{\\hat\\imath}"],
    ["start color #ca337c, \\jmath, with, hat, on top, end color #ca337c",
        "\\textcolor{red}{\\hat\\jmath}"],
    # [" 111 ", " 1 "],todolist 1 a A dx dy    , . ! - + = < > ? : ; / \ | ( ) [ ] { } * ^ & % $ # @ ~ ` " ' \n \t
    #[" 111,", " 1 "],todolist
    ["f(x, y)f(x,y)f, left parenthesis, x, comma, y, right parenthesis", "f(x, y)"],
    ["(x_0, y_0)(x0​,y0​)left parenthesis, x, start subscript, 0, end subscript, comma, y, start subscript, 0, end subscript, right parenthesis", "(x_0, y_0)"],
    ["\\frac{\\partial f}{\\partial x}∂x∂f​start fraction, \\partial, f, divided by, \\partial, x, end fraction",
        "\\frac{\\partial f}{\\partial x}"],
    ["\\frac{\\partial f}{\\partial y}∂y∂f​start fraction, \\partial, f, divided by, \\partial, y, end fraction",
        "\\frac{\\partial f}{\\partial y}"],
    ["f'f′f, prime", "f'"],
    ["\\nabla∇del", "\\nabla"],

    ["left brace,", "{"],
    ["right brace,", "}"],
    ["minus,", "-"],
    ["plus,", "+"],
    ["left parenthesis,", "("],
    ["right parenthesis,", ")"],
    ["comma,", ","],
    ["left brace", "{"],
    ["right brace", "}"],
    ["left parenthesis", "("],
    ["right parenthesis", ")"],
    ["cubed,", "^3"],
    ["\\\\varvdots, rectangle", "$\\vdots$"],
    ["start bold text, a, end bold text, with, vector, on top", "\\vec{a}"],
    ["start bold text, b, end bold text, with, vector, on top", "\\vec{b}"],
    ["start bold text, c, end bold text, with, vector, on top", "\\vec{c}"],
    ["start bold text, d, end bold text, with, vector, on top", "\\vec{d}"],
    ["start bold text, e, end bold text, with, vector, on top", "\\vec{e}"],
    ["start bold text, f, end bold text, with, vector, on top", "\\vec{f}"],
    ["start bold text, i, end bold text, with, vector, on top", "\\vec{i}"],
    ["start bold text, j, end bold text, with, vector, on top", "\\vec{j}"],
    ["start bold text, k, end bold text, with, vector, on top", "\\vec{k}"],
    ["start bold text, k, end bold text, with, vector, on top", "\\vec{k}"],
    ["start bold text, k, end bold text, with, vector, on top", "\\vec{k}"],
    ["start bold text, k, end bold text, with, vector, on top", "\\vec{k}"],
    ["start bold text, k, end bold text, with, vector, on top", "\\vec{k}"],
    ["start bold text, k, end bold text, with, vector, on top", "\\vec{k}"],
    #["\\\\", "\\"],
    [", ,", ","],
]
replace_list2 = [
    [" ", " "],

    ["", ""],
    ["", ""],
    ["", ""],
    ["", ""],
    ["\\\\", "\\"],
    ["\\left\\[", ""],
    ["\\right\\]", ""],
    ["\\left[", ""],
    ["\\right]", ""],
    ["{array}", "{bmatrix}"],
    ["{bmatrix}{c}", "{bmatrix}"],
    ["{bmatrix}{cc}", "{bmatrix}"],
    ["{bmatrix}{ccc}", "{bmatrix}"],
    ["{bmatrix}{cccc}", "{bmatrix}"],
    # color+A  \textcolor{color} todolist
    ["\\blueD", "\\textcolor{#11accd}"],
    ["\\blueE", "\\textcolor{#0c7f99}"],
    ["\\greenD", "\\textcolor{green}"],
    ["\\greenE", "\\textcolor{#0d923f}"],
    ["\\maroonD", "\\textcolor{maroon}"],
    ["\\goldD", "\\textcolor{gold}"],
    ["\\redD", "\\textcolor{#e84d39}"],
    ["\\redE", "\\textcolor{#bc2612}"],
    ["\\_", "_"],
    [" \\vec{\\textbf{v}}vstart bold text, v, end bold text, with, vector, on top",
        " $\\vec{\\textbf{v}}$"],

    ["f(x, y)f(x,y)f, left parenthesis, x, comma, y, right parenthesis", "f(x,y)"],
    ["xyxyx, y", "xy"],
    ["\dfrac{\partial f}{\partial y}∂y∂f​start fraction, \partial, f, divided by, \partial, y, end fraction",
        " $\dfrac{\partial f}{\partial y}$"],
    ["\dfrac{\partial f}{\partial x}∂x∂f​start fraction, \partial, f, divided by, \partial, x, end fraction",
        " $\dfrac{\partial f}{\partial x}$"],
    ["\dfrac{\partial f}{\partial z}∂z∂f​start fraction, \partial, f, divided by, \partial, z, end fraction",
        " $\dfrac{\partial f}{\partial z}$"],

    ["\dfrac{\partial g}{\partial x}∂x∂f​start fraction, \partial, g, divided by, \partial, x, end fraction",
        " $\dfrac{\partial f}{\partial x}$"],
    ["\dfrac{\partial g}{\partial y}∂x∂f​start fraction, \partial, g, divided by, \partial, y, end fraction",
        " $\dfrac{\partial f}{\partial y}$"],
    ["\dfrac{\partial g}{\partial z}∂x∂f​start fraction, \partial, g, divided by, \partial, z, end fraction",
        " $\dfrac{\partial f}{\partial z}$"],
    [" ∂x\partial x∂x\partial, x", " $\partial x$"],
    [" ∂y\partial y∂y\partial, y", " $\partial y$"],
    [" ∂z\partial z∂z\partial, z", " $\partial z$"],
    [" ∂f\partial f∂f\partial, f", " $\partial f$"],
    [" ∂g\partial g∂g\partial, g", " $\partial g$"],
    [" (x_0, y_0)(x0​,y0​)left parenthesis, x, start subscript, 0, end subscript, comma, y, start subscript, 0, end subscript, right parenthesis", " $(x_0, y_0)$"],
    [" f(x0,y0)f(x_0, y_0)f(x0,y0)f, left parenthesis, x, start subscript, 0, end subscript, comma, y, start subscript, 0, end subscript, right parenthesis", " $f(x_0, y_0)$"],
    ["", ""],
    ["", ""],
    [" \\hat{\\textbf{j}}j^​start bold text, j, end bold text, with, hat, on top",
        " \\hat{\\textbf{j}}"],
    [" f(x, y, z)f(x,y,z)f, left parenthesis, x, comma, y, comma, z, right parenthesis", " f(x, y, z)"],
    [" \\nabla f∇fdel, f", " $\\nabla f$"],
    ["\hat{\\textbf{u}}u^start bold text, u, end bold text, with, hat, on top", "\hat{\\textbf{u}}"],
    ["\hat{\\textbf{v}}v^start bold text, v, end bold text, with, hat, on top", "\hat{\\textbf{v}}"],
    ["\hat{\\textbf{i}}i^start bold text, i, end bold text, with, hat, on top", "\hat{\\textbf{i}}"],
    ["\hat{\\textbf{j}}j^start bold text, j, end bold text, with, hat, on top", "\hat{\\textbf{j}}"],
    ["\hat{\\textbf{k}}k^start bold text, k, end bold text, with, hat, on top", "\hat{\\textbf{k}}"],
    ["", ""],
    ["", ""],
    ["", ""],
    ["", ""],
    ["", ""],

]


def main():

    path = os.getcwd()+"/"
    text_replace(path, replace_list)


if __name__ == '__main__':
    global replace_list
    replace_list = replace_list2+generate_multi_charater_repalce_list(3)+generate_multi_number_replace_list(3,500)
    main()
