#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import datetime
import shutil



def rename_files_end(path, old_extension, new_extension, file_remove_length=0, dir_remove_length=0):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(old_extension):
                os.rename(os.path.join(root, file),
                          os.path.join(root, file[:-(len(old_extension)+file_remove_length)]+new_extension))
        for dir in dirs:
            if dir_remove_length > 0:
                os.rename(os.path.join(root, dir), os.path.join(
                    root, dir[:-(dir_remove_length)]))

def rename_files_start(num_remove,extensions=None):
    # 获取当前目录下所有文件的文件名
    files = os.listdir()

    for filename in files:
        # 如果文件名以"."开头，说明是隐藏文件，跳过
        if filename.startswith("."):
            continue

        # 获取文件名的后缀名
        suffix = os.path.splitext(filename)[-1]
        # 如果设置了扩展名过滤器，且当前文件扩展名不在过滤器中，跳过
        if extensions and suffix not in extensions:
            continue
        # 获取文件名的新名称（去除前四位）
        new_filename = filename[num_remove:]

        # 生成文件的旧路径和新路径
        old_path = os.path.join(os.getcwd(), filename)
        new_path = os.path.join(os.getcwd(), new_filename)

        # 重命名文件
        os.rename(old_path, new_path)

        # 输出修改后的文件名
        print("文件名从 {} 变为 {}".format(filename, new_filename))

def rename_files(path, replace_list):
    for root, dirs, files in os.walk(path):
        for file in files:
            file_old = file
            for replace_str in replace_list:
                if file.find(replace_str[0]) != -1:
                    file = file.replace(replace_str[0], replace_str[1])
            os.rename(os.path.join(root, file_old),
                      os.path.join(root, file))
        for dir in dirs:
            dir_old = dir
            for replace_str in replace_list:
                if dir.find(replace_str[0]) != -1:
                    dir = dir.replace(replace_str[0], replace_str[1])
            os.rename(os.path.join(root, dir_old),
                      os.path.join(root, dir))

# remove line with search_str


def remove_line(path, search_list):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.md'):
                with open(os.path.join(root, file), 'r', encoding='UTF-8') as f:
                    lines = f.readlines()
                with open(os.path.join(root, file), 'w', encoding='UTF-8') as f:
                    for l in lines:
                        flag = 0
                        for search_str in search_list:
                            if l.find(search_str) != -1:
                                flag = flag+1
                        if flag == 0:
                            f.write(l)


def mulu_process(replace_list):
    with open("目录.md", 'r', encoding='UTF-8') as f:
        lines = f.readlines()
    with open("目录.md", 'w', encoding='UTF-8') as f:
        for l in lines:
            for replace_str in replace_list:
                if l.find(replace_str[0]) != -1:
                    l = l.replace(replace_str[0], replace_str[1])
            f.write(l)


def num2str_title(num):
    if num < 10:
        return '00'+str(num)
    elif num < 100:
        return '0'+str(num)
    else:
        return str(num)


def search_file(path):
    with (open("目录.md", 'r', encoding='UTF-8')) as f:
        lines = f.readlines()
        for root, dirs, files in os.walk(path):
            counter = 0
            for line in lines:
                if line[:-1]+'.md' in files:
                    counter = counter+1
                    os.rename(os.path.join(
                        root, line[:-1]+'.md'), os.path.join(root, num2str_title(counter)+line[:-1]+'.md'))
                    print(line[:-1]+'.md')


def global_replace_list():
    global replace_list
    replace_list = [["「", "_"], ["」", "_"], [
        "，", ","], ["：", "_"], [" ", "_"], ["“", "_"], ["”", "_"], ["？", "?"], ["·", "_"]]


def remove_line_test1():
    path = os.getcwd()
    search_list = ["- created: 2023", "- source: https://www.zhihu.com"]
    remove_line(path, search_list)


def rename_files_end_test1():
    path = os.getcwd()
    rename_files_end(path, '.md', '.md', 14, 14)


def replace_name_test1():
    path = os.getcwd()
    global_replace_list()
    rename_files(path, replace_list)


def tianjiaxiahuaxian():
    for root, dirs, files in os.walk("."):
        for i in range(1, 38):
            for file in files:
                if file[:3] == num2str_title(i):
                    os.rename(os.path.join(root, file),
                              os.path.join(root, file[:3]+"_"+file[3:]))


def back_up_dir_tree(path):

    time_str = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    # get the father path
    father_path = os.path.abspath(os.path.dirname(path) + os.path.sep + ".")
    # get current dir name
    dir_name = os.path.basename(path)
    back_path = os.path.join(father_path, dir_name+"_"+time_str)
    # os.mkdir(back_path)
    # copy all files in the current path to the back_path
    shutil.copytree(path, back_path)

def back_up_dir(src_dir):

    time_str = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    # get the father path
    father_path = os.path.abspath(os.path.dirname(src_dir) + os.path.sep + ".")
    # get current dir name
    dir_name = os.path.basename(src_dir)
    back_path = os.path.join(father_path, dir_name+"_"+time_str)
    # os.mkdir(back_path)
    if not os.path.exists(back_path):
        os.makedirs(back_path)
    # copy all files in the current path to the back_path
    for filename in os.listdir(src_dir):
        src_path = os.path.join(src_dir, filename)
        dst_path = os.path.join(back_path, filename)
        if os.path.isfile(src_path):
            shutil.copy2(src_path, dst_path)

# remove multiple lines with space


def remove_line_multi_space(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.md'):
                with open(os.path.join(root, file), 'r', encoding='UTF-8') as f:
                    lines = f.readlines()
                with open(os.path.join(root, file), 'w', encoding='UTF-8') as f:
                    for i in range(len(lines)):
                        space_list = ["\n", "    \n"]
                        if i != len(lines)-1:
                            if lines[i] == ' ' and lines[i+1] == ' ':
                                continue
                            if lines[i] in space_list and lines[i+1] in space_list:
                                continue
                        f.write(lines[i])

# copy all files in the current path into a single file


def copy_all_files(path):
    with open("all_files.md", 'w', encoding='UTF-8') as f:
        for root, dirs, files in os.walk(path):
            for i in range(1, 38):
                for file in files:
                    if file[:3] == num2str_title(i) and file.endswith('.md'):
                        with open(os.path.join(root, file), 'r', encoding='UTF-8') as f1:
                            lines = f1.readlines()
                        for line in lines:
                            f.write(line)


def process_feiman_head2():
    for root, dirs, files in os.walk("."):
        for i in range(1, 38):
            for file in files:
                if file[:3] == num2str_title(i) and file.endswith('.md'):
                    with open(os.path.join(root, file), 'r', encoding='UTF-8') as f:
                        lines = f.readlines()
                    with open(os.path.join(root, file), 'w', encoding='UTF-8') as f:
                        for i in range(len(lines)):
                            if lines[i][0:3] == "## " and lines[i+1] != "\n":
                                f.write(lines[i][:-1])
                            else:
                                f.write(lines[i])


def search_in_mulu():
    counter = 0
    with open("mulu.md", 'r', encoding='UTF-8') as f:
        lines = f.readlines()
    for root, dirs, files in os.walk("."):
        for line in lines:
            if line[:-1]+'.md' in files:
                counter = counter+1
                # print(line[:-1]+'.md')

            else:
                print(line[:-1]+'.md')
        # print(files)


def base_on_mulu_markdown_rename_files():
    counter = 0
    with open("mulu.md", 'r', encoding='UTF-8') as f:
        lines = f.readlines()
    for root, dirs, files in os.walk("."):
        for line in lines:
            if line[:-1]+'.md' in files:
                counter = counter+1
                # print(line[:-1]+'.md')
                os.rename(os.path.join(root, line[:-1]+'.md'),
                          os.path.join(root, num2str_title(counter)+"_"+line[:-1]+'.md'))

import os

def create_md_files_from_markdown_file(markdown_file):
    """
    读取markdown文件，将每一行内容生成一个md文件，并根据行号、内容、扩展名为文件命名。
    如果该文件已经存在，则跳过该行，继续生成下一行的文件。

    :param markdown_file: 要读取的markdown文件名
    """
    with open(markdown_file, encoding='utf-8') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            # 构造文件名
            filename = num2str_title(i+1)+f"_{line.strip()}.md"
            # 检查文件是否已存在，如果是则跳过
            if os.path.exists(filename):
                continue
            # 创建新的md文件并写入内容
            with open(filename, 'w', encoding='utf-8') as new_file:
                #new_file.write(line)
                pass

def test_create_md_files_from_markdown_file():

    create_md_files_from_markdown_file('test.md')
    # 检查生成的文件是否存在
    assert os.path.exists('1_第一行_.md')
    assert os.path.exists('2_第二行_.md')
    assert os.path.exists('3_第三行_.md')
    # # 删除测试用的markdown文件和生成的md文件
    # os.remove('test.md')
    # os.remove('1_第一行_.md')
    # os.remove('2_第二行_.md')
    # os.remove('3_第三行_.md')
import glob
import os

def delete_non_example_md_files():
    for file_path in glob.glob('*.md'):
        if file_path != 'example.md' and file_path.endswith('.md'):
            os.remove(file_path)
def open_folder_in_windows(folder_path):
    """根据文件夹路径在Windows文件管理器中打开文件夹。

    参数:
    folder_path (str): 要打开的文件夹路径。

    返回:
    无返回值。
    """
    if os.path.exists(folder_path):
        os.startfile(folder_path)
    else:
        print(f"文件夹路径 {folder_path} 不存在。")

def open_assets_folder():
    CWD=os.getcwd()
    #print(CWD)
    assets_path_front="C:/BaiduSyncdisk/assets"
    KG_path_front="C:\\BaiduSyncdisk\\assets\\KG"
    #split paht CWD after KG, replace \ with /
    KG_path_back=CWD.split("\KG")[1].replace("\\", "/")

    #print(KG_path_back)
    assets_path=assets_path_front+KG_path_back
    #print(assets_path)
    open_folder_in_windows(assets_path)

import os
import time


def add_timestamp_to_filenames():
    current_dir = os.getcwd()
    timestamp = int(time.time())
    for filename in os.listdir(current_dir):
        if os.path.isfile(os.path.join(current_dir, filename)) and not filename.endswith(".py"):
            filename_without_ext, ext = os.path.splitext(filename)
            new_filename = f"{filename_without_ext}_{timestamp}{ext}"
            os.rename(os.path.join(current_dir, filename), os.path.join(current_dir, new_filename))
def text_replace(root_dir: str, replace_list: list):
    dest_dir = os.path.join(root_dir, 'des')
    if not os.path.isdir(dest_dir):
        os.mkdir(dest_dir)

    for filename_with_ext in os.listdir(root_dir):
        if filename_with_ext.endswith('.md'):
            src_path = os.path.join(root_dir, filename_with_ext)
            dest_path = os.path.join(dest_dir, filename_with_ext)

            with open(src_path, 'r', encoding='UTF-8') as f_src, open(dest_path, 'w', encoding='UTF-8') as f_dest:
                for line in f_src:
                    for replace_item in replace_list:
                        line = line.replace(replace_item[0], replace_item[1])
                    f_dest.write(line)
def test_text_replace(timestamp: int = 1676880280):
    text_replace_list_mdx2md=[[r'<Figure image="', r'![]('],
                              ['" id="distribution"/>', r')'],
                              ['<Figure video="', r'![]('],
                               ['" show="video"/>', r')'],
                            ['" show="video" />', r')'],
                              ['"/>', r')'],['" />', r')'],
                              ['" image="', ')'+'\n'+'![]('],
                            ['" video="', ')'+'\n'+'![]('],
                                ["question=","- question"+"\n"],
                                ["choice1=","- choice1 "],
                                ["choice2=","- choice2 "],
                                ["choice3=","- choice3 "],
                                ["choice4=","- choice4 "],
                                ["answer=","- answer "],
                                ["",""],
                                ["",""],
                                ["",""],
                                ["</Question>",""],
                              ["</LessonLink>",""],
                              ['<LessonLink id="differential-equations">',"(differential-equations) "],
                              ['<LessonLink id="fourier-series">',"(fourier-series) "]]
    text_replace_list_mdx2md2=[['.png', r'_'+str(timestamp)+'.png'],
                              ['.jpeg', r'_'+str(timestamp)+'.jpeg'],
                              ['.mp4', r'_'+str(timestamp)+'.mp4'],
                              ]
    replace_list=text_replace_list_mdx2md
    #+text_replace_list_mdx2md2
    cwd=os.getcwd()
    text_replace(cwd, replace_list)
if __name__ == "__main__":
    path=os.getcwd()
    back_up_dir(path)
    test_text_replace(1677211210)



