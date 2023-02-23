import os
# coding=<utf-8>
tr_on=True
tr_off=False

def generate_function_replace_list(TR_MODE):
    # T(t)T(t)T, left parenthesis, t, right parenthesis
    replace_list_function = []
    str1="("
    str2=")"
    str3=", left parenthesis, "
    str4=", right parenthesis"
    for i in range(65, 91):
        c1=str(chr(i).encode('utf-8'))[2]
        for j in range(65, 91):
            c2=str(chr(j).encode('utf-8'))[2]
            replace_list_function.append([" "+c1+str1+c2+str2+c1+str1+c2+str2+c1+str3+c2+str4," "+c1+str1+c2+str2+""])
        for j in range(97, 97+26):
            c2=str(chr(j).encode('utf-8'))[2]
            replace_list_function.append([" "+c1+str1+c2+str2+c1+str1+c2+str2+c1+str3+c2+str4," "+c1+str1+c2+str2+""])

    for i in range(97, 97+26):
        c1=str(chr(i).encode('utf-8'))[2]
        for j in range(65, 91):
            c2=str(chr(j).encode('utf-8'))[2]
            replace_list_function.append([" "+c1+str1+c2+str2+c1+str1+c2+str2+c1+str3+c2+str4," "+c1+str1+c2+str2+""])
        for j in range(97, 97+26):
            c2=str(chr(j).encode('utf-8'))[2]
            replace_list_function.append([" "+c1+str1+c2+str2+c1+str1+c2+str2+c1+str3+c2+str4," "+c1+str1+c2+str2+""])

    if TR_MODE:
        print(replace_list_function)
    return replace_list_function
def generate_differential_variable_repalce_list(TR_MODE):
    # dsdsd, s
    replace_list_differential_variable = []
    str1=" d"
    str2="d"
    str3="d, "
    for i in range(65, 91):
        c1=str(chr(i).encode('utf-8'))[2]
        replace_list_differential_variable.append([str1+c1+str2+c1+str3+c1," "+str1+c1])
    for i in range(97, 97+26):
        c1=str(chr(i).encode('utf-8'))[2]
        replace_list_differential_variable.append([str1+c1+str2+c1+str3+c1," "+str1+c1])
    if TR_MODE:
        print(replace_list_differential_variable)
    return replace_list_differential_variable

def generate_letters_equals_numbers_replace_list(num,TR_MODE):
    #["t = 3t=3t, equals, 3", "t = 3"],
    replace_list_letters_equals_number = []
    str1=" = "
    str2="="
    str3=", equals, "
    for i in range(65, 91):
        c1=str(chr(i).encode('utf-8'))[2]
        for j in range(num):
            replace_list_letters_equals_number.append([c1+str1+str(j)+c1+str2+str(j)+c1+str3+str(j),c1+str1+str(j)])
    for i in range(97, 97+26):
        c1=str(chr(i).encode('utf-8'))[2]
        for j in range(num):
            replace_list_letters_equals_number.append([c1+str1+str(j)+c1+str2+str(j)+c1+str3+str(j),c1+str1+str(j)])
    if TR_MODE:
        print(replace_list_letters_equals_number)
    return replace_list_letters_equals_number
def generate_letters_subscript_numbers_replace_list(num,TR_MODE):
    replace_list_letters_subscript_numbers = []
    #[" t_0t0 t, start subscript, 0, end subscript", " $t_0$"],
    #str1="t_0t0 t, start subscript, 0, end subscript"
    str1="{letter}_{subscript}{letter}{subscript} {letter}, start subscript, {subscript}, end subscript"

    str2="${letter}_{subscript}$"
    for i in range(65, 91):
        c1=str(chr(i).encode('utf-8'))[2]
        for j in range(num):

            replace_list_letters_subscript_numbers.append([str1.format(letter=c1,subscript=j),str2.format(letter=c1,subscript=j)])
            #replace_list_letters_subscript_numbers.append([" "+c1+str1+str(j)+c1+str(j)+str2+c1+str3+str(j)+str4," $"+c1+str1+str(j)+"$"])
    for i in range(97, 97+26):
        c1=str(chr(i).encode('utf-8'))[2]
        for j in range(num):
            replace_list_letters_subscript_numbers.append([str1.format(letter=c1,subscript=j),str2.format(letter=c1,subscript=j)])
            #replace_list_letters_subscript_numbers.append([" "+c1+str1+str(j)+c1+str(j)+str2+c1+str3+str(j)+str4," $"+c1+str1+str(j)+"$"])
    if TR_MODE:
        print(replace_list_letters_subscript_numbers)
    return replace_list_letters_subscript_numbers
def generate_nabla_variable_replace_list(TR_MODE):
    replace_list_nabla_variable = []
    # [" \\nabla f∇fdel, f", " $\\nabla f$"],
    str1 = " \\nabla "
    str11=" $\\nabla "
    str2="∇"
    str3="del, "
    for i in range(65, 91):
        c1=str(chr(i).encode('utf-8'))[2]
        replace_list_nabla_variable.append([str1+c1+str2+c1+str3+c1,str11+c1+"$"])
    for i in range(97, 97+26):
        c1=str(chr(i).encode('utf-8'))[2]
        replace_list_nabla_variable.append([str1+c1+str2+c1+str3+c1,str11+c1+"$"])
    if TR_MODE:
        print(replace_list_nabla_variable)
    return replace_list_nabla_variable
def generate_partial_variable_replace_list(TR_MODE):
    replace_list_partial_variable = []
    #[" ∂x\partial x∂x\partial, x", " $\partial x$"],
    str1 = " ∂"

    str2="\partial "
    str22=" $\partial "
    str3="∂"
    str4="\partial, "
    for i in range(65, 91):
        c1=str(chr(i).encode('utf-8'))[2]
        replace_list_partial_variable.append([str1+c1+str2+c1+str3+c1+str4+c1,str22+c1+"$"])
    for i in range(97, 97+26):
        c1=str(chr(i).encode('utf-8'))[2]
        replace_list_partial_variable.append([str1+c1+str2+c1+str3+c1+str4+c1,str22+c1+"$"])
    if TR_MODE:
        print(replace_list_partial_variable)
    return replace_list_partial_variable
def generate_partial_function_replace_list(TR_MODE):
    replace_list_partial_function = []
    # ["\dfrac{\partial f}{\partial y}∂y∂f start fraction, \partial, f, divided by, \partial, y, end fraction",
    #    " $\dfrac{\partial f}{\partial y}$"]
    str1 = " \\dfrac{\\partial "
    str11=" $\\dfrac{\\partial "
    str2="}{\\partial "
    str3="}∂"
    str33="}$"
    str4="∂"
    str5=" start fraction, \\partial, "
    str6=", divided by, \\partial, "
    str7=", end fraction"
    for i in range(65, 91):

        # Convert the integer to a character
        c = chr(i).encode('utf-8')
        # print(c+c+c)

        c2 = str(c)[2]
        # print(c2[2])
        for j in range(65, 91):
            c3 = str(chr(j).encode('utf-8'))[2]
            replace_list_partial_function.append([str1+c2+str2+c3+str3+c3+str4+c2+str5+c2+str6+c3+str7,str11+c2+str2+c3+str33])
    for i in range(97, 97+26):
        c = chr(i).encode('utf-8')
        # Convert the integer to a character
        c2 = str(c)[2]
        # print(c2[2])
        for j in range(97, 97+26):
            c3 = str(chr(j).encode('utf-8'))[2]
            replace_list_partial_function.append([str1+c2+str2+c3+str3+c3+str4+c2+str5+c2+str6+c3+str7,str11+c2+str2+c3+str33])
    if TR_MODE:
        print(replace_list_partial_function)

    return replace_list_partial_function

def generate_bold_hat_replace_list(TR_MODE):
    #[" \hat{\\textbf{u}}u^start bold text, u, end bold text, with, hat, on top"," \hat{\\textbf{u}}"]
    replace_list_bold_hat = []
    str1 = " \\hat{\\textbf{"
    str11=" $\\hat{\\textbf{"
    str2="}}"
    str22="}}$"
    str3="^start bold text, "
    str4=", end bold text, with, hat, on top"
    for i in range(65, 91):

        # Convert the integer to a character
        c = chr(i).encode('utf-8')
        # print(c+c+c)

        c2 = str(c)[2]
        # print(c2[2])

        replace_list_bold_hat.append([str1+c2+str2+c2+str3+c2+str4,str11+c2+str22])
    for i in range(97, 97+26):
        c = chr(i).encode('utf-8')
        # Convert the integer to a character
        c2 = str(c)[2]
        # print(c2[2])
        replace_list_bold_hat.append([str1+c2+str2+c2+str3+c2+str4,str1+c2+str2])
    if TR_MODE:
        print(replace_list_bold_hat)

    return replace_list_bold_hat


def generate_bold_vec_replace_list(TR_MODE):
    replace_list_bold_vec = []

    # \\vec{\\textbf{v}}vstart bold text, v, end bold text, with, vector, on top
    str0="\\vec{\\textbf{%s}}%sstart bold text, %s, end bold text, with, vector, on top"

    str1="$\\vec{\\textbf{%s}}$"

    # Iterate through all the English letters
    for i in range(65, 91):

        # Convert the integer to a character
        c2=str(chr(i).encode('utf-8'))[2]
        replace_list_bold_vec.append([str0%(c2,c2,c2),str1%(c2)])



    for i in range(97, 97+26):

        # Convert the integer to a character
        c2=str(chr(i).encode('utf-8'))[2]
        replace_list_bold_vec.append([str0%(c2,c2,c2),str1%(c2)])

    if TR_MODE:
        print(replace_list_bold_vec)
    #print(replace_list_bold_vec)
    return replace_list_bold_vec

def generate_multi_number_replace_list(num, num_base, TR_MODE):
    replace_list_multi_number = []

    for i in range(num_base):
        replace_list_multi_number.append([" "+num*str(i), " "+str(i)])
    if TR_MODE:
        print(replace_list_multi_number)
    return replace_list_multi_number


def generate_multi_charater_repalce_list(num, TR_MODE):
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
    if TR_MODE:
        print(replace_list_multi_charactor)
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
                    line = line.replace(
                        replace_list[j][0], replace_list[j][1])
                f2.write(line)


replace_list_khanacademy = [
    [" ", " "],

    ["​", " "],
    ["", ""],
    ["", ""],
    ["", ""],
    ["", ""],
    ["", ""],
    ["", ""],
    #["\\\\", "\\"],
    ["\\left\\[", ""],
    ["\\right\\]", ""],
    ["\\left[", ""],
    ["\\right]", ""],
    ["{array}", "{bmatrix}"],
    ["{bmatrix}{c}", "{bmatrix}"],
    ["{bmatrix}{cc}", "{bmatrix}"],
    ["{bmatrix}{ccc}", "{bmatrix}"],
    ["{bmatrix}{cccc}", "{bmatrix}"],
        ["{bmatrix}{ccccc}", "{bmatrix}"],
    # color+A  \textcolor{color} todolist
    ["\\blueD", "\\textcolor{#11accd}"],
    ["\\blueE", "\\textcolor{#0c7f99}"],
    ["\\greenD", "\\textcolor{#1fab54}"],
    ["\\greenE", "\\textcolor{#0d923f}"],
    ["\\maroonD", "\\textcolor{maroon}"],
    ["\\goldD", "\\textcolor{gold}"],
    ["\\redD", "\\textcolor{#e84d39}"],
    ["\\redE", "\\textcolor{#bc2612}"],
    ["\\purpleC", "\\textcolor{purple}"],
    ["\\_", "_"],


    ["f(x, y)f(x,y)f, left parenthesis, x, comma, y, right parenthesis", "f(x,y)"],
    ["xyxyx, y", "xy"],
["(x, y)(x,y)left parenthesis, x, comma, y, right parenthesis", "(x,y)"],
    ["(x_0, y_0)(x0 ,y0 )left parenthesis, x, start subscript, 0, end subscript, comma, y, start subscript, 0, end subscript, right parenthesis", " $(x_0, y_0)$"],
    ["f(x0,y0)f(x_0, y_0)f(x0,y0)f, left parenthesis, x, start subscript, 0, end subscript, comma, y, start subscript, 0, end subscript, right parenthesis", " $f(x_0, y_0)$"],
    ["\kappaκ\kappa", " $\kappa$"],
    ["\\vec{\\textbf{s}}(t)s(t)start bold text, s, end bold text, with, vector, on top, left parenthesis, t, right parenthesis", " $\\vec{\\textbf{s}}(t)$"],

    ["f(x, y, z)f(x,y,z)f, left parenthesis, x, comma, y, comma, z, right parenthesis", " f(x, y, z)"],
    #[" \\nabla f∇fdel, f", " $\\nabla f$"],

    ["\dfrac{dT}{ds}dsdT start fraction, d, T, divided by, d, s, end fraction", " $\dfrac{dT}{ds}$"],
    #[" t_0t0 t, start subscript, 0, end subscript", "$t_0$"],
    #[" t = 3t=3t, equals, 3", "t = 3"],
    ["[Hide explanation]", "Explanation"],
    ["    A\n", ""],
    ["    B\n", ""],
    ["    C\n", ""],
    ["    D\n", ""],
        ["Check\n", ""],
            ["Choose 1 answer:\n", ""],
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
    replace_list = replace_list_khanacademy + \
        generate_multi_charater_repalce_list(
            3,tr_off)+\
                generate_multi_number_replace_list(3, 500,tr_off)+\
                    generate_bold_vec_replace_list(tr_off)+\
                        generate_bold_hat_replace_list(tr_off)+\
                            generate_partial_function_replace_list(tr_off)+\
                                generate_partial_variable_replace_list(tr_off)+\
                                    generate_nabla_variable_replace_list(tr_off)+\
                                        generate_letters_subscript_numbers_replace_list(10,tr_off)+\
                                            generate_letters_equals_numbers_replace_list(10,tr_off)+\
                                                generate_differential_variable_repalce_list(tr_off)+\
                                                    generate_function_replace_list(tr_off)
    replace_list=[]
    main()
