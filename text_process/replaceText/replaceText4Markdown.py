import os
# coding=<utf-8>
# replace text with given list
# Generate 26 uppercase English letters and lowercase English letters in string format


def generate_multi_number_replace_list(num, num_base):
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
    # print(replace_list_multi_charactor)
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
    ["\hat{\\textbf{u}}u^start bold text, u, end bold text, with, hat, on top",
        "\hat{\\textbf{u}}"],
    ["\hat{\\textbf{v}}v^start bold text, v, end bold text, with, hat, on top",
        "\hat{\\textbf{v}}"],
    ["\hat{\\textbf{i}}i^start bold text, i, end bold text, with, hat, on top",
        "\hat{\\textbf{i}}"],
    ["\hat{\\textbf{j}}j^start bold text, j, end bold text, with, hat, on top",
        "\hat{\\textbf{j}}"],
    ["\hat{\\textbf{k}}k^start bold text, k, end bold text, with, hat, on top",
        "\hat{\\textbf{k}}"],
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
    replace_list = replace_list2 + \
        generate_multi_charater_repalce_list(
            3)+generate_multi_number_replace_list(3, 500)
    main()
