#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import difflib
import time
import glob
import os
import datetime
import shutil
import argparse


def remove_filesname_end(path, old_extension, new_extension, file_remove_length=0, dir_remove_length=0):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(old_extension):
                os.rename(os.path.join(root, file),
                          os.path.join(root, file[:-(len(old_extension)+file_remove_length)]+new_extension))
        for dir in dirs:
            if dir_remove_length > 0:
                os.rename(os.path.join(root, dir), os.path.join(
                    root, dir[:-(dir_remove_length)]))


def rename_files_start(num_remove, extensions=None):
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
    remove_filesname_end(path, '.md', '.md', 2, 2)


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
    back_path = os.path.join(src_dir, dir_name+"_"+time_str)
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
                # new_file.write(line)
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
    CWD = os.getcwd()
    # print(CWD)
    assets_path_front = "C:/BaiduSyncdisk/assets"
    KG_path_front = "C:\\BaiduSyncdisk\\assets\\KG"
    # split paht CWD after KG, replace \ with /
    KG_path_back = CWD.split("\KG")[1].replace("\\", "/")

    # print(KG_path_back)
    assets_path = assets_path_front+KG_path_back
    # print(assets_path)
    open_folder_in_windows(assets_path)


def add_timestamp_to_filenames():
    current_dir = os.getcwd()
    timestamp = int(time.time())
    for filename in os.listdir(current_dir):
        if os.path.isfile(os.path.join(current_dir, filename)) and not filename.endswith(".py"):
            filename_without_ext, ext = os.path.splitext(filename)
            new_filename = f"{filename_without_ext}_{timestamp}{ext}"
            os.rename(os.path.join(current_dir, filename),
                      os.path.join(current_dir, new_filename))


def text_replace(root_dir: str, replace_list: list):

    output_dir=create_output_directory()
    for filename_with_ext in os.listdir(root_dir):
        if filename_with_ext.endswith('.md'):
            src_path = os.path.join(root_dir, filename_with_ext)
            dest_path = os.path.join(output_dir, filename_with_ext)

            with open(src_path, 'r', encoding='UTF-8') as f_src, open(dest_path, 'w', encoding='UTF-8') as f_dest:
                for line in f_src:
                    for replace_item in replace_list:
                        line = line.replace(replace_item[0], replace_item[1])
                    f_dest.write(line)


def mdx2md_b1(timestamp: int = 1676880280):
    text_replace_list_mdx2md1 = [[r'<Figure image="', r'![]('],
                                 ['" id="distribution"/>', r')'],
                                 ['<Figure video="', r'![]('],
                                 ['" show="video"/>', r')'],
                                 ['" show="video" />', r')'],
                                 ['"/>', r')'], ['" />', r')'],
                                 ['" image="', ')'+'\n'+'![]('],
                                 ['" video="', ')'+'\n'+'![]('],
                                 ["question=", "- question"+"\n"],
                                 ["choice1=", "- choice1 "],
                                 ["choice2=", "- choice2 "],
                                 ["choice3=", "- choice3 "],
                                 ["choice4=", "- choice4 "],
                                 ["answer=", "- answer "],
                                 ["", ""],
                                 ["", ""],
                                 ["", ""],
                                 ["</Question>", ""],
                                 ["</LessonLink>", ""],
                                 ['<LessonLink id="differential-equations">',
                                 "(differential-equations) "],
                                 ['<LessonLink id="fourier-series">', "(fourier-series) "]]
    text_replace_list_mdx2md2 = [['.png', r'_'+str(timestamp)+'.png'],
                                 ['.jpeg', r'_'+str(timestamp)+'.jpeg'],
                                 ['.mp4', r'_'+str(timestamp)+'.mp4'],
                                 ]
    text_replace_list_mdx2md3 = [[r'<Figure', r''],
                                 ['/>', r''],
                                 ["<PiCreature", ""],
                                 ["show=\"video\"", ""],
                                 ["", ""],
                                 ["", ""],
                                 ["<Question", "---"],
                                 ["</Question>", "---"],
                                 ]
    replace_list = text_replace_list_mdx2md3
    # +text_replace_list_mdx2md2
    cwd = os.getcwd()
    text_replace(cwd, replace_list)


def mdx2md(timestamp: int = 1676880280):
    output_dir = create_output_directory()
    cwd = os.getcwd()
    # text_replace_list_mdx2md3 = [
    #                              ]
    # replace_list = text_replace_list_mdx2md3
    # <Figure
    for filename_with_ext in os.listdir(cwd):
        if filename_with_ext.endswith('.md'):
            src_path = os.path.join(cwd, filename_with_ext)
            dest_path = os.path.join(output_dir, filename_with_ext)

            # with open(src_path, 'r', encoding='UTF-8') as f_src, open(dest_path, 'w', encoding='UTF-8') as f_dest:
            #     for line in f_src:
            #         for replace_item in replace_list:
            #             line = line.replace(replace_item[0], replace_item[1])
            #         f_dest.write(line)
            with open(src_path, 'r', encoding='UTF-8') as f_src:
                content = f_src.read()
            # Define the regex pattern and replacement string

            replace_list_regex = [
                                 [r"<PiCreature", r""],
                                 [r"show=\"video\"\n", r""],
                                 [r"<!--", r""],
                                 [r"-->", r""],
                                 [r"<Question", r"---"],
                                 [r"<FreeResponse>", r"---"],
                                    [r"</FreeResponse>", r"---"],
                                 [r"</Question>", r"---"],
                [r'<Figure[\n ]{1,}image="(.+)(\.svg|\.png|\.jpg)".{0,}/>', r'![](\1_'+str(timestamp)+r'\2)'],
                                  [r'<Accordion\stitle=".+">\n', r''],
                                  [r'</Accordion>\n', r''],
                                  [r'emotion="\w+"[ \t]+\n', r''],
                                  [r'flip=\{(true|false)\}\n', r''],

                                  [r'answer={(\d)}[ \t]{0,}\n>', r'\n<details><summary>answer</summary><p>Choice= \1</p></details>\n\n- **Explanation**'],
                                  [r'[ \t]{0,}question="(.+\?)"',r'- **Question**\n\t\1'],
                                  [r'[ \t]{0,}choice1="(.+)"',r'    - **Choice 1=** \1'],
                                  [r'[ \t]{0,}choice2="(.+)"',r'    - **Choice 2=** \1'],
                                    [r'[ \t]{0,}choice3="(.+)"',r'    - **Choice 3=** \1'],
                                    [r'[ \t]{0,}choice4="(.+)"',r'    - **Choice 4=** \1'],
                                    [r'video=".+\.mp4"', r''],
                                    [r'show="video"', r''],
                                    [r'([ \t]{0,}\n){3,}', r'\1\1'],
                                    ['/>', r''],]

            for i in range(len(replace_list_regex)):
                pattern = replace_list_regex[i][0]
                replacement = replace_list_regex[i][1]

                # Perform the regex replacement
                content = re.sub(pattern, replacement, content)
            # Write the modified content to the output Markdown file with UTF-8 encoding
            with open(dest_path, 'w', encoding='utf-8') as file:
                file.write(content)


def copy_timestamps_and_index_2_root(directory=None):
    """
    Copies files with 'timestamps' in their name and '.mdx' extension to the root directory
    with an updated name. Also copies files with 'index' in their name and '.mdx' extension
    to the root directory with an updated name.
    """
    if directory is None:
        directory = os.getcwd()

    current_folder_name = os.path.basename(directory)
    filelist = os.listdir(directory)

    for file in filelist:
        file_name, file_extension = os.path.splitext(file)

        if "timestamps" in file_name and file_extension == '.md':
            new_file_name1 = f"timestamps_{current_folder_name}.md"
            dest_path1 = os.path.join(directory, '../..', new_file_name1)

            if not os.path.exists(dest_path1):
                shutil.copy(file, dest_path1)

        if file_extension == '.mdx':
            if "index" in file_name:
                new_file_name = f"{current_folder_name}.md"
                dest_path = os.path.join(directory, '../..', new_file_name)

                if not os.path.exists(dest_path):
                    shutil.copy(file, dest_path)

def search_str_url_4_file_vid(str_url):
    url_pattern_4_file_vid=r'(!\[.+\..+\]\(file:///C:%5CBaiduSyncdisk%5Cassets(%5C.+){1,}\.\w+)(\))'
    match1=re.search(url_pattern_4_file_vid, str_url)
    if not match1:
        raise Exception('No match found')
    return match1

def convert_min_sec_to_seconds(time_str):
    time_line_pattern_str=r'\((\d{1,2}:\d{1,2})-(\d{1,2}:\d{1,2})\)[ ]{1,}'
    time_stamp_pattern_str=r'(\d{1,2}):(\d{1,2})'
    match=re.search(time_line_pattern_str, time_str)
    if match:
        time_line_start=match.group(1)
        time_line_end=match.group(2)
        time_line_start_seconds=int(time_line_start.split(':')[0])*60+int(time_line_start.split(':')[1])
        return time_line_start_seconds
    else:
        match = re.search(time_stamp_pattern_str, time_str)
        if match:
            time_seconds = int(match.group(1)) * 60 + int(match.group(2))
            return time_seconds
        else:
            return None

def create_output_directory():
    output_dir=os.path.join(os.getcwd(), 'output')
    if not os.path.isdir(output_dir):
        os.mkdir(output_dir)
    return output_dir

def create_new_file_name(file):
    if not file.endswith('.md'):
        filename_without_ext=os.path.splitext(file)[0]
        new_file_name=filename_without_ext+'.md'
    else:
        new_file_name=file
    print(new_file_name)
    return new_file_name

#0
def list_time_head_textshort_text_to_vid_timeline_md(timeline_data,file,match):
    print(timeline_data)

    output_dir=create_output_directory()
    new_file_name=create_new_file_name(file)
    with open(os.path.join(output_dir, new_file_name), 'w', encoding='UTF-8') as f:
        for i, (start_time, heading, short_text, text) in enumerate(timeline_data):
            start_time_sec = int(start_time)

            if i == len(timeline_data) - 1:
                end_time_sec = start_time_sec + 999
            else:
                end_time_sec = int(timeline_data[i + 1][0])

            if heading:
                f.write(f"## {heading}\n\n")

                i_temp = i
                flag_find_next_head = False
                while i_temp < len(timeline_data) - 1:
                    i_temp += 1
                    if timeline_data[i_temp][1]:
                        end_time_sec2 = int(timeline_data[i_temp][0])
                        vid_line = f"{match.group(1)}#t={start_time_sec},{end_time_sec2}{match.group(3)}"
                        f.write(f"{vid_line}\n\n")
                        flag_find_next_head = True
                        break

                if not flag_find_next_head:
                    vid_line = f"{match.group(1)}#t={start_time_sec}{match.group(3)}"
                    f.write(f"{vid_line}\n\n")

            if short_text:
                f.write(f"- {short_text}\n\n")

            if short_text or text:
                vid_line = f"{match.group(1)}#t={start_time_sec},{end_time_sec}{match.group(3)}"
                f.write(f"{vid_line}\n\n")

            if text:
                f.write(f"{text}\n\n")



def get_list_time_head_textshort_text_4_file(file,key_word):
    print("start to generate time line for video and head text:")
    number_list_bullet_pattern_str=r'((\d{1,2}\.)|-)[ ]{1,}'
    head_pattern_str=r'(([\w:-]+ ){1,})'
    time_line_pattern_str=r'\((\d{1,2}:\d{1,2})-{0,1}(\d{1,2}:\d{1,2}){0,1}\)[ ]{1,}'
    time_stamp_pattern_str=r'\((\d{1,2}):(\d{1,2})\)'
    text_pattern_str=r'(.+)\n{0,1}'
    #number_list_head_time_text_pattern_str=r'((\d{1,2}\.)|(-))[ ]{1,}([\w, ]+):[ ]\((\d{1,2}:\d{1,2})\)[ ](.+)'
    number_list_head_time_text_pattern_str=number_list_bullet_pattern_str+head_pattern_str+time_stamp_pattern_str+text_pattern_str
    number_list_head_time_pattern_str=r'(\d{1,2}):(\d{1,2})\s+(.+)'

    time_text_pattern_str=r'\((\d{1,2}):(\d{1,2})\)[ ]{0,}([^\n]+)[\n]{0,}'

    pattern_dict=dict()
    pattern_dict["timestamps"]=number_list_head_time_pattern_str
    pattern_dict["summary_base_on_chatgpt"]=number_list_head_time_text_pattern_str
    pattern_dict["subtitle"]=time_text_pattern_str
    list_time_head_textshort_text=[]
    with open(os.path.join(os.getcwd(), file), 'r', encoding='UTF-8') as f:
        lines = f.readlines()

    for line in lines:
        time_line_start_seconds=convert_min_sec_to_seconds(line)
        if time_line_start_seconds!=None:
            if key_word in pattern_dict:
                pattern_str=pattern_dict[key_word]
                match=re.search(pattern_str, line)
                if match:
                    if key_word=="timestamps":
                        list_time_head_textshort_text.append([time_line_start_seconds, match.group(3),None,None])
                    elif key_word=="summary_base_on_chatgpt":
                        for i in range(len(match.groups())):
                            print(i,match.group(i))
                        list_time_head_textshort_text.append([time_line_start_seconds, match.group(3),match.group(7),None])
                    elif key_word=="subtitle":
                        list_time_head_textshort_text.append([time_line_start_seconds, None,None,match.group(3)])
                else:
                    print("no match for line:",line)
                    print(key_word)
    print("List of time, heading, short text, text:")
    print(list_time_head_textshort_text)
    return list_time_head_textshort_text

def timestamps_3blue1brown_2_timeline(str_url):
    #process url
    #str_url=r'![007_limits.mp4](file:///C:%5CBaiduSyncdisk%5Cassets%5CO%5CO1%5CO17%5CO172%5CCalculus%203Blue1Brown%5Cassets%5Cbvids%5C007_limits.mp4)'
    #'(!\[.+\..+\]\(file:///C:%5CBaiduSyncdisk%5Cassets(%5C.+){1,}\.\w+)(\))'
    match1=search_str_url_4_file_vid(str_url)
    #timestamps file
    file_list=os.listdir(os.getcwd())
    for file in file_list:
        if file.endswith(".md") or file.endswith(".txt"):
            if file.find("timestamps")!=-1:
                key_word="timestamps"
                list_time_head_textshort_text=get_list_time_head_textshort_text_4_file(file,key_word)

                list_time_head_textshort_text_to_vid_timeline_md(list_time_head_textshort_text,file,match1)


def convert_subtitle_chatgpt_summary_to_markdown_vid_timeline(str_url):

    #str_url=r'![009_area-and-slope.mp4](file:///C:%5CBaiduSyncdisk%5Cassets%5CO%5CO1%5CO17%5CO172%5CCalculus%203Blue1Brown%5Cassets%5Cbvids%5C009_area-and-slope.mp4)'

    match1=search_str_url_4_file_vid(str_url)
    cwd=os.getcwd()
    file_list=os.listdir(cwd)

    create_output_directory()


    for file in file_list:
        if file.endswith(".md"):
            if file.find("summary_base_on_chatgpt")!=-1:
                key_word="summary_base_on_chatgpt"
                list_time_head_textshort_text=get_list_time_head_textshort_text_4_file(file,key_word)
                list_time_head_textshort_text_to_vid_timeline_md(list_time_head_textshort_text,file,match1)

def merge_list_time_head_textshort_text(list_time_text,list_time_head_textshort):
    print("list_time_head_textshort is :")
    print(list_time_head_textshort)
    print("list_time_text is :")
    print(list_time_text)


    for i in range(len(list_time_head_textshort)):
        #print(list_time_head_textshort[i][0])
        for j in range(len(list_time_text)):
            if list_time_head_textshort[i][0]==list_time_text[j][0]:

                time_text=list_time_text.pop(j)
                print(time_text)
                list_time_head_textshort[i][3]=time_text[3]
                #list_time_head_textshort.append([list_time_head_textshort[i][0],list_time_head_textshort[i][1],list_time_head_textshort[i][2],time_text[3]])
                break
    print("first merge list_time_head_textshort_text is :")
    print(list_time_head_textshort)
    list_time_head_textshort_text=list_time_head_textshort
    if len(list_time_text)>0:
        #print("remain:",list_time_text)

        list_pop=[]
        for i in range(len(list_time_text)):
            for j in range(len(list_time_head_textshort_text)):
                time_text=int(list_time_text[i][0])
                time_shorttext=int(list_time_head_textshort_text[j][0])
                if j!=len(list_time_head_textshort_text)-1:
                    time_shorttext_next=int(list_time_head_textshort_text[j+1][0])

                    if time_text>time_shorttext and time_text<time_shorttext_next:

                        list_time_head_textshort_text.insert(j+1,[list_time_text[i][0],None,None,list_time_text[i][3]])
                        list_pop.append(list_time_text[i])
                        break
                else:
                    if time_text>time_shorttext:
                        list_time_head_textshort_text.append([list_time_text[i][0],None,None,list_time_text[i][3]])
                        list_pop.append(list_time_text[i])
                        break
        for elment in list_pop:
            index=list_time_text.index(elment)
            list_time_text.pop(index)
    if len(list_time_text)>0:
        print("remain:",list_time_text)

    return list_time_head_textshort_text
def convert_subtitle_and_summary_to_markdown_vid_timeline(str_url):

    #str_url=r'![009_area-and-slope.mp4](file:///C:%5CBaiduSyncdisk%5Cassets%5CO%5CO1%5CO17%5CO172%5CCalculus%203Blue1Brown%5Cassets%5Cbvids%5C009_area-and-slope.mp4)'

    match1=search_str_url_4_file_vid(str_url)
    cwd=os.getcwd()
    file_list=os.listdir(cwd)

    create_output_directory()

    for file in file_list:
        if file.endswith(".md"):
            if file.find("subtitle")!=-1:
                key_word="subtitle"
                list_time_text=get_list_time_head_textshort_text_4_file(file,key_word)
                #list_time_head_textshort_text_to_vid_timeline_md(list_time_head_textshort_text,file,match1)

            if file.find("summary_base_on_chatgpt")!=-1:
                key_word="summary_base_on_chatgpt"
                list_time_head_textshort=get_list_time_head_textshort_text_4_file(file,key_word)
                #list_time_head_textshort_text_to_vid_timeline_md(list_time_head_textshort_text,file,match1)


    list_time_head_textshort_text=merge_list_time_head_textshort_text(list_time_text,list_time_head_textshort)
    print("final is:")
    print(list_time_head_textshort_text)
    list_time_head_textshort_text_to_vid_timeline_md(list_time_head_textshort_text,file,match1)








def compare_md_files(dir1, dir2):
    """
    比较两个目录下同名的md文件，并输出两个文件的差异。

    Args:
        dir1 (str): 第一个目录路径。
        dir2 (str): 第二个目录路径。

    Returns:
        None

    Raises:
        FileNotFoundError: 如果任意一个目录不存在，则抛出异常。

    """
    if not os.path.exists(dir1):
        raise FileNotFoundError(f"{dir1} not found!")
    if not os.path.exists(dir2):
        raise FileNotFoundError(f"{dir2} not found!")

    md_files1 = [f for f in os.listdir(dir1) if f.endswith('.md')]
    md_files2 = [f for f in os.listdir(dir2) if f.endswith('.md')]

    common_files = set(md_files1).intersection(md_files2)

    for f in common_files:
        file1_path = os.path.join(dir1, f)
        file2_path = os.path.join(dir2, f)

        with open(file1_path, 'r', encoding='utf-8') as f1, open(file2_path, 'r', encoding='utf-8') as f2:
            diff = difflib.unified_diff(f1.readlines(), f2.readlines(
            ), lineterm='', fromfile=file1_path, tofile=file2_path)

            # 输出不同之处
            print(f"--- {file1_path}\n")
            print(f"+++ {file2_path}\n")
            print(''.join(diff))


def process_md_files_filename_2_head():
    md_files = [f for f in os.listdir() if f.endswith('.md')]
    for file_name in md_files:
        with open(file_name, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        new_lines = []
        if 'CHAPTER' in file_name:
            new_lines.append('## ' + file_name[4:-3] + lines[0])
        else:
            new_lines.append('### ' + file_name[4:-3] + lines[0])
        new_lines.extend(lines[1:])
        with open(file_name, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)


def zhihu_book_process():
    path = os.getcwd()
    back_up_dir_tree(path)
    #rename_files_end(path, '.md', '.md', 2, 2)
    base_on_mulu_markdown_rename_files()
    search_list = ["- created: 2023", "- source: https://www.zhihu.com"]
    remove_line(path, search_list)


def rename_files_and_dirs_sensor_fusion(path):
    for root, dirs, files in os.walk(path):
        for name in files + dirs:
            # # 如果文件或目录名称包含空格，则用下划线替换
            # if ' ' in name:
            #     new_name = name.replace(' ', '_')
            #     os.rename(os.path.join(root, name), os.path.join(root, new_name))
            #     name = new_name

            # 如果文件或目录名称以数字开头，则进行重新编号
            if not (name[:3].isdigit()):
                if name[:2].isdigit():
                    prefix = name[:2]
                    new_prefix = prefix.zfill(3)  # 将前缀转换为三位数
                    if name[2] == " ":
                        new_name = new_prefix+"_"+name[3:]
                    elif name[2] == "_":
                        new_name = new_prefix+name[2:]
                    else:
                        new_name = new_prefix+"_"+name[2:]

                    os.rename(os.path.join(root, name),
                              os.path.join(root, new_name))


def test():
    path = os.getcwd()
    # back_up_dir_tree(path)
    # back_up_dir(path)
    # test_text_replace(1677211210)
    # rename_files_end(path, '.md', '.md', 33, 33)
    # base_on_mulu_markdown_rename_files()
    # search_list = ["- created: 2023", "- source: https://www.zhihu.com"]
    # remove_line(path, search_list)
    # compare_md_files("mds", "mds_2023-02-26-22-12-57")
    # process_md_files_filename_2_head()
    rename_files_and_dirs_sensor_fusion(path)


def main():
    # create a parser object
    parser = argparse.ArgumentParser()

    # add arguments for each function
    parser.add_argument('-mdx', '--mdx2md',
                        action='store_true', help='call mdx2md')
    parser.add_argument('-rfe', '--remove_filesname_end',
                        action='store_true', help='call remove_filesname_end')
    parser.add_argument('-ds', '--rename_files_and_dirs_sensor_fusion',
                        action='store_true', help='call rename_files_and_dirs_sensor_fusion')
    parser.add_argument('-tt', '--timestamps_3blue1brown_2_timeline',
                    action='store_true', help='call timestamps_3blue1brown_2_timeline')
    parser.add_argument('-cti', '--copy_timestamps_and_index_2_root',
                action='store_true', help='call copy_timestamps_and_index_2_root')
    parser.add_argument('-csm', '--convert_subtitle_chatgpt_summary_to_markdown_vid_timeline',
                action='store_true', help='call convert_subtitle_chatgpt_summary_to_markdown_vid_timeline')
    parser.add_argument('-cssm', '--convert_subtitle_and_summary_to_markdown_vid_timeline',
                action='store_true', help='call convert_subtitle_and_summary_to_markdown_vid_timeline')
    parser.add_argument('-t', '--timestamp', type=str, default=r'1676880280',
                        help='input timestamp to pass to the function')
    parser.add_argument('-u', '--str_url', type=str, default=r'test',
                    help='input str_url to pass to the function')
    # parse the command-line arguments
    args = parser.parse_args()

    # call the appropriate function based on the arguments
    if args.remove_filesname_end:
        rename_files_end_test1()
    elif args.rename_files_and_dirs_sensor_fusion:
        rename_files_and_dirs_sensor_fusion()
    elif args.copy_timestamps_and_index_2_root:
        copy_timestamps_and_index_2_root()
    elif args.convert_subtitle_chatgpt_summary_to_markdown_vid_timeline:
        convert_subtitle_chatgpt_summary_to_markdown_vid_timeline(args.str_url)
    elif args.convert_subtitle_and_summary_to_markdown_vid_timeline:
        convert_subtitle_and_summary_to_markdown_vid_timeline(args.str_url)
    elif args.mdx2md:
        mdx2md(args.timestamp)
    elif args.timestamps_3blue1brown_2_timeline:
        timestamps_3blue1brown_2_timeline(args.str_url)
    else:
        print("Invalid argument")


if __name__ == "__main__":
    main()
