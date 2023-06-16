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
import aspose.words as aw
import urllib.parse


def remove_filesname_end(path, old_extension, new_extension, file_remove_length=0, dir_remove_length=0):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(old_extension):
                os.replace(os.path.join(root, file),
                           os.path.join(root, file[:-(len(old_extension)+file_remove_length)]+new_extension))
        for dir in dirs:
            if dir_remove_length > 0:
                os.replace(os.path.join(root, dir), os.path.join(
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
        os.replace(old_path, new_path)

        # 输出修改后的文件名
        print("文件名从 {} 变为 {}".format(filename, new_filename))


def rename_files(path, replace_list):
    for root, dirs, files in os.walk(path):
        for file in files:
            file_old = file
            for replace_str in replace_list:
                if file.find(replace_str[0]) != -1:
                    file = file.replace(replace_str[0], replace_str[1])
            os.replace(os.path.join(root, file_old),
                       os.path.join(root, file))
        for dir in dirs:
            dir_old = dir
            for replace_str in replace_list:
                if dir.find(replace_str[0]) != -1:
                    dir = dir.replace(replace_str[0], replace_str[1])
            os.replace(os.path.join(root, dir_old),
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


# def num2str_title(num):
#     if num < 10:
#         return '00'+str(num)
#     elif num < 100:
#         return '0'+str(num)
#     else:
#         return str(num)


def search_file(path):
    with (open("目录.md", 'r', encoding='UTF-8')) as f:
        lines = f.readlines()
        for root, dirs, files in os.walk(path):
            counter = 0
            for line in lines:
                if line[:-1]+'.md' in files:
                    counter = counter+1
                    os.replace(os.path.join(
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



def tianjiaxiahuaxian():
    for root, dirs, files in os.walk("."):
        for i in range(1, 38):
            for file in files:
                if file[:3] == num2str_title(i):
                    os.replace(os.path.join(root, file),
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


# def rename_files_base_on_index_markdown(path=None):
#     counter = 0
#     if path is None:
#         path = os.getcwd()
#     with open(os.path.join(path,"000_index.md"), 'r', encoding='UTF-8') as f:
#         lines = f.readlines()
#     files = os.listdir(path)
#     for i in range(len(lines)):
#         line =lines[i]
#         line = line.replace("%", "_")
#     #for line in lines:
#         if line[-1]=="\n":
#             note_name=line[:-1]+'.md'
#         else:
#             note_name=line+'.md'
#         if note_name in files:
#             counter = i+1
#             # print(line[:-1]+'.md')
#             os.replace(os.path.join(path, note_name),
#                         os.path.join(path, num2str_title(counter)+"_"+note_name))
#         else:
#             raise Exception(note_name+" not in the files list")


def num2str_title(num):
    return str(num).zfill(3)

def rename_files_base_on_index_markdown(path=None):
    counter = 0
    if path is None:
        path = os.getcwd()
    with open(os.path.join(path, "000_index.md"), 'r', encoding='UTF-8') as f:
        lines = f.readlines()
    files = os.listdir(path)
    for i, line in enumerate(lines):
        line = line.strip().replace("%", "_")
        note_name = line + '.md'
        if note_name in files:
            counter += 1
            os.replace(os.path.join(path, note_name),
                        os.path.join(path, num2str_title(counter) + "_" + note_name))
        else:
            print(files)
            raise FileNotFoundError(f"{note_name} not in the files list")


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




def delete_non_example_md_files():
    for file_path in glob.glob('*.md'):
        if file_path != 'example.md' and file_path.endswith('.md'):
            os.remove(file_path)


def add_timestamp_to_filenames():
    current_dir = os.getcwd()
    timestamp = int(time.time())
    for filename in os.listdir(current_dir):
        if os.path.isfile(os.path.join(current_dir, filename)) and not filename.endswith(".py"):
            filename_without_ext, ext = os.path.splitext(filename)
            new_filename = f"{filename_without_ext}_{timestamp}{ext}"
            os.replace(os.path.join(current_dir, filename),
                       os.path.join(current_dir, new_filename))


def text_replace(root_dir: str, replace_list: list):
    assets_root_path,assets_root_dir=get_assets_root_path()
    output_dir = create_output_directory(assets_root_path)
    for filename_with_ext in os.listdir(root_dir):
        if filename_with_ext.endswith('.md'):
            src_path = os.path.join(root_dir, filename_with_ext)
            dest_path = os.path.join(output_dir, filename_with_ext)

            with open(src_path, 'r', encoding='UTF-8') as f_src, open(dest_path, 'w', encoding='UTF-8') as f_dest:
                for line in f_src:
                    for replace_item in replace_list:
                        line = line.replace(replace_item[0], replace_item[1])
                    f_dest.write(line)



def mdx2md(timestamp: int = 1676880280):
    assets_root_path,assets_root_dir=get_assets_root_path()
    output_dir = create_output_directory(assets_root_path)
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
                                 [r"<PiCreature\n{0,}\s{0,}(.+)\n{0,}\s{0,}(.+)\n{0,}\s{0,}/>", r"\1\n\2\n"],
                #[r"show=\"video\"\n", r""],
                #  [r"<!--", r""],
                #  [r"-->", r""],
                                 [r"<Question", r"---"],
                                 [r"<FreeResponse>", r"---"],
                [r"</FreeResponse>", r"---"],
                [r"</Question>", r"---"],
                [r'''<Figure[\n ]{1,}image="(.+)(\.svg|\.png|\.jpg)"[\w ._="'\n_%]{0,}/>''',
                                     r'![](\1_'+str(timestamp)+r'\2)'],
                [r'<Accordion\stitle=".+">\n', r''],
                [r'</Accordion>\n', r''],
                #[r'emotion="\w+"[ \t]+\n', r''],
                #[r'flip=\{(true|false)\}\n', r''],
                #[r'(?s)<Question .+?</Question>', r'tttttttttttttttttttt'],
                [r'answer=\{(\d)\}[ \n\t]{0,}>',
                                     r'\n<details><summary>answer</summary><p>Choice= \1</p></details>\n\n- **Explanation**'],
                #[r'''<Question[\n \t]{0,}question="(.+)"[\n \t]{0,}choice1="(.+)"[\n \t]{0,}choice2="(.+)"[\n \t]{0,}choice3="(.+)"[\n \t]{0,}choice4="(.+)"[\n \t]answer=\{(\d)\}[\n \t]{0,}>''',r'- **Question**\n\t\1']
                [r'[ \t]{0,}question="(.+)"',
                                     r'- **Question**\n\t\1'],
                [r'[ \t]{0,}choice1="(.+)"',
                                     r'    - **Choice 1=** \1'],
                [r'[ \t]{0,}choice2="(.+)"',
                                     r'    - **Choice 2=** \1'],
                [r'[ \t]{0,}choice3="(.+)"', r'    - **Choice 3=** \1'],
                [r'[ \t]{0,}choice4="(.+)"', r'    - **Choice 4=** \1'],
                #[r'video=".+\.mp4"', r''],
                #[r'show="video"', r''],
                [r'([ \t]{0,}\n){3,}', r'\1\1'],
                #['/>', r''],
            ]

            for i in range(len(replace_list_regex)):
                pattern = replace_list_regex[i][0]
                replacement = replace_list_regex[i][1]
                # pattern2=r'''<Question[\n \t]{0,}question="(.+)"([\n \t]{0,}choice\d="(.+)"){1,}[\n \t]{0,}answer=\{(\d)\}[\n \t]{0,}>'''
                # match=re.search(pattern2, content)
                # if match:
                #     print(len(match.groups()))
                #     # print(match.group(0))
                #     # print(match.group(1))
                #     # print(match.group(2))
                #     print(match.group(3))
                #     #print(match.group(4))

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
    r"![001_Derivatives of multivariable functions.mp4](file:///C%3A%5CBaiduSyncdisk%5Cassets%5CO%5CO1%5CO17%5CO172%5CMultivaribale_calculus_Khan_Academy%5Cassets%5Cbvids%5Cmc_1683793602%5C002%5C001%5C001_Derivatives%20of%20multivariable%20functions.mp4)"
    url_pattern_4_file_vid = r'(!\[.+\..+\]\(file:///C:%5CBaiduSyncdisk%5Cassets(%5C.+){1,}\.\w+)(\))'
    url_pattern_4_file_vid2 = r'(!\[.+\..+\]\(file:///C%3A%5CBaiduSyncdisk%5Cassets(%5C.+){1,}\.\w+)(\))'
    match1 = re.search(url_pattern_4_file_vid, str_url)
    if not match1:
        match1 = re.search(url_pattern_4_file_vid2, str_url)
        if not match1:
            raise Exception('No match found')
    return match1


def convert_min_sec_to_seconds(time_str):
    time_line_pattern_str = r'\((\d{1,2}:\d{1,2})-(\d{1,2}:\d{1,2})\)[ ]{1,}'
    time_stamp_pattern_str = r'(\d{1,2}):(\d{1,2})'
    match = re.search(time_line_pattern_str, time_str)
    if match:
        time_line_start = match.group(1)
        time_line_end = match.group(2)
        time_line_start_seconds = int(time_line_start.split(
            ':')[0])*60+int(time_line_start.split(':')[1])
        return time_line_start_seconds
    else:
        match = re.search(time_stamp_pattern_str, time_str)
        if match:
            time_seconds = int(match.group(1)) * 60 + int(match.group(2))
            return time_seconds
        else:
            return None


def get_father_path(path):
    return os.path.dirname(path)


def create_output_directory(root=None):
    if root is None:
        root = os.getcwd()

    output_dir = os.path.join(root, 'output')

    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    print("Created output directory %s" % output_dir)
    return output_dir


def create_new_file_name(file):
    if not file.endswith('.md'):
        filename_without_ext = os.path.splitext(file)[0]
        new_file_name = filename_without_ext+'.md'
    else:
        new_file_name = file
    print(new_file_name)
    return new_file_name

# 0


def list_time_head_textshort_text_to_vid_timeline_md(timeline_data, file, match):
    # print(timeline_data)
    assets_root_path,assets_root_dir=get_assets_root_path()
    output_dir = create_output_directory(assets_root_path)
    new_file_name = create_new_file_name(file)
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


def get_list_time_head_textshort_text_4_file(file, key_word):
    print("start to generate time line for video and head text:")
    find1 = r'Part \d:\nTitle: ([\w ]+)\nTimestamp: (\(\d{1,2}:\d{1,2}\))\nSummary: ([\w , .]+)'
    replace1 = r'- $1 $2 $3'
    find2 = r'(\(\d{1,2}:\d{1,2}\)) ([\w ]+)\n'
    replace2 = r'- $2 $1 '
    number_list_bullet_pattern_str = r'((\d{1,2}\.)|-)[ ]{1,}'
    head_pattern_str = r'(([\w:-]+ ){1,})'
    time_line_pattern_str = r'\((\d{1,2}:\d{1,2})-{0,1}(\d{1,2}:\d{1,2}){0,1}\)[ ]{1,}'
    time_stamp_pattern_str = r'\((\d{1,2}):(\d{1,2})\)'
    text_pattern_str = r'(.+)\n{0,1}'
    #number_list_head_time_text_pattern_str=r'((\d{1,2}\.)|(-))[ ]{1,}([\w, ]+):[ ]\((\d{1,2}:\d{1,2})\)[ ](.+)'
    # number_list_head_time_text_pattern_str=number_list_bullet_pattern_str+head_pattern_str+time_stamp_pattern_str+text_pattern_str
    number_list_head_time_text_pattern_str = r'((\d{1,2}\.)|-)[ ]{1,}(.+) \((\d{1,2}):(\d{1,2})\) (.+)'
    number_list_head_time_pattern_str = r'(\d{1,2}):(\d{1,2})\s+(.+)'

    time_text_pattern_str = r'\((\d{1,2}):(\d{1,2})\)[ ]{0,}([^\n]+)[\n]{0,}'

    pattern_dict = dict()
    pattern_dict["timestamps"] = number_list_head_time_pattern_str
    pattern_dict["summary_base_on_chatgpt"] = number_list_head_time_text_pattern_str
    pattern_dict["subtitle"] = time_text_pattern_str
    list_time_head_textshort_text = []
    with open(os.path.join(os.getcwd(), file), 'r', encoding='UTF-8') as f:
        lines = f.readlines()

    for line in lines:
        time_line_start_seconds = convert_min_sec_to_seconds(line)
        if time_line_start_seconds != None:
            if key_word in pattern_dict:
                pattern_str = pattern_dict[key_word]
                match = re.search(pattern_str, line)
                if match:
                    if key_word == "timestamps":
                        list_time_head_textshort_text.append(
                            [time_line_start_seconds, match.group(3), None, None])
                    elif key_word == "summary_base_on_chatgpt":
                        # for i in range(len(match.groups())):
                        #     print(i,match.group(i))
                        list_time_head_textshort_text.append(
                            [time_line_start_seconds, match.group(3), match.group(6), None])
                    elif key_word == "subtitle":
                        list_time_head_textshort_text.append(
                            [time_line_start_seconds, None, None, match.group(3)])
                else:
                    print("no match for line:", line)
                    print(key_word)
    # print("List of time, heading, short text, text:")
    # print(list_time_head_textshort_text)
    return list_time_head_textshort_text


def timestamps_3blue1brown_2_timeline(str_url):
    # process url
    # str_url=r'![007_limits.mp4](file:///C:%5CBaiduSyncdisk%5Cassets%5CO%5CO1%5CO17%5CO172%5CCalculus%203Blue1Brown%5Cassets%5Cbvids%5C007_limits.mp4)'
    # '(!\[.+\..+\]\(file:///C:%5CBaiduSyncdisk%5Cassets(%5C.+){1,}\.\w+)(\))'
    match1 = search_str_url_4_file_vid(str_url)
    # timestamps file
    file_list = os.listdir(os.getcwd())
    for file in file_list:
        if file.endswith(".md") or file.endswith(".txt"):
            if file.find("timestamps") != -1:
                key_word = "timestamps"
                list_time_head_textshort_text = get_list_time_head_textshort_text_4_file(
                    file, key_word)

                list_time_head_textshort_text_to_vid_timeline_md(
                    list_time_head_textshort_text, file, match1)


def convert_subtitle_chatgpt_summary_to_markdown_vid_timeline(str_url):

    # str_url=r'![009_area-and-slope.mp4](file:///C:%5CBaiduSyncdisk%5Cassets%5CO%5CO1%5CO17%5CO172%5CCalculus%203Blue1Brown%5Cassets%5Cbvids%5C009_area-and-slope.mp4)'

    match1 = search_str_url_4_file_vid(str_url)
    cwd = os.getcwd()
    file_list = os.listdir(cwd)
    assets_root_path,assets_root_dir=get_assets_root_path()
    create_output_directory(assets_root_path)

    for file in file_list:
        if file.endswith(".md"):
            if file.find("summary_base_on_chatgpt") != -1:
                key_word = "summary_base_on_chatgpt"
                list_time_head_textshort_text = get_list_time_head_textshort_text_4_file(
                    file, key_word)
                list_time_head_textshort_text_to_vid_timeline_md(
                    list_time_head_textshort_text, file, match1)


def merge_list_time_head_textshort_text(list_time_text, list_time_head_textshort):
    # print("list_time_head_textshort is :")
    # print(list_time_head_textshort)
    # print("list_time_text is :")
    # print(list_time_text)

    for i in range(len(list_time_head_textshort)):
        # print(list_time_head_textshort[i][0])
        for j in range(len(list_time_text)):
            if list_time_head_textshort[i][0] == list_time_text[j][0]:

                time_text = list_time_text.pop(j)
                print(time_text)
                list_time_head_textshort[i][3] = time_text[3]
                # list_time_head_textshort.append([list_time_head_textshort[i][0],list_time_head_textshort[i][1],list_time_head_textshort[i][2],time_text[3]])
                break
    # print("first merge list_time_head_textshort_text is :")
    # print(list_time_head_textshort)
    list_time_head_textshort_text = list_time_head_textshort
    if len(list_time_text) > 0:
        # print("remain:",list_time_text)

        list_pop = []
        for i in range(len(list_time_text)):
            for j in range(len(list_time_head_textshort_text)):
                time_text = int(list_time_text[i][0])
                time_shorttext = int(list_time_head_textshort_text[j][0])
                if j != len(list_time_head_textshort_text)-1:
                    time_shorttext_next = int(
                        list_time_head_textshort_text[j+1][0])

                    if time_text > time_shorttext and time_text < time_shorttext_next:

                        list_time_head_textshort_text.insert(
                            j+1, [list_time_text[i][0], None, None, list_time_text[i][3]])
                        list_pop.append(list_time_text[i])
                        break
                else:
                    if time_text > time_shorttext:
                        list_time_head_textshort_text.append(
                            [list_time_text[i][0], None, None, list_time_text[i][3]])
                        list_pop.append(list_time_text[i])
                        break
        for elment in list_pop:
            index = list_time_text.index(elment)
            list_time_text.pop(index)
    if len(list_time_text) > 0:
        print("remain:", list_time_text)

    return list_time_head_textshort_text


def convert_subtitle_and_summary_to_markdown_vid_timeline(str_url):

    # str_url=r'![009_area-and-slope.mp4](file:///C:%5CBaiduSyncdisk%5Cassets%5CO%5CO1%5CO17%5CO172%5CCalculus%203Blue1Brown%5Cassets%5Cbvids%5C009_area-and-slope.mp4)'

    match1 = search_str_url_4_file_vid(str_url)
    cwd = os.getcwd()
    file_list = os.listdir(cwd)
    assets_root_path,assets_root_dir=get_assets_root_path()
    output_dir = create_output_directory(assets_root_path)

    for file in file_list:
        if file.endswith(".md"):
            if file.find("subtitle") != -1:
                key_word = "subtitle"
                list_time_text = get_list_time_head_textshort_text_4_file(
                    file, key_word)
                # list_time_head_textshort_text_to_vid_timeline_md(list_time_head_textshort_text,file,match1)

            if file.find("summary_base_on_chatgpt") != -1:
                cwd_floder_name = os.path.basename(cwd)
                file_summary = file
                key_word = "summary_base_on_chatgpt"
                list_time_head_textshort = get_list_time_head_textshort_text_4_file(
                    file, key_word)
                # list_time_head_textshort_text_to_vid_timeline_md(list_time_head_textshort_text,file,match1)

    list_time_head_textshort_text = merge_list_time_head_textshort_text(
        list_time_text, list_time_head_textshort)
    print("final is:")
    print(list_time_head_textshort_text)
    list_time_head_textshort_text_to_vid_timeline_md(
        list_time_head_textshort_text, file_summary, match1)
    vid_link_md_2_html(output_dir)
    return output_dir, file_summary


def get_current_timestamp():
    timestamp = int(time.time())
    print(timestamp)
    return timestamp


def add_timestamp_to_filenames():
    current_dir = os.getcwd()
    timestamp = int(time.time())
    print("add_timestamp is : ", timestamp)
    for filename in os.listdir(current_dir):
        if os.path.isfile(os.path.join(current_dir, filename)) and not filename.endswith(".py"):
            filename_without_ext, ext = os.path.splitext(filename)
            new_filename = f"{filename_without_ext}_{timestamp}{ext}"
            os.replace(os.path.join(current_dir, filename),
                       os.path.join(current_dir, new_filename))


def create_directory_assets_imgs():
    dirs = [
        "assets/imgs",
        "assets/vids"
    ]

    for directory in dirs:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"Created directory: {directory}")
        else:
            print(f"Directory already exists: {directory}")


def create_directory_assets_concept_structure():
    dirs = [
        "assets",
        "assets/imgs",
        "assets/lectures",
        "assets/papers",
        "lectures",
        "papers",
    ]

    for directory in dirs:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"Created directory: {directory}")
        else:
            print(f"Directory already exists: {directory}")


def open_folder_in_windows(folder_path):
    """Open a folder in Windows File Explorer based on the folder path.

    Args:
    folder_path (str): The folder path to open.

    Returns:
    None
    """
    if os.path.exists(folder_path):
        os.startfile(folder_path)
    else:
        print(f"Folder path {folder_path} does not exist.")


def open_b_assets_folder(cwd=None):
    if cwd is None:
        cwd = os.getcwd()
    print(cwd)
    if cwd.find("OneDrive") == -1:
        raise Exception("This script is only for use with OneDrive.")
    assets_path_front = "C:/BaiduSyncdisk/assets"

    # Split the path after 'KG' and replace backslashes with forward slashes
    kg_path_back = cwd.split("\\KG")[1].replace("\\", "/")

    # Remove the leading forward slash from kg_path_back
    kg_path_back = kg_path_back.lstrip("/")

    assets_path = os.path.join(assets_path_front, kg_path_back)
    if assets_path.find("BaiduSyncdisk") == -1:
        raise Exception("The assets path is not in BaiduSyncdisk.")
    open_folder_in_windows(assets_path)


def rename_files_sensor_fusion(path=None):
    if path == None:
        path = os.getcwd()
    file_list = os.listdir(path)
    for name in file_list:

        if name.endswith(".md"):
            # 如果文件或目录名称以数字开头，则进行重新编号
            if not (name[:3].isdigit()):
                if name[:2].isdigit():
                    prefix = name[:2]
                    new_prefix = prefix.zfill(3)  # 将前缀转换为三位数
                    if name[2] == " ":
                        new_name = new_prefix+"_"+name[3:]
                    elif name[2] == "_":
                        new_name = new_prefix+name[2:]
                    elif name[2] == ".":
                        if name[3] == " ":
                            new_name = new_prefix+"_"+name[4:]
                        else:
                            new_name = new_prefix+"_"+name[3:]
                    else:
                        new_name = new_prefix+"_"+name[2:]
                    try:
                        os.replace(os.path.join(path, name),
                                   os.path.join(path, new_name))
                    except FileExistsError:
                        os.remove(os.path.join(path, new_name))
                        os.replace(os.path.join(path, name),
                                   os.path.join(path, new_name))


def html2md(path=None, output_root="C://Output//", output_folder_name=None):
    if path is None:
        path = os.getcwd()
    timestamp = int(time.time())
    intput_path = path
    input_floder_name = os.path.basename(intput_path)
    #replace_list_regex2=[[r'Part \d{2}-Module \d{2}-Lesson (\d{2})_(.+)',r'0\1_\2'],]
    input_floder_name = re.sub(
        r'Part \d{2}-Module \d{2}-Lesson (\d{2})_(.+)', r'0\1_\2', input_floder_name)
    # Part 01-Module 01-Lesson 01_Welcome to the C++ Developer Nanodegree Program
    input_floder_name = input_floder_name.replace(" ", "_")
    output_path = os.path.join(
        output_root, output_folder_name, input_floder_name)
    os.makedirs(output_path, exist_ok=True)

    listfiles = os.listdir(intput_path)
    mp4_list = [
        filename for filename in listfiles if filename.endswith(".mp4")]
    # print(listfiles)
    for i in range(len(listfiles)):
        filename = listfiles[i]  # get all file list
        if filename.endswith(".html"):
            input_file = os.path.join(intput_path, filename)
            doc = aw.Document(input_file)
            output_file = os.path.join(
                output_path, filename.replace(".html", ".md"))
            # print(output_path)

            doc.save(output_file)

    output_files_list = os.listdir(output_path)
    replace_list_regex = [[r'!\[\]\(.+\.001\.png\)', r''],
                          [r'(!\[\]|!\[.+\])(\(.+)(\.png|\.jpg|\.gif|\.jpeg|\.svg|\.wbem)\)',
                              r'\1\2'+f'_{timestamp}'+r'\3)'],
                          [r'\*\*Evaluation Only\. Created with Aspose\.Words\. Copyright 2003-2023 Aspose Pty Ltd\.\*\*', r''],
                          [r'\*\*Created with an evaluation copy of Aspose.Words. To discover the full versions of our APIs please visit: https://products.aspose.com/words/\*\*', r''],
                          [r'\[udacimak v1.4.1\]\(https://github.com/udacimak/udacimak#readme\)', r''],
                          [r'\[.+\]\(.+\.html\)', r''],
                          [r'\n{3,}', r'\n\n'],
                          [r'`[ ]+`', r'    '],
                          ]
    for i in range(len(output_files_list)):
        filename = output_files_list[i]
        if filename.endswith(".001.png"):
            os.remove(os.path.join(output_path, filename))
            continue
        if filename.endswith(".md"):
            if filename == "index.md":
                os.remove(os.path.join(output_path, filename))
                continue
            with open(os.path.join(output_path, filename), 'r', encoding='UTF-8') as f:
                content = f.read()
            with open(os.path.join(output_path, filename), 'w', encoding='UTF-8') as f:

                for replace_list in replace_list_regex:
                    content = re.sub(replace_list[0], replace_list[1], content)
                # f.write(content)

                lines = content.splitlines()
                for line in lines:
                    if len(line) > 4:
                        for file_mp4 in mp4_list:
                            word_list = line.split(" ")
                            flag = 0
                            flag_out = 0
                            for word in word_list:
                                if file_mp4.find(word) > -1:
                                    flag = flag+1
                                elif file_mp4.find(word) == -1:
                                    flag_out = flag_out+1
                            if flag:
                                if flag_out:
                                    # print(line)
                                    pass
                                else:
                                    path_mp4 = os.path.join(
                                        intput_path, file_mp4)
                                    url_path = urllib.parse.quote(
                                        os.path.abspath(path_mp4))
                                    url = "file:///" + \
                                        url_path.replace("\\", "/")
                                    line = line+"\n\n" + \
                                        f"[{file_mp4}]({url})\n" + \
                                        f"![{file_mp4}]({url})"

                    f.write(line+"\n")
    rename_files_sensor_fusion(output_path)
    output_files_list = os.listdir(output_path)

    output_path_md = output_path
    output_path_img = os.path.join(
        output_root, "imgs", output_folder_name, input_floder_name)

    # Create the output directory and its subdirectory if they don't exist
    try:
        os.makedirs(output_path_img, exist_ok=True)
    except FileNotFoundError as e:
        if e.winerror == 206:
            # Shorten the filename and try again
            output_path_img = output_path_img = os.path.join(
                output_path_md, "imgs")
            os.makedirs(output_path_img, exist_ok=True)

        else:
            # If it's not WinError 206, raise the original error
            raise e
    for i in range(len(output_files_list)):
        filename = output_files_list[i]
        if filename.endswith(".md"):
            try:
                os.replace(os.path.join(output_path, filename),
                           os.path.join(output_path_md, filename))
            except FileExistsError:
                os.remove(os.path.join(output_path_md, filename))
                os.replace(os.path.join(output_path, filename),
                           os.path.join(output_path_md, filename))

        if filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".gif"):
            filename_ext = os.path.splitext(filename)[1]
            filename_without_ext = os.path.splitext(filename)[0]
            filename_img = filename_without_ext+f'_{timestamp}'+filename_ext
            try:
                os.replace(os.path.join(output_path, filename),
                           os.path.join(output_path_img, filename_img))
            except FileExistsError:
                os.remove(os.path.join(output_path_img, filename_img))
                os.replace(os.path.join(output_path, filename),
                           os.path.join(output_path_img, filename_img))
            except FileNotFoundError as e:
                if e.winerror == 3:

                    output_path_img = output_path_img = os.path.join(
                        output_path_md, "imgs")
                    os.makedirs(output_path_img, exist_ok=True)
                    os.replace(os.path.join(output_path, filename),
                               os.path.join(output_path_img, filename_img))
                else:
                    # If it's not WinError 206, raise the original error
                    raise e


def html2md_tree():
    files = [f for f in os.listdir() if os.path.isfile(f)]
    directories = [f for f in os.listdir() if os.path.isdir(f)]
    output_folder_dict = dict()
    for directory in directories:
        search_str = r'Part (\d{2})_(.+)'
        match = re.search(search_str, directory)
        if match:
            output_folder_dict[match.group(
                1)] = '0'+match.group(1)+"_"+match.group(2)
    for directory in directories:
        search_str = r'Part (\d{2})-Module \d{2}-Lesson (\d{2})_(.+)'
        match = re.search(search_str, directory)
        if match:
            output_folder1 = "C:\\Output\\"
            output_folder2 = output_folder_dict[match.group(1)]
            # output_folder=os.path.join(output_folder1,output_folder2)
            input_path = os.path.join(os.getcwd(), directory)
            html2md(input_path, output_folder1, output_folder2)


def vid_link_md_2_html(path=None):
    if path is None:
        path = os.getcwd()
    #print("vid_link_md_2_html input path is %s" % path)
    files = [f for f in os.listdir(path) if os.path.isfile(f)]
    assets_root_path, assets_root_dir = get_assets_root_path(path)
    output_path = create_output_directory(assets_root_path)
    if not os.path.exists(output_path):
        os.makedirs(output_path, exist_ok=True)
    replace_list_regex = [
        [r'(!\[\]|!\[.+\])\((file:///.+(\.mp4|\.mp4#t=.+))\)', r'<video src="\2" controls></video>']]
    for file in files:
        if file.endswith(".md"):
            with open(os.path.join(path, file), "r", encoding="utf-8") as f:
                content = f.read()
                # print(content)
            for replace_list in replace_list_regex:
                content = re.sub(replace_list[0], replace_list[1], content)
            with open(os.path.join(output_path, file), "w", encoding="utf-8") as f:
                f.write(content)


def create_file_subtitle_summary_base_on_chatgpt_md(path=None):
    # Create a file named subtitle.md and summary_base_on_chatgpt.md
    print("create_file_subtitle_summary_base_on_chatgpt_md")
    if path is None:
        path = os.getcwd()
    time_stamp = get_current_timestamp()
    with open(os.path.join(path, "subtitle_"+str(time_stamp)+".md"), "w") as f:
        pass
    with open(os.path.join(path, "summary_base_on_chatgpt_"+str(time_stamp)+".md"), "w") as f:
        pass
# Function to get the parent directory


def get_parent_dir(directory):
    return os.path.dirname(directory)
    # Function to create a file


def create_file(path, content=""):
    with open(path, 'w') as f:
        f.write(content)

def get_assets_root_path(current_dir=None):
    if current_dir is None:
        current_dir = os.getcwd()
    while True:
        if 'assets' in os.listdir(current_dir):
            return current_dir,os.path.basename(current_dir)
        else:
            current_dir = get_parent_dir(current_dir)
            if current_dir == '':
                raise Exception('assets folder not found')

def get_note_assets_path(folder_list, current_dir):
    folder_list.append(os.path.basename(current_dir))
    current_dir = get_parent_dir(current_dir)
    while True:

        if 'assets' in os.listdir(current_dir):
            folder_list.reverse()
            if folder_list != []:
                assets_dir_path = os.path.join(current_dir, 'assets')
                for folder_name in folder_list:
                    assets_dir_path = os.path.join(
                        assets_dir_path, folder_name)
                    # print(assets_dir_path)
                    # if os.path.isdir(assets_dir_path):
                    if not os.path.exists(assets_dir_path):
                        os.makedirs(assets_dir_path)
                return assets_dir_path
                # else:
                #     raise Exception('not a directory ',assets_dir_path)
            else:
                raise Exception("No folder name found")

            break
        else:
            folder_list.append(os.path.basename(current_dir))
            current_dir = get_parent_dir(current_dir)


def init_note():
    import os
    import pyperclip
    import time

    # Get content from clipboard
    content = pyperclip.paste()

    # Get current directory
    current_dir = os.getcwd()

    # Check for existing serial numbers (first three digits of filenames)
    serial_numbers = [f[:3] for f in os.listdir(current_dir) if os.path.isfile(
        os.path.join(current_dir, f)) and f[:3].isdigit()]

    # Generate filename
    if serial_numbers:
        max_serial_number = max(serial_numbers)

        note_file = str(int(max_serial_number) + 1).zfill(3)+"_"+content+".md"

    else:
        note_file = "001"+"_"+content+".md"

    # Add the filename to the current_dir
    note_path = os.path.join(current_dir, note_file)
    if not os.path.exists(note_path):
        create_file(note_path)
    folder_list = []
    folder_list.append(note_file[:-3])
    #folder_list.append(os.path.basename(current_dir))

    assets_dir_path = get_note_assets_path(folder_list, current_dir)

    create_file_subtitle_summary_base_on_chatgpt_md(assets_dir_path)


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

def zhi_book_markdown_process(num=0):
    if num==0:
        files=os.listdir()

        for file in files:
            if file.endswith(".md"):
                with open(file,'r',encoding='utf-8') as f:
                    content=f.read()

def get_md_files(directory='.'):
    """Return a sorted list of markdown filenames in a given directory."""
    files = [f for f in os.listdir(directory) if f.endswith('.md')]
    # Extract numeric prefix and sort based on it
    files.sort(key=lambda x: int(re.match(r'(\d{3})_', x).group(1)) if re.match(r'(\d{3})_', x) else float('inf'))
    return files
def check_md_files(files):


    # Check if files are in expected order
    for i, filename in enumerate(files):
        expected_prefix = f"{i:03d}_"
        if not filename.startswith(expected_prefix):
            print(f"Warning: {filename} does not match expected prefix {expected_prefix}")

def merge_files(filenames, output_filename):
    """Merge the content of a list of files and write to a new file."""
    with open(output_filename, 'w', encoding='utf-8') as outfile:
        for fname in filenames:
            try:
                with open(fname, 'r', encoding='utf-8') as infile:
                    content = infile.read()
                    outfile.write(content)
                    outfile.write('\n')  # add blank lines between files
            except IOError:
                print(f'Error opening file {fname}, skipping.')

def merge_all_md_files_into_one():
    """Merge all markdown files in the current directory into one file."""
    root_path, root_dir = get_assets_root_path()
    output_file = os.path.join(root_path,root_dir+".md")
    md_files = get_md_files()
    check_md_files(md_files)
    merge_files(md_files, output_file)


def Merge_all_md_files_into_one_file_base_on_num_index():
    files = [f for f in os.listdir() if f.endswith('.md')]
    files.sort()
    print(files)
    root_path,root_dir=get_assets_root_path()
    with open(os.path.join(root_path,root_dir+".md"), 'w', encoding='utf-8') as f:
        for file in files:
            with open(file, 'r', encoding='utf-8') as f2:
                content = f2.read()
                f.write(content)
                f.write('\n\n')

def test(num=0):
    operations = {
        1: perform_regex_replacement_on_index_file,

        2: perform_regex_replacement_on_zhi_book_mds_name,
        3: rename_files_base_on_index_markdown,
        4: prepend_filename_as_header_if_chapter_present,
        5: lower_header_level_in_md_files,

        6: remove_md_copy_code,
        7: perform_regex_replacement_on_zhi_mds,
        8: convert_zhi_footnote_to_obsidian,
        10: merge_all_md_files_into_one,
    }

    if num in operations:
        operations[num]()
    elif num == 0:
        print("Available operations:")
        for num, func in operations.items():
            print(f"{num}: {func.__name__}")
    else:
        raise ValueError("Invalid operation number. Please choose a number between 0 and 4.")

def html2md2():
    import html2markdown
    files = [f for f in os.listdir() if os.path.isfile(f)]
    for file in files:
        if file.endswith(".html"):
            with open(file, 'r', encoding='utf-8') as f:
                html_string = f.read()
            markdown_text = html2markdown.convert(html_string)
            with open(file[:-4] + '.md', 'w', encoding='utf-8') as f:
                f.write(markdown_text)





def get_b_assets_path(path=None):
    if path is None:
        path = os.getcwd()

    if path.find("OneDrive") == -1 or path.find("KG") == -1:
        raise Exception("This script is only for use with OneDrive/KG.")
    # if path.find("assets") ==-1:
    #     raise Exception("current path is not an assets path.")
    # reg_search=[r'(.+\\OneDrive\\KG\\)(.+)']
    reg_search = [
        [r'.+\\OneDrive\\KG\\(.+)', r'C:\\BaiduSyncdisk\\assets\\\1']]
    test2 = r'C:\BaiduSyncdisk\assets\O\O1\O17\O172\Multivaribale_calculus_Khan_Academy\assets\bvids\mc_1683793602\001_\005_'
    test = r'C:\Users\shade\OneDrive\KG\O\O1\O17\O172\Multivaribale_calculus_Khan_Academy\assets\001_Thinking about multivariable functions\005_Transformations\003_Transformations, part 3'
    # print(path)
    match1 = re.search(reg_search[0][0], path)
    if match1:
        path_b_assets = re.sub(reg_search[0][0], reg_search[0][1], path)
        print(path_b_assets)
        return path_b_assets


def get_bvids_path(current_dir=None, key_word="mc_1683793602"):
    if current_dir is None:
        current_dir = os.getcwd()
    folder_list = []

    folder_list.append(os.path.basename(current_dir))
    current_dir = get_parent_dir(current_dir)
    while True:

        if 'assets' in os.listdir(current_dir):
            folder_list.reverse()
            folder_list.insert(1, "bvids")
            folder_list.insert(2, key_word)
            return folder_list, current_dir

        else:
            folder_list.append(os.path.basename(current_dir))
            current_dir = get_parent_dir(current_dir)


def get_bvids_destination(folder_list, BaiduSyncdisk_assets_root):
    path_temp = BaiduSyncdisk_assets_root
    for i in range(len(folder_list)-1):

        folder_temp = folder_list[i].split('_')[0]
        if folder_temp != "mc":
            path_temp = os.path.join(path_temp, folder_temp)
        else:
            path_temp = os.path.join(path_temp, folder_list[i])
        if not os.path.exists(path_temp):
            os.makedirs(path_temp)
    return path_temp


def get_bvids_origin_path(BaiduSyncdisk_assets_root):
    return os.path.join(BaiduSyncdisk_assets_root, "assets", "bvids", "mc_1683793602")


def get_bvid_name():
    file = os.path.basename(os.getcwd())
    return file+".mp4"


def get_note_name():
    file = os.path.basename(os.getcwd())
    return file+".md"


def get_OneDrive_KG_note_path(OneDrive_KG_root, folder_list):
    OneDrive_KG_note_path = OneDrive_KG_root
    for i in range(3, len(folder_list)-1):
        OneDrive_KG_note_path = os.path.join(
            OneDrive_KG_note_path, folder_list[i])
    print(OneDrive_KG_note_path)
    return OneDrive_KG_note_path


def vid_path_2_md_vid_link(vid_path, bvid_name):
    url_path = urllib.parse.quote(os.path.abspath(vid_path))
    url = "file:///" + url_path.replace("\\", "/")
    md_show_url = f"![{bvid_name}]({url})"
    md_url = f"[{bvid_name}]({url})"
    return md_show_url, md_url


def full_fill_vid_link_2_summary():

    folder_list, OneDrive_KG_root = get_bvids_path(key_word="mc_1683793602")
    BaiduSyncdisk_assets_root = get_b_assets_path(OneDrive_KG_root)
    bvids_origin_path = get_bvids_origin_path(BaiduSyncdisk_assets_root)
    bvids_origin_path = r"C:\BaiduSyncdisk\Multivariable_calculus_Khan_Academy_youtube"
    print(folder_list, BaiduSyncdisk_assets_root)
    # print(bvids_origin_path)
    files = [f for f in os.listdir(bvids_origin_path) if os.path.isfile(
        os.path.join(bvids_origin_path, f)) and f.endswith(".mp4")]
    OneDrive_KG_note_path = get_OneDrive_KG_note_path(
        OneDrive_KG_root, folder_list)
    bvid_name = get_bvid_name()
    number_data = bvid_name[:4]
    print(bvid_name)
    bvids_destination_path = get_bvids_destination(
        folder_list, BaiduSyncdisk_assets_root)
    print(bvids_destination_path)
    reg_search = r'.+\(P\d{1,3}\. \d{1,3}\.\d{1,3}\.\d{1,3}(.+)\)\.mp4'
    flag_one_by_one = False
    if flag_one_by_one:
        vid_name_origin = files[0]
        content2 = "\n"+re.sub(reg_search, r'\1', vid_name_origin)
        vid_path = os.path.join(bvids_destination_path, bvid_name)
        if not os.path.exists(vid_path):

            os.rename(os.path.join(bvids_origin_path,
                      vid_name_origin), vid_path)
    else:
        content2 = ""
        for file in files:
            if (number_data+file) == bvid_name:
                vid_name_origin = file

                break
        vid_path = os.path.join(bvids_destination_path, bvid_name)
        if not os.path.exists(vid_path):

            os.rename(os.path.join(bvids_origin_path,
                      vid_name_origin), vid_path)
        files_srt = [f for f in os.listdir(bvids_origin_path) if os.path.isfile(
            os.path.join(bvids_origin_path, f)) and f.endswith(".srt")]
        for file_srt in files_srt:
            # print(number_data+file_srt[:-7]+".mp4")
            # print(file_srt[-7:])
            if (number_data+file_srt[:-7]+".mp4" == bvid_name) and (file_srt[-7:] == ".en.srt"):
                srt_path = os.path.join(bvids_destination_path, file_srt)
                if not os.path.exists(srt_path):
                    os.rename(os.path.join(
                        bvids_origin_path, file_srt), srt_path)

    md_show_url, md_url = vid_path_2_md_vid_link(vid_path, bvid_name)
    content3 = '\n\n'+md_url+'\n'+md_show_url+'\n\n'
    output_dir, file_summary = convert_subtitle_and_summary_to_markdown_vid_timeline(
        md_show_url)
    note_name = get_note_name()
    if not os.path.exists(os.path.join(OneDrive_KG_note_path, note_name)):
        raise Exception("note not found")
    else:
        with open(os.path.join(OneDrive_KG_note_path, note_name), "r", encoding="utf-8") as f:
            content1 = f.read()
        with open(os.path.join(output_dir, file_summary), "r", encoding="utf-8") as f:
            content4 = f.read()
        with open(os.path.join(OneDrive_KG_note_path, note_name), "w", encoding="utf-8") as f:
            f.write(content1+content2+content3+content4)


# def lower_header_level_in_md_files(path=None):
#     if path is None:
#         path = os.getcwd()
#     files_md = [f for f in os.listdir(path) if f.endswith('.md')]
#     reg_string_head=[r"(#{1,6}) (.+)",r" \2"]
#     for file in files_md:

#         with open(os.path.join(path,file),"r",encoding="utf-8") as f:
#             lines=f.readlines()
#         with open(os.path.join(path,file),"w",encoding="utf-8") as f:

#             for line in lines:

#                 match = re.search(reg_string_head[0],line)
#                 if match:
#                     string_sharp=match.group(1)
#                     head_num=string_sharp.count("#")
#                     line=re.sub(reg_string_head[0],(head_num+1)*"#"+reg_string_head[1],line)
#                 f.write(line)


def lower_header_level_in_md_files(path=None):
    if path is None:
        path = os.getcwd()

    files_md = [f for f in os.listdir(path) if f.endswith('.md')]
    reg_string_head = re.compile(r"(#{1,6}) (.+)")
    #what is compile
    for file in files_md:
        try:
            with open(os.path.join(path, file), "r", encoding="utf-8") as f:
                lines = f.readlines()

            processed_lines = []
            for line in lines:
                match = reg_string_head.search(line)
                if match:
                    string_sharp = match.group(1)
                    head_num = string_sharp.count("#")
                    line = reg_string_head.sub((head_num + 1) * "#" + r" \2", line)
                processed_lines.append(line)

            with open(os.path.join(path, file), "w", encoding="utf-8") as f:
                f.writelines(processed_lines)
        except Exception as e:
            print(f"Failed to process file {file} due to {str(e)}")

def prepend_filename_as_header_if_chapter_present(directory=None):
    reg_string1=r"\d{3}_(第.{1,2}章.+)"
    reg_string2=r"\d{3}_(\d{1,2} .+)\.md"

    if directory is None:
        directory = os.getcwd()
    reg_string=reg_string2
    files_md = [f for f in os.listdir(directory) if f.endswith('.md')]
    # Iterate over all files in the directory
    for filename in files_md:
        # If the filename contains 'Chapter'
        match=re.search(reg_string, filename)
        if match:
            chapter_name=match.group(1)
            print(chapter_name)
            # Open the file and read its contents
            with open(os.path.join(directory, filename), 'r',encoding="utf-8") as f:
                content = f.readlines()

            # Prepend the filename as a level 2 header
            content.insert(0, f'## {chapter_name}\n')

            # Write the modified content back to the file
            with open(os.path.join(directory, filename), 'w',encoding="utf-8") as f:
                f.writelines(content)
def remove_md_copy_code(path=None):
    if path is None:
        path = os.getcwd()
    reg_string=[r"```\n(.+)Copy code",r"```\1\n"]
    reg_string_list=[]
    reg_string_list.append(reg_string)

    files_md = [f for f in os.listdir(path) if f.endswith('.md')]
    perform_regex_replacement_on_files(reg_string_list,path,files_md)

# def format_index_file(path=None):
#     if path is None:
#         path = os.getcwd()
#     inedex_name="000_index.md"
#     if inedex_name not in os.listdir(path):
#         raise Exception("index file not found")
#     files=[]
#     files.append(os.path.join(path,inedex_name))
#     reg_string=[r"- \[(.+)\]\(.+\)",r"\1"]
#     reg_string_list=[]
#     reg_string_list.append(reg_string)
#     perform_regex_replacement_on_files(reg_string_list,path,files)


def perform_regex_replacement_on_index_file(directory_path=None):
    """
    This function checks for the existence of an index file in the given directory
    path and performs a regex replacement on it.
    Args:
        directory_path: Path to the directory to check. Defaults to the current working directory.
    Raises:
        FileNotFoundError: If the index file is not found in the directory.
    """
    if directory_path is None:
        directory_path = os.getcwd()

    index_filename = "000_index.md"

    if index_filename not in os.listdir(directory_path):
        raise FileNotFoundError("Index file not found")

    file_paths = [os.path.join(directory_path, index_filename)]
    regex_patterns = [(r"- \[(.+)\]\(.+\)", r"\1")]

    perform_regex_replacement_on_files(regex_patterns, directory_path, file_paths)
def perform_regex_replacement_on_zhi_mds(directory_path=None):

    if directory_path is None:
        directory_path = os.getcwd()

    files_md = [f for f in os.listdir(directory_path) if f.endswith('.md')]

    reg_string_list=[]
    reg_index_link=[r"-\s+\[.+\]\(https://www.zhihu.com/pub/reader/.+\)\n",r""]
    reg_string_list.extend([reg_index_link])
    reg_zhi_sao_ma=[r"扫码下载知乎APP 客户端\n\n!\[\]\(.+sidebar-download-qrcode.wybWudky.png\)\n",r""]
    reg_string_list.extend([reg_zhi_sao_ma])
    reg_Back_matter_template=[r"---\n\n- created:.+\n- source: .+",r""]
    reg_string_list.extend([reg_Back_matter_template])

    perform_regex_replacement_on_files(reg_string_list, directory_path, files_md)

def convert_zhi_footnote_to_obsidian(directory_path=None):
    if directory_path is None:
        directory_path = os.getcwd()

    files_md = [f for f in os.listdir(directory_path) if f.endswith('.md')]

    reg_string_list=[]
    #r"[\[1\]](https://www.zhihu.com/pub/reader/120057501/chapter/1302455544230445056#n1s) 在英语中，发散一词是diffuse。注意focused（专注）一词的词尾是-ed，而diffuse则不是。发散一词的意思是“薄薄地弥漫出去”。"
    reg_string1=[r'<sup><a href="https://www.zhihu.com/pub/.+" id=".+">\[(\d{1,2})\] </a></sup>',r"[^\1]"]
    reg_string_list.extend([reg_string1])
    reg_string2=[r'\[\\\[(\d{1,2})\\\]\]\(https://www\.zhihu\.com/pub/.+\) (.+)',r"[^\1]: (\2)"]
    reg_string_list.extend([reg_string2])

    perform_regex_replacement_on_files(reg_string_list, directory_path, files_md)
def perform_regex_replacement_on_zhi_book_mds_name(path=None):
    if path is None:
        path = os.getcwd()
    files_md=[f for f in os.listdir(path) if f.endswith('.md')]
    reg_string_dir = [r"(.+) - .+ - 知乎书店", r"\1"]
    reg_string_md = [r"(.+) - .+ - 知乎书店(\.md)", r"\1\2"]
    reg_string_md2=[r"{ (.+) }", r"{\1}"]
    reg_string_list=[]
    reg_string_list.append(reg_string_md)
    perform_regex_rename_on_files(reg_string_list,path,files_md)
    dirs = [directory for directory in os.listdir(path) if os.path.isdir(directory)]
    reg_string_list=[]
    reg_string_list.append(reg_string_dir)
    perform_regex_rename_on_files(reg_string_list,path,dirs)

def perform_regex_replacement_on_files(reg_string_list,path=None,files=None):

    if path is None:
        path = os.getcwd()
    if files is None:
        files = os.listdir(path)

    for file in files:

        with open(os.path.join(path, file), "r", encoding="utf-8") as f1:
            content=f1.read()
        for regex in reg_string_list:
            content=re.sub(regex[0],regex[1],content)
        with open(os.path.join(path, file), "w", encoding="utf-8") as f:
            f.write(content)

def perform_regex_rename_on_files(reg_string_list,path=None,files=None):

    if path is None:
        path = os.getcwd()
    if files is None:
        files = os.listdir(path)

    for file in files:
        for reg_string in reg_string_list:
            match = re.search(reg_string[0], file)
            if match is not None:
                new_file = re.sub(reg_string[0], reg_string[1], file)
                print(new_file)
                os.rename(file, new_file)
def perform_regex_replacement_on_md_files(path=None):

    if path is None:
        path = os.getcwd()
    files = os.listdir(path)
    dirs = [directory for directory in os.listdir(path) if os.path.isdir(directory)]
    reg_string_list=[]
    reg_index_link=[r"-\s+\[.+\]\(https://www.zhihu.com/pub/reader/.+\)\n",r""]
    reg_string_list.extend([reg_index_link])
    reg_zhi_sao_ma=[r"扫码下载知乎APP 客户端\n\n!\[\]\(.+sidebar-download-qrcode.wybWudky.png\)\n",r""]
    reg_string_list.extend([reg_zhi_sao_ma])
    reg_Back_matter_template=[r"---\n\n- created:.+\n- source: .+",r""]
    reg_string_list.extend([reg_Back_matter_template])
    reg_string_remove_zhi_mul_img=[r"!\[\]\(.+\)\n\n(!\[\]\(.+\.webp\))",r"\1"]
    #reg_string_list.extend([reg_string_remove_zhi_mul_img])
    assets_root_path,assets_root_dir=get_assets_root_path()
    output_path=create_output_directory(assets_root_path)
    for file in files:
        if file.endswith(".md"):

            with open(os.path.join(path, file), "r", encoding="utf-8") as f1:
                content=f1.read()
            for regex in reg_string_list:
                content=re.sub(regex[0],regex[1],content)
            with open(os.path.join(path, file), "w", encoding="utf-8") as f:
                f.write(content)


def rename_files_and_folders_by_regex(path=None):
    if path is None:
        path = os.getcwd()
    files = os.listdir(path)
    dirs = [directory for directory in os.listdir(path) if os.path.isdir(directory)]
    # print(dirs)
    reg_string_dir = [r"(.+) - .+ - 知乎书店", r"\1"]
    reg_string_md = [r"(.+) - .+ - 知乎书店(\.md)", r"\1\2"]
    reg_string1 = [
        r"(.+) - Multivariable Calculus - Khan.+(\.en\.srt|\.mp4)", r"\1\2"]
    reg_string_vid = [r"(.+) - Multivariable Calculus - Kh.+(\.mp4)", r"\1\2"]
    reg_string_srt = [
        r"(.+) - Multivariable Calculus - Kh.+(\..+\.srt)", r"\1\2"]
    for file in files:
        if file.endswith(".mp4"):
            match = re.search(reg_string_vid[0], file)
            if match is not None:
                new_file = re.sub(reg_string_vid[0], reg_string_vid[1], file)
                print(new_file)
                os.rename(file, new_file)
        if file.endswith('.srt'):
            match = re.search(reg_string_srt[0], file)
            if match is not None:

                new_file = re.sub(reg_string_srt[0], reg_string_srt[1], file)
                print(new_file)
                os.rename(file, new_file)
        if file.endswith(".md"):
            match = re.search(reg_string_md[0], file)
            if match is not None:
                new_file = re.sub(reg_string_md[0], reg_string_md[1], file)
                print(new_file)
                os.rename(file, new_file)
    for directory in dirs:
        match = re.search(reg_string_dir[0], directory)
        if match is not None:
            new_directory = re.sub(
                reg_string_dir[0], reg_string_dir[1], directory)
            print(new_directory)
            os.rename(directory, new_directory)





def main():
    # create a parser object
    parser = argparse.ArgumentParser()

    # add arguments for each function
    parser.add_argument('-t', '--timestamp', type=str, default=r'1676880280',
                        help='input timestamp to pass to the function')
    parser.add_argument('-u', '--str_url', type=str, default=r'test',
                        help='input str_url to pass to the function')
    parser.add_argument('-ii', '--input_int', type=int, default=r'0',
                    help='input input_int to pass to the function')
    parser.add_argument('-gt', '--get_timestamp',
                        action='store_true', help='call get_current_timestamp')
    parser.add_argument('-at', '--add_timestamp', action='store_true',
                        help='call add_timestamp_to_filenames')

    parser.add_argument('-regmd', '--perform_regex_replacement_on_md_files', action='store_true',
                        help='call perform_regex_replacement_on_md_files')
    parser.add_argument('-mdx', '--mdx2md',
                        action='store_true', help='call mdx2md')
    parser.add_argument('-oaf', '--open_b_assets_folder',
                        action='store_true', help='call open_b_assets_folder')
    parser.add_argument('-rfe', '--remove_filesname_end',
                        action='store_true', help='call remove_filesname_end')
    parser.add_argument('-ds', '--rename_files_sensor_fusion',
                        action='store_true', help='call rename_files_sensor_fusion')
    parser.add_argument('-tt', '--timestamps_3blue1brown_2_timeline',
                        action='store_true', help='call timestamps_3blue1brown_2_timeline')
    parser.add_argument('-cti', '--copy_timestamps_and_index_2_root',
                        action='store_true', help='call copy_timestamps_and_index_2_root')
    parser.add_argument('-csm', '--convert_subtitle_chatgpt_summary_to_markdown_vid_timeline',
                        action='store_true', help='call convert_subtitle_chatgpt_summary_to_markdown_vid_timeline')
    parser.add_argument('-cssm', '--convert_subtitle_and_summary_to_markdown_vid_timeline',
                        action='store_true', help='call convert_subtitle_and_summary_to_markdown_vid_timeline')

    parser.add_argument('-ci', '--create_imgs_folder',
                        action='store_true', help='call create_directory_assets_imgs')
    parser.add_argument('-cc', '--creat_concept_folder', action='store_true',
                        help='call create_directory_assets_concept_structure')
    parser.add_argument('-css', '--creat_subtitle_summary', action='store_true',
                        help='call create_file_subtitle_summary_base_on_chatgpt_md')
    parser.add_argument('-h2m', '--html2md',
                        action='store_true', help='call html2md')
    parser.add_argument('-h2m2', '--html2md2',
                        action='store_true', help='call html2md2')

    parser.add_argument('-h2mt', '--html2md_tree',
                        action='store_true', help='call html2md_tree')
    parser.add_argument('-m2hl', '--vid_link_md_2_html',
                        action='store_true', help='call vid_link_md_2_html')
    parser.add_argument('-init', '--init_note',
                        action='store_true', help='call init_note')
    parser.add_argument('-test', '--test',
                        action='store_true', help='call test')
    parser.add_argument('-vls', '--full_fill_vid_link_2_summary',
                        action='store_true', help='call full_fill_vid_link_2_summary')
    # parse the command-line arguments
    args = parser.parse_args()

    # call the appropriate function based on the arguments
    if args.rename_files_sensor_fusion:
        rename_files_sensor_fusion()
    elif args.copy_timestamps_and_index_2_root:
        copy_timestamps_and_index_2_root()
    elif args.convert_subtitle_chatgpt_summary_to_markdown_vid_timeline:
        convert_subtitle_chatgpt_summary_to_markdown_vid_timeline(args.str_url)
    elif args.convert_subtitle_and_summary_to_markdown_vid_timeline:
        convert_subtitle_and_summary_to_markdown_vid_timeline(args.str_url)
    elif args.mdx2md:
        mdx2md(args.timestamp)
    elif args.open_b_assets_folder:
        open_b_assets_folder()
    elif args.timestamps_3blue1brown_2_timeline:
        timestamps_3blue1brown_2_timeline(args.str_url)
    elif args.get_timestamp:
        get_current_timestamp()
    elif args.add_timestamp:
        add_timestamp_to_filenames()

    elif args.perform_regex_replacement_on_md_files:
        perform_regex_replacement_on_md_files()
    elif args.create_imgs_folder:
        create_directory_assets_imgs()
    elif args.creat_concept_folder:
        create_directory_assets_concept_structure()
    elif args.creat_subtitle_summary:
        create_file_subtitle_summary_base_on_chatgpt_md()
    elif args.html2md:
        html2md()
    elif args.html2md2:
        html2md2()
    elif args.html2md_tree:
        html2md_tree()
    elif args.vid_link_md_2_html:
        vid_link_md_2_html()
    elif args.init_note:
        init_note()
    elif args.full_fill_vid_link_2_summary:
        full_fill_vid_link_2_summary()
    elif args.test:
        test(args.input_int)
    else:
        print("Invalid argument")


if __name__ == "__main__":
    main()
