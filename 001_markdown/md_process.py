#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

import time

import os
import datetime
import shutil
import argparse
import aspose.words as aw
import urllib.parse


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
    assets_root_path, assets_root_dir = get_assets_root_path()
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
    assets_root_path, assets_root_dir = get_assets_root_path()
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
                # [r"show=\"video\"\n", r""],
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
                # [r'emotion="\w+"[ \t]+\n', r''],
                # [r'flip=\{(true|false)\}\n', r''],
                # [r'(?s)<Question .+?</Question>', r'tttttttttttttttttttt'],
                [r'answer=\{(\d)\}[ \n\t]{0,}>',
                                     r'\n<details><summary>answer</summary><p>Choice= \1</p></details>\n\n- **Explanation**'],
                # [r'''<Question[\n \t]{0,}question="(.+)"[\n \t]{0,}choice1="(.+)"[\n \t]{0,}choice2="(.+)"[\n \t]{0,}choice3="(.+)"[\n \t]{0,}choice4="(.+)"[\n \t]answer=\{(\d)\}[\n \t]{0,}>''',r'- **Question**\n\t\1']
                [r'[ \t]{0,}question="(.+)"',
                                     r'- **Question**\n\t\1'],
                [r'[ \t]{0,}choice1="(.+)"',
                                     r'    - **Choice 1=** \1'],
                [r'[ \t]{0,}choice2="(.+)"',
                                     r'    - **Choice 2=** \1'],
                [r'[ \t]{0,}choice3="(.+)"', r'    - **Choice 3=** \1'],
                [r'[ \t]{0,}choice4="(.+)"', r'    - **Choice 4=** \1'],
                # [r'video=".+\.mp4"', r''],
                # [r'show="video"', r''],
                [r'([ \t]{0,}\n){3,}', r'\1\1'],
                # ['/>', r''],
            ]

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


def check_video_file_path_conforms_to_pattern(str_url):
    r"![001_Derivatives of multivariable functions.mp4](file:///C%3A%5CBaiduSyncdisk%5Cassets%5CO%5CO1%5CO17%5CO172%5CMultivaribale_calculus_Khan_Academy%5Cassets%5Cbvids%5Cmc_1683793602%5C002%5C001%5C001_Derivatives%20of%20multivariable%20functions.mp4)"
    url_pattern_4_file_vid = r'(!\[.+\..+\]\(file:///C:%5CBaiduSyncdisk%5Cassets(%5C.+){1,}\.\w+)(\))'
    url_pattern_4_file_vid2 = r'(!\[.+\..+\]\(file:///C%3A%5CBaiduSyncdisk%5Cassets(%5C.+){1,}\.\w+)(\))'
    match1 = re.search(url_pattern_4_file_vid, str_url)
    if not match1:
        match1 = re.search(url_pattern_4_file_vid2, str_url)
        if not match1:
            print("str_url: ", str_url)
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
    assets_root_path, assets_root_dir = get_assets_root_path()
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
    return output_dir, new_file_name


def get_list_time_head_textshort_text_4_file(file, key_word):
    print("start to generate time line for video and head text:")

    number_list_head_time_text_pattern_str = r'((\d{1,2}\.)|-)[ ]{1,}(.+) \((\d{1,2}):(\d{1,2})\) (.+)'
    number_list_head_time_pattern_str = r'(\d{1,2}):(\d{1,2}) - (.+)'

    time_text_pattern_str = r'\((\d{1,2}):(\d{1,2})\)[ ]{0,}([^\n]+)[\n]{0,}'

    pattern_dict = dict()
    pattern_dict["timestamps"] = number_list_head_time_pattern_str
    pattern_dict["summary_gpt"] = number_list_head_time_text_pattern_str
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
                    elif key_word == "summary_gpt":
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
            else:
                raise Exception("key_word not in pattern_dict")

    # print("List of time, heading, short text, text:")
    # print(list_time_head_textshort_text)
    return list_time_head_textshort_text


def timestamps_3blue1brown_2_timeline(str_url):
    # process url
    # str_url=r'![007_limits.mp4](file:///C:%5CBaiduSyncdisk%5Cassets%5CO%5CO1%5CO17%5CO172%5CCalculus%203Blue1Brown%5Cassets%5Cbvids%5C007_limits.mp4)'
    # '(!\[.+\..+\]\(file:///C:%5CBaiduSyncdisk%5Cassets(%5C.+){1,}\.\w+)(\))'
    match1 = check_video_file_path_conforms_to_pattern(str_url)
    # timestamps file
    file_list = os.listdir(os.getcwd())
    for file in file_list:
        if file.endswith(".md") or file.endswith(".txt"):
            if file.find("timestamps") != -1:
                key_word = "timestamps"
                list_time_head_textshort_text = get_list_time_head_textshort_text_4_file(
                    file, key_word)

                output_dir, file_name = list_time_head_textshort_text_to_vid_timeline_md(
                    list_time_head_textshort_text, file, match1)

                return output_dir, file_name


def convert_subtitle_chatgpt_summary_to_markdown_vid_timeline(str_url):

    # str_url=r'![009_area-and-slope.mp4](file:///C:%5CBaiduSyncdisk%5Cassets%5CO%5CO1%5CO17%5CO172%5CCalculus%203Blue1Brown%5Cassets%5Cbvids%5C009_area-and-slope.mp4)'

    match1 = check_video_file_path_conforms_to_pattern(str_url)
    cwd = os.getcwd()
    file_list = os.listdir(cwd)
    assets_root_path, assets_root_dir = get_assets_root_path()
    create_output_directory(assets_root_path)

    for file in file_list:
        if file.endswith(".md"):
            if file.find("summary_gpt") != -1:
                key_word = "summary_gpt"
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


def convert_gpt_summary_to_markdown_vid_timeline(str_url, path=None):

    # str_url=r'![009_area-and-slope.mp4](file:///C:%5CBaiduSyncdisk%5Cassets%5CO%5CO1%5CO17%5CO172%5CCalculus%203Blue1Brown%5Cassets%5Cbvids%5C009_area-and-slope.mp4)'

    match1 = check_video_file_path_conforms_to_pattern(str_url)

    if path is None:
        path = os.getcwd()
    file_list = os.listdir(path)
    assets_root_path, assets_root_dir = get_assets_root_path()
    output_dir = create_output_directory(assets_root_path)

    for file in file_list:
        if file.endswith(".md"):

            if file.find("summary_gpt") != -1:
                cwd_floder_name = os.path.basename(path)
                file_summary = file
                key_word = "summary_gpt"
                list_time_head_textshort = get_list_time_head_textshort_text_4_file(
                    file, key_word)
                # list_time_head_textshort_text_to_vid_timeline_md(list_time_head_textshort_text,file,match1)

    list_time_head_textshort_text_to_vid_timeline_md(
        list_time_head_textshort, file_summary, match1)
    convert_md_vid_link_to_html(output_dir)
    return output_dir, file_summary


def convert_subtitle_and_summary_to_markdown_vid_timeline(str_url):

    # str_url=r'![009_area-and-slope.mp4](file:///C:%5CBaiduSyncdisk%5Cassets%5CO%5CO1%5CO17%5CO172%5CCalculus%203Blue1Brown%5Cassets%5Cbvids%5C009_area-and-slope.mp4)'

    match1 = check_video_file_path_conforms_to_pattern(str_url)
    cwd = os.getcwd()
    file_list = os.listdir(cwd)
    assets_root_path, assets_root_dir = get_assets_root_path()
    output_dir = create_output_directory(assets_root_path)

    for file in file_list:
        if file.endswith(".md"):
            if file.find("subtitle") != -1:
                key_word = "subtitle"
                list_time_text = get_list_time_head_textshort_text_4_file(
                    file, key_word)
                # list_time_head_textshort_text_to_vid_timeline_md(list_time_head_textshort_text,file,match1)

            if file.find("summary_gpt") != -1:
                cwd_floder_name = os.path.basename(cwd)
                file_summary = file
                key_word = "summary_gpt"
                list_time_head_textshort = get_list_time_head_textshort_text_4_file(
                    file, key_word)
                # list_time_head_textshort_text_to_vid_timeline_md(list_time_head_textshort_text,file,match1)

    list_time_head_textshort_text = merge_list_time_head_textshort_text(
        list_time_text, list_time_head_textshort)
    print("final is:")
    print(list_time_head_textshort_text)
    list_time_head_textshort_text_to_vid_timeline_md(
        list_time_head_textshort_text, file_summary, match1)
    convert_md_vid_link_to_html(output_dir)
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


def html2md(path=None, output_root="C://Output//", output_folder_name=None):
    if path is None:
        path = os.getcwd()
    timestamp = int(time.time())
    intput_path = path
    input_floder_name = os.path.basename(intput_path)
    # replace_list_regex2=[[r'Part \d{2}-Module \d{2}-Lesson (\d{2})_(.+)',r'0\1_\2'],]
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
    md_note_process(output_path)
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


def create_file_subtitle_summary_gpt_md(path=None):
    # Create a file named subtitle.md and summary_gpt.md
    print("create_file_subtitle_summary_gpt_md")
    if path is None:
        path = os.getcwd()
    time_stamp = get_current_timestamp()
    with open(os.path.join(path, "subtitle_"+str(time_stamp)+".md"), "w") as f:
        pass
    with open(os.path.join(path, "summary_gpt_"+str(time_stamp)+".md"), "w") as f:
        pass
    with open(os.path.join(path, "timestamps_"+str(time_stamp)+".md"), "w") as f:
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
            return current_dir, os.path.basename(current_dir)
        else:
            current_dir = get_parent_dir(current_dir)
            if current_dir == '':
                raise Exception('assets folder not found')


def get_note_assets_dir_path(sub_topic1_to_sub_topicn_folder_list, current_dir):
    # sub_topic1_to_sub_topicn_folder_list.append(os.path.basename(current_dir))
    # current_dir = get_parent_dir(current_dir)
    while True:

        if 'assets' in os.listdir(current_dir):
            sub_topic1_to_sub_topicn_folder_list.reverse()
            if sub_topic1_to_sub_topicn_folder_list != []:
                note_assets_dir_path = os.path.join(current_dir, 'assets')
                for folder_name in sub_topic1_to_sub_topicn_folder_list:
                    note_assets_dir_path = os.path.join(
                        note_assets_dir_path, folder_name)
                    # print(note_assets_dir_path)
                    # if os.path.isdir(note_assets_dir_path):
                    if not os.path.exists(note_assets_dir_path):
                        os.makedirs(note_assets_dir_path)
                return note_assets_dir_path
                # else:
                #     raise Exception('not a directory ',note_assets_dir_path)
            else:
                raise Exception("No folder name found")

            break
        else:
            sub_topic1_to_sub_topicn_folder_list.append(
                os.path.basename(current_dir))
            current_dir = get_parent_dir(current_dir)


def get_md_files(directory='.'):
    """Return a sorted list of markdown filenames in a given directory."""
    files = [f for f in os.listdir(directory) if f.endswith('.md')]
    # Extract numeric prefix and sort based on it
    files.sort(key=lambda x: int(re.match(r'(\d{3})_', x).group(
        1)) if re.match(r'(\d{3})_', x) else float('inf'))
    return files


def check_md_files(files):

    # Check if files are in expected order
    for i, filename in enumerate(files):
        expected_prefix = f"{i:03d}_"
        if not filename.startswith(expected_prefix):
            print(
                f"Warning: {filename} does not match expected prefix {expected_prefix}")


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
    output_file = os.path.join(root_path, root_dir+".md")
    md_files = get_md_files()
    check_md_files(md_files)
    merge_files(md_files, output_file)


def Merge_all_md_files_into_one_file_base_on_num_index():
    files = [f for f in os.listdir() if f.endswith('.md')]
    files.sort()
    print(files)
    root_path, root_dir = get_assets_root_path()
    with open(os.path.join(root_path, root_dir+".md"), 'w', encoding='utf-8') as f:
        for file in files:
            with open(file, 'r', encoding='utf-8') as f2:
                content = f2.read()
                f.write(content)
                f.write('\n\n')


def zhi_book_process(num=0):
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
        raise ValueError(
            "Invalid operation number. Please choose a number between 0 and 4.")


def test():
    pass


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


def get_bvids_destination_short(sub_topic1_to_sub_topicn_folder_list, BaiduSyncdisk_assets_root):
    path_temp = BaiduSyncdisk_assets_root
    for i in range(len(sub_topic1_to_sub_topicn_folder_list)-1):

        folder_temp = sub_topic1_to_sub_topicn_folder_list[i].split('_')[0]
        if folder_temp != "FPCV":
            path_temp = os.path.join(path_temp, folder_temp)
        else:
            path_temp = os.path.join(
                path_temp, sub_topic1_to_sub_topicn_folder_list[i])
        if not os.path.exists(path_temp):
            os.makedirs(path_temp)
    return path_temp


def get_bvids_origin_topic_path(BaiduSyncdisk_assets_root):
    return os.path.join(BaiduSyncdisk_assets_root, "assets", "bvids", "mc_1683793602")


def get_current_bvid_name():
    file = os.path.basename(os.getcwd())
    return file+".mp4"


def get_note_name():
    file = os.path.basename(os.getcwd())
    return file+".md"


def get_note_vid_tra_name():
    file = os.path.basename(os.getcwd())
    return file+r'_vid_tra'+".md"


def get_note_vid_name():
    file = os.path.basename(os.getcwd())
    return file+r'_vid'+".md"


def get_OneDrive_KG_note_path(OneDrive_KG_root, sub_topic1_to_sub_topicn_folder_list):
    OneDrive_KG_note_path = OneDrive_KG_root
    for i in range(2, len(sub_topic1_to_sub_topicn_folder_list)-1):
        OneDrive_KG_note_path = os.path.join(
            OneDrive_KG_note_path, sub_topic1_to_sub_topicn_folder_list[i])
    print(OneDrive_KG_note_path)
    return OneDrive_KG_note_path


def vid_path_2_md_vid_link(vid_path, current_bvid_name):
    url_path = urllib.parse.quote(os.path.abspath(vid_path))
    url = "file:///" + url_path.replace("\\", "/")
    md_show_url = f"![{current_bvid_name}]({url})"
    md_url = f"[{current_bvid_name}]({url})"
    return md_show_url, md_url


def lower_header_level_in_md_files(path=None):
    if path is None:
        path = os.getcwd()

    files_md = [f for f in os.listdir(path) if f.endswith('.md')]
    reg_string_head = re.compile(r"(#{1,6}) (.+)")
    # what is compile
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
                    line = reg_string_head.sub(
                        (head_num + 1) * "#" + r" \2", line)
                processed_lines.append(line)

            with open(os.path.join(path, file), "w", encoding="utf-8") as f:
                f.writelines(processed_lines)
        except Exception as e:
            print(f"Failed to process file {file} due to {str(e)}")


def prepend_filename_as_header_if_chapter_present(directory=None):
    reg_string1 = r"\d{3}_(第.{1,2}章.+)"
    reg_string2 = r"\d{3}_(\d{1,2} .+)\.md"

    if directory is None:
        directory = os.getcwd()
    reg_string = reg_string2
    files_md = [f for f in os.listdir(directory) if f.endswith('.md')]
    # Iterate over all files in the directory
    for filename in files_md:
        # If the filename contains 'Chapter'
        match = re.search(reg_string, filename)
        if match:
            chapter_name = match.group(1)
            print(chapter_name)
            # Open the file and read its contents
            with open(os.path.join(directory, filename), 'r', encoding="utf-8") as f:
                content = f.readlines()

            # Prepend the filename as a level 2 header
            content.insert(0, f'## {chapter_name}\n')

            # Write the modified content back to the file
            with open(os.path.join(directory, filename), 'w', encoding="utf-8") as f:
                f.writelines(content)


def remove_md_copy_code(path=None):
    if path is None:
        path = os.getcwd()
    reg_string_copy_code = [r"```\n(.+)Copy code", r"```\1\n"]
    reg_string_list = []
    reg_string_list.append(reg_string_copy_code)

    files_md = [f for f in os.listdir(path) if f.endswith('.md')]
    perform_regex_replacement_on_files(reg_string_list, path, files_md)


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

    perform_regex_replacement_on_files(
        regex_patterns, directory_path, file_paths)


def perform_regex_replacement_on_zhi_mds(directory_path=None):

    if directory_path is None:
        directory_path = os.getcwd()

    files_md = [f for f in os.listdir(directory_path) if f.endswith('.md')]

    reg_string_list = []
    reg_index_link = [
        r"-\s+\[.+\]\(https://www.zhihu.com/pub/reader/.+\)\n", r""]
    reg_string_list.extend([reg_index_link])
    reg_zhi_sao_ma = [
        r"扫码下载知乎APP 客户端\n\n!\[\]\(.+sidebar-download-qrcode.wybWudky.png\)\n", r""]
    reg_string_list.extend([reg_zhi_sao_ma])
    reg_Back_matter_template = [r"---\n\n- created:.+\n- source: .+", r""]
    reg_string_list.extend([reg_Back_matter_template])

    perform_regex_replacement_on_files(
        reg_string_list, directory_path, files_md)


def convert_zhi_footnote_to_obsidian(directory_path=None):
    if directory_path is None:
        directory_path = os.getcwd()

    files_md = [f for f in os.listdir(directory_path) if f.endswith('.md')]

    reg_string_list = []
    # r"[\[1\]](https://www.zhihu.com/pub/reader/120057501/chapter/1302455544230445056#n1s) 在英语中，发散一词是diffuse。注意focused（专注）一词的词尾是-ed，而diffuse则不是。发散一词的意思是“薄薄地弥漫出去”。"
    reg_string1 = [
        r'<sup><a href="https://www\.zhihu\.com/pub/reader.+n\d{1,2}" id="n\d{1,2}s">\[(\d{1,2})\]</a></sup>', r"[^\1]"]
    # r'<sup><a href="https://www\.zhihu\.com/pub/reader.+n\d{1,2}" id="n\d{1,2}s">\[\d{1,2}\]</a></sup>'
    reg_string_list.extend([reg_string1])
    reg_string2 = [
        r'\[\\\[(\d{1,2})\\\]\]\(https://www\.zhihu\.com/pub/.+\) (.+)', r"[^\1]: (\2)"]
    reg_string_list.extend([reg_string2])

    perform_regex_replacement_on_files(
        reg_string_list, directory_path, files_md)


def perform_regex_replacement_on_zhi_book_mds_name(path=None):
    if path is None:
        path = os.getcwd()
    files_md = [f for f in os.listdir(path) if f.endswith('.md')]
    reg_string_dir = [r"(.+) - .+ - 知乎书店", r"\1"]
    reg_string_md = [r"(.+) - .+ - 知乎书店(\.md)", r"\1\2"]
    reg_string_md2 = [r"{ (.+) }", r"{\1}"]
    reg_string_list = []
    reg_string_list.append(reg_string_md)
    perform_regex_rename_on_files(reg_string_list, path, files_md)
    dirs = [directory for directory in os.listdir(
        path) if os.path.isdir(directory)]
    reg_string_list = []
    reg_string_list.append(reg_string_dir)
    perform_regex_rename_on_files(reg_string_list, path, dirs)


def perform_regex_replacement_on_files(reg_string_list, path=None, files=None):

    if path is None:
        path = os.getcwd()
    if files is None:
        files = os.listdir(path)

    for file in files:

        with open(os.path.join(path, file), "r", encoding="utf-8") as f1:
            content = f1.read()
        for regex in reg_string_list:
            content = re.sub(regex[0], regex[1], content)
        with open(os.path.join(path, file), "w", encoding="utf-8") as f:
            f.write(content)


def perform_regex_replacement_on_files_tree(reg_string_list, path=None):

    if path is None:
        path = os.getcwd()

    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)

            with open(file_path, "r", encoding="utf-8") as f1:
                content = f1.read()

            new_content = content
            for regex in reg_string_list:
                new_content = re.sub(regex[0], regex[1], new_content)

            if new_content != content:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(new_content)


def perform_regex_rename_on_files(reg_string_list, path=None, files=None):
    if path is None:
        path = os.getcwd()
    if files is None:
        files = os.listdir(path)

    for file in files:
        for reg_string in reg_string_list:
            match = re.search(reg_string[0], file)
            if match is not None:
                new_file = re.sub(reg_string[0], reg_string[1], file)
                try:
                    os.rename(file, new_file)
                    print(f"Renamed '{file}' to '{new_file}'")
                except OSError as e:
                    print(f"Error renaming '{file}' to '{new_file}': {e}")


def md_note_process(num=0, head_num=1):
    import md_helper
    operations = {
        1: remove_back_matter_and_copy_code,
        2: degrade_markdown_by_head_number,
        3: md_helper.retrieve_document_summary_info,

    }

    if num in operations:
        if num == 2:
            operations[num](head_num)
        else:
            operations[num]()
    elif num == 0:
        print("Available operations:")
        for num, func in operations.items():
            print(f"{num}: {func.__name__}")
    else:
        raise ValueError("Invalid operation number.")


def degrade_markdown_by_head_number(head_number):
    import md_helper
    import pyperclip
    content = pyperclip.paste()
    TR_MODE = 1
    highest_head_level = md_helper.get_highest_head_level(content)
    # highest_head_level=3
    if TR_MODE:
        print("highest_head_level: ", highest_head_level)
        print("head_number: ", head_number)
    if highest_head_level < head_number:
        content = md_helper.downgrade_heads(
            content, head_number+1-highest_head_level)
        pyperclip.copy(content)


def remove_back_matter_and_copy_code(directory_path=None):

    if directory_path is None:
        directory_path = os.getcwd()

    files_md = [f for f in os.listdir(directory_path) if f.endswith('.md')]

    reg_string_list = []

    reg_Back_matter_template = [r"---\n\n- created:.+\n- source: .+", r""]
    reg_string_list.extend([reg_Back_matter_template])
    reg_string_copy_code = [r"```\n(.+)Copy code", r"```\1\n"]
    reg_string_list.extend([reg_string_copy_code])
    perform_regex_replacement_on_files(
        reg_string_list, directory_path, files_md)


def wiki_note_process(num=0):
    operations = {
        1: remove_wiki_edit_link,
        2: remove_wiki_equation_svg,


    }

    if num in operations:
        operations[num]()
    elif num == 0:
        print("Available operations:")
        for num, func in operations.items():
            print(f"{num}: {func.__name__}")
    else:
        raise ValueError("Invalid operation number.")


def remove_wiki_edit_link(directory_path=None):

    if directory_path is None:
        directory_path = os.getcwd()

    files_md = [f for f in os.listdir(directory_path) if f.endswith('.md')]

    reg_string_list = []

    reg_wiki_edit_link = [
        r'\\\[\[edit\]\(https://en\.wikipedia\.org/w/index\.php\?title=.+ "Edit section: (.+)"\)\\\]', r""]
    reg_string_list.extend([reg_wiki_edit_link])

    perform_regex_replacement_on_files(
        reg_string_list, directory_path, files_md)


def remove_wiki_equation_svg(directory_path=None):
    if directory_path is None:
        directory_path = os.getcwd()

    files_md = [f for f in os.listdir(directory_path) if f.endswith('.md')]

    reg_string_list = []

    reg_wiki_equation_svg = [r'!\[([^\]]+)\]\([A-Za-z0-9]+\.svg\)', r"$\1$"]

    reg_string_list.extend([reg_wiki_equation_svg])

    perform_regex_replacement_on_files(
        reg_string_list, directory_path, files_md)


def vid_note_process(num=0):
    operations = {
        1: init_note,
        2: generate_vid_notes_with_timeline_from_text_summary,
        3: generate_vid_notes_with_timeline_from_timestamps,
        4: convert_md_vid_link_to_html,
        5: convert_md_vid_link_to_html_tree,


    }

    if num in operations:
        operations[num]()
    elif num == 0:
        print("Available operations:")
        for num, func in operations.items():
            print(f"{num}: {func.__name__}")
    else:
        raise ValueError("Invalid operation number.")


def init_note(current_dir=None):

    import pyperclip
    TR_MODE = 1
    # Get content from clipboard
    content = pyperclip.paste()
    reg_content_to_current_topic = [r"\d{1,3}_(.+)\.mp4", r"\1"]
    match = re.search(reg_content_to_current_topic[0], content)
    if match:
        current_topic = re.sub(
            reg_content_to_current_topic[0], reg_content_to_current_topic[1], content)
    else:
        reg_content_to_current_topic = [r"(.+)\.mp4", r"\1"]
        match = re.search(reg_content_to_current_topic[0], content)
        if match:
            current_topic = re.sub(
                reg_content_to_current_topic[0], reg_content_to_current_topic[1], content)
        else:
            current_topic = content
    if TR_MODE == 1:
        print("current_topic: ", current_topic)
    if current_dir is None:
        current_dir = os.getcwd()

    # Check for existing serial numbers (first three digits of filenames)
    serial_numbers = [f[:3] for f in os.listdir(current_dir) if os.path.isfile(
        os.path.join(current_dir, f)) and f[:3].isdigit()]

    # Generate filename
    if serial_numbers:
        max_serial_number = max(serial_numbers)

        note_file = str(int(max_serial_number) + 1).zfill(3) + \
            "_"+current_topic+".md"

    else:
        note_file = "001"+"_"+current_topic+".md"
    if TR_MODE == 1:
        print("note_file: ", note_file)

    # Add the filename to the current_dir
    note_file_path = os.path.join(current_dir, note_file)
    if not os.path.exists(note_file_path):
        create_file(note_file_path)
    sub_topic1_to_sub_topicn_folder_list = []
    sub_topic1_to_sub_topicn_folder_list.append(note_file[:-3])
    # sub_topic1_to_sub_topicn_folder_list.append(os.path.basename(current_dir))

    note_assets_dir_path = get_note_assets_dir_path(
        sub_topic1_to_sub_topicn_folder_list, current_dir)
    if TR_MODE == 1:
        print("note_assets_dir_path: ", note_assets_dir_path)
    create_file_subtitle_summary_gpt_md(note_assets_dir_path)

    Topic, sub_topic1 = get_Topic_in_kg(TR_MODE)

    if Topic is None:
        raise ValueError("Topic is None")
    bvids_origin_topic_path = get_bvids_origin_topic_path(Topic, TR_MODE)
    flag_search_sub_topic1 = get_flag_search_sub_topic1_in_bvids_origin_topic_path()
    if flag_search_sub_topic1:
        dirs = [d for d in os.listdir(bvids_origin_topic_path) if os.path.isdir(
            os.path.join(bvids_origin_topic_path, d))]
        if TR_MODE:
            print("dirs:", dirs)
        reg_string = r"\d{1,3}_"+sub_topic1
        flag_find_sub_topic = False
        for dir in dirs:
            if re.match(reg_string, dir):
                bvids_origin_topic_path = os.path.join(
                    bvids_origin_topic_path, dir)
                flag_find_sub_topic = True
                break
        if not flag_find_sub_topic:
            raise Exception("sub topic not found")
    # RUGUO MATCH COPY
    files_srt = [f for f in os.listdir(
        bvids_origin_topic_path) if f.endswith('.srt')]
    if TR_MODE:
        print("files_srt:", files_srt)
    reg_srt_string_current_topic = [
        r'(\d{1,3}_|)'+current_topic+r'(.+)\.srt', r'']
    flag_one_by_one = get_flag_one_by_one()
    for file_srt in files_srt:
        match = re.match(reg_srt_string_current_topic[0], file_srt)
        flag_find_match = False
        if match:
            flag_find_match = True
            # copy srt to note_assets_dir_path
            new_srt_name = note_file[:-3]+match.group(2)+".md"
            src_srt_file_path = os.path.join(bvids_origin_topic_path, file_srt)
            des_srt_file_path = os.path.join(
                note_assets_dir_path, new_srt_name)
            shutil.copy(src_srt_file_path, des_srt_file_path)
    if not flag_find_match:
        if flag_one_by_one:
            file_srt = files_srt[0]
            src_srt_file_path = os.path.join(
                bvids_origin_topic_path, file_srt)
            des_srt_file_path = os.path.join(
                note_assets_dir_path, file_srt[:-4]+".md")
            shutil.copy(src_srt_file_path, des_srt_file_path)

    srt_format_for_gpt_input(note_assets_dir_path)
    # todo generate prompt


def srt_format_for_gpt_input(directory_path=None):
    if directory_path is None:
        directory_path = os.getcwd()

    files_md = [f for f in os.listdir(directory_path) if f.endswith('.md')]

    reg_string_list = []
    reg_string1 = [
        r'\d{1,3}\n(\d{1,2}:\d{1,2}:\d{1,2},\d{1,3} --> \d{1,2}:\d{1,2}:\d{1,2},\d{1,3})\n(.+)\n(.+)\n\n', r"[[\1],[\2],[\3]]"]
    reg_string_list.extend([reg_string1])
    reg_string2 = [
        r'\d{1,3}\n(\d{1,2}:\d{1,2}:\d{1,2},\d{1,3} --> \d{1,2}:\d{1,2}:\d{1,2},\d{1,3})\n(.+)\n(.+)', r"[[\1],[\2],[\3]]"]
    reg_string_list.extend([reg_string2])
    reg_string2 = [
        r'\d{1,3}\n(\d{1,2}:\d{1,2}:\d{1,2},\d{1,3} --> \d{1,2}:\d{1,2}:\d{1,2},\d{1,3})\n(.+)', r"[[\1],[\2]]"]
    reg_string_list.extend([reg_string2])
    reg_string3 = [r'\n\n', r"\n"]
    reg_string_list.extend([reg_string3])
    perform_regex_replacement_on_files(
        reg_string_list, directory_path, files_md)


def generate_vid_notes_with_timeline_from_text_summary():
    TR_MODE = 1

    origin_current_vid_file_name, current_bvid_destination_file_path, OneDrive_KG_current_note_directory_path = move_origin_vid_to_destination(
        TR_MODE)
    current_bvid_name = get_current_bvid_name()
    if TR_MODE:
        print("current_bvid_name:", current_bvid_name)

    md_show_url, md_url = vid_path_2_md_vid_link(
        current_bvid_destination_file_path, current_bvid_name)
    current_vid_md_link_content = '\n\n'+md_url+'\n'+md_show_url+'\n\n'
    if TR_MODE:
        print("md_show_url:", md_show_url)
        print("md_url:", md_url)
    convert_chatgpt_summary_text_to_one_line_summary()
    # output_dir, file_summary = convert_subtitle_and_summary_to_markdown_vid_timeline(
    #     md_show_url)
    output_dir, file_summary = convert_gpt_summary_to_markdown_vid_timeline(
        md_show_url)
    file_summary_path = os.path.join(output_dir, file_summary)
    note_name = get_note_vid_name()
    if TR_MODE:
        print("note_name:", note_name)
    if not os.path.exists(os.path.join(OneDrive_KG_current_note_directory_path, note_name)):
        # print(os.path.join(OneDrive_KG_current_note_directory_path, note_name),"is note exists")
        # raise Exception("note not found")
        with open(os.path.join(OneDrive_KG_current_note_directory_path, note_name), "w", encoding="utf-8") as f:
            pass

    merge_all_content_into_md_note_file(note_name, file_summary_path, origin_current_vid_file_name,
                                        current_vid_md_link_content, OneDrive_KG_current_note_directory_path)
    convert_md_vid_link_to_html(OneDrive_KG_current_note_directory_path)


def get_bassets_keyword_path(current_dir=None, key_word="mc_1683793602"):
    '''
    kg and bkg 中的 bassets path
    '''
    TR_MODE = 1
    if current_dir is None:
        current_dir = os.getcwd()
    keyword_sub_topic1_to_sub_topicn_folder_list = []

    keyword_sub_topic1_to_sub_topicn_folder_list.append(
        os.path.basename(current_dir))
    current_dir = get_parent_dir(current_dir)
    while True:

        if 'assets' in os.listdir(current_dir):
            keyword_sub_topic1_to_sub_topicn_folder_list.reverse()

            keyword_sub_topic1_to_sub_topicn_folder_list.insert(1, key_word)
            return keyword_sub_topic1_to_sub_topicn_folder_list, current_dir

        else:
            keyword_sub_topic1_to_sub_topicn_folder_list.append(
                os.path.basename(current_dir))
            current_dir = get_parent_dir(current_dir)


def get_kg_assets_root(current_dir=None):
    '''

    '''
    TR_MODE = 1
    if current_dir is None:
        current_dir = os.getcwd()
    sub_topic1_to_sub_topicn_folder_list = []

    while True:

        if 'assets' in os.listdir(current_dir):
            sub_topic1_to_sub_topicn_folder_list.reverse()

            return sub_topic1_to_sub_topicn_folder_list, current_dir

        else:
            sub_topic1_to_sub_topicn_folder_list.append(
                os.path.basename(current_dir))
            current_dir = get_parent_dir(current_dir)


def get_kg_bassets_folder_keyword():
    TR_MODE = 1
    sub_topic1_to_sub_topicn_folder_list, OneDrive_KG_note_root_directory_path = get_kg_assets_root()

    if TR_MODE:
        print("Folder list:", sub_topic1_to_sub_topicn_folder_list)
        print("OneDrive KG root directory_path:",
              OneDrive_KG_note_root_directory_path)
    OneDrive_KG_assets_directory_path = os.path.join(
        OneDrive_KG_note_root_directory_path, "assets")
    if TR_MODE:
        print("OneDrive KG assets directory_path:",
              OneDrive_KG_assets_directory_path)
    dirs = [directory for directory in os.listdir(OneDrive_KG_assets_directory_path) if os.path.isdir(
        os.path.join(OneDrive_KG_assets_directory_path, directory))]
    if TR_MODE:
        print("dirs:", dirs)
    reg_string = [r".+_\d{10}", r"\1"]
    for dir in dirs:
        match = re.search(reg_string[0], dir)
        if match:
            if TR_MODE:
                print("match.group(0):", match.group(0))
            keyword_path = os.path.join(OneDrive_KG_assets_directory_path, dir)
            if TR_MODE:
                print("keyword_path:", keyword_path)
            return match.group(0), keyword_path


def get_b_KG_directory_path(path=None):
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
        # print(path_b_assets)
        return path_b_assets


def get_bvids_destination_long(sub_topic1_to_sub_topicn_folder_list, BaiduSyncdisk_assets_root):
    path_temp = BaiduSyncdisk_assets_root
    for i in range(len(sub_topic1_to_sub_topicn_folder_list)-1):
        path_temp = os.path.join(
            path_temp, sub_topic1_to_sub_topicn_folder_list[i])

        if not os.path.exists(path_temp):
            os.makedirs(path_temp)
    return path_temp


def get_bvid_reg_string(sub_topic1_to_sub_topicn_folder_list, TR_MODE=0):

    # sub_topic=sub_topic1_to_sub_topicn_folder_list[-2].split("_")[-2]+" "+sub_topic1_to_sub_topicn_folder_list[-2].split("_")[-1]
    # sub_topic=sub_topic1_to_sub_topicn_folder_list[-2].split("_")[-1]
    reg_sub = [r'\d{3}_(.+)', r'\1']

    match = re.search(reg_sub[0], sub_topic1_to_sub_topicn_folder_list[-2])
    if match:
        sub_topic1 = re.sub(reg_sub[0], reg_sub[1],
                            sub_topic1_to_sub_topicn_folder_list[-2])
        sub_topic1.replace("_", " ")
    else:
        raise Exception("sub_topic1 not found")
    if TR_MODE:
        print("Sub topic1:", sub_topic1)
    current_topic = sub_topic1_to_sub_topicn_folder_list[-1].split("_")[-1]
    if TR_MODE:
        print("Current topic:", current_topic)
    bvid_reg_string = current_topic+r'(( - )|(- - ))'+sub_topic1+r'\.mp4'
    if TR_MODE:
        print("bvid_reg_string:", bvid_reg_string)
    bvid_srt_reg_string = current_topic + \
        r'(( - )|(- - ))'+sub_topic1+r'(\.en|\.en.+)'+r'\.srt'
    return bvid_reg_string, bvid_srt_reg_string


def get_bvids_origin_topic_path(Topic, TR_MODE=0):
    # bvids_origin_topic_path = get_bvids_origin_topic_path(BaiduSyncdisk_assets_root)
    # bvids_origin_topic_path = r"C:\BaiduSyncdisk\Multivariable_calculus_Khan_Academy_youtube"
    # bvids_origin_topic_path=r'C:\BaiduSyncdisk\First Principles of Computer Vision Specialization\Features and Boundaries'
    bvids_origin_topic_path = r'C:\BaiduSyncdisk\00_MOOC_b'
    # bvids_origin_topic_path=r'C:\BaiduSyncdisk\deep'
    # bvids_origin_topic_path=r'C:\BaiduSyncdisk\Introduction'

    if Topic is None:
        raise Exception("Topic is None")
    bvids_origin_topic_path = os.path.join(
        bvids_origin_topic_path, Topic)
    if TR_MODE:
        print("bvids_origin_topic_path:", bvids_origin_topic_path)
    # if os.path.basename(bvids_origin_topic_path) != Topic:
    #     print("bvids_origin_topic_path:", bvids_origin_topic_path)
    #     print("Topic:", Topic)

    #     raise Exception("Topic name not match")
    return bvids_origin_topic_path


def get_Topic_in_kg(TR_MODE=0):
    assets_sub_topic1_to_sub_topicn_folder_list, OneDrive_KG_note_root_directory_path = get_kg_assets_root()
    if TR_MODE:
        print("assets_sub_topic1_to_sub_topicn_folder_list:",
              assets_sub_topic1_to_sub_topicn_folder_list)
        print("OneDrive KG root directory_path:",
              OneDrive_KG_note_root_directory_path)
    Topic = os.path.basename(OneDrive_KG_note_root_directory_path)
    if TR_MODE:
        print("Topic:", Topic)
    num_topic = len(assets_sub_topic1_to_sub_topicn_folder_list)
    reg_sub1 = [r'\d{3}_(.+)', r'\1']
    if num_topic < 1:
        sub_topic1 = None
    elif num_topic >= 1:
        sub_topic1 = assets_sub_topic1_to_sub_topicn_folder_list[0]
        match = re.search(reg_sub1[0], sub_topic1)
        if match:
            sub_topic1 = re.sub(reg_sub1[0], reg_sub1[1], sub_topic1)
            if TR_MODE:
                print("sub_topic1:", sub_topic1)

    return Topic, sub_topic1


def get_Topic_in_kg_assets(TR_MODE=0):
    assets_sub_topic1_to_sub_topicn_folder_list, OneDrive_KG_note_root_directory_path = get_kg_assets_root()
    if TR_MODE:
        print("assets_sub_topic1_to_sub_topicn_folder_list:",
              assets_sub_topic1_to_sub_topicn_folder_list)
        print("OneDrive KG root directory_path:",
              OneDrive_KG_note_root_directory_path)
    Topic = os.path.basename(OneDrive_KG_note_root_directory_path)
    if TR_MODE:
        print("Topic:", Topic)
    num_topic = len(assets_sub_topic1_to_sub_topicn_folder_list)
    reg_sub1 = [r'\d{3}_(.+)', r'\1']
    if num_topic <= 1:
        raise Exception("num_topic<=1")
    elif num_topic == 2:
        sub_topic1 = None

    elif num_topic >= 3:

        match = re.search(
            reg_sub1[0], assets_sub_topic1_to_sub_topicn_folder_list[1])
        if match:
            sub_topic1 = re.sub(reg_sub1[0], reg_sub1[1],
                                assets_sub_topic1_to_sub_topicn_folder_list[1])
            if TR_MODE:
                print("sub_topic1:", sub_topic1)
        else:
            raise Exception("sub_topic1 not found")

    current_topic = assets_sub_topic1_to_sub_topicn_folder_list[-1]
    current_topic = re.sub(reg_sub1[0], reg_sub1[1], current_topic)
    return Topic, sub_topic1, current_topic


def get_flag_search_sub_topic1_in_bvids_origin_topic_path(TR_MODE=0):
    flag_search_sub_topic1 = False
    return flag_search_sub_topic1


def get_flag_one_by_one(TR_MODE=0):
    flag_one_by_one = True
    return flag_one_by_one


def move_origin_vid_to_destination(TR_MODE=0):

    flag_one_by_one = get_flag_one_by_one()
    if TR_MODE:
        print("flag_one_by_one:", flag_one_by_one)
    flag_search_sub_topic1 = get_flag_search_sub_topic1_in_bvids_origin_topic_path()
    key_word, key_word_path = get_kg_bassets_folder_keyword()
    sub_topic1_to_sub_topicn_folder_list, OneDrive_KG_note_root_directory_path = get_bassets_keyword_path(
        key_word=key_word)
    # sub_topic1_to_sub_topicn_folder_list, OneDrive_KG_note_root_directory_path = get_bassets_keyword_path(key_word="NN_1687967434")
    origin_current_vid_file_name = ""
    # sub_topic1_to_sub_topicn_folder_list, OneDrive_KG_note_root_directory_path = get_kg_assets_root()
    Topic, sub_topic1, current_topic = get_Topic_in_kg_assets(TR_MODE)

    if TR_MODE:
        print("Folder list:", sub_topic1_to_sub_topicn_folder_list)
        print("OneDrive KG root directory_path:",
              OneDrive_KG_note_root_directory_path)

    BaiduSyncdisk_KG_note_root_directory_path = get_b_KG_directory_path(
        OneDrive_KG_note_root_directory_path)
    if TR_MODE:
        print("BaiduSyncdisk assets root _directory_path:",
              BaiduSyncdisk_KG_note_root_directory_path)

    bvids_origin_topic_path = get_bvids_origin_topic_path(
        Topic, TR_MODE=TR_MODE)

    if flag_search_sub_topic1:
        dirs = [d for d in os.listdir(bvids_origin_topic_path) if os.path.isdir(
            os.path.join(bvids_origin_topic_path, d))]
        if TR_MODE:
            print("dirs:", dirs)
        reg_string = r"\d{1,3}_"+sub_topic1
        flag_find_sub_topic = False
        for dir in dirs:
            if re.match(reg_string, dir):
                bvids_origin_topic_path = os.path.join(
                    bvids_origin_topic_path, dir)
                flag_find_sub_topic = True
                break
        if not flag_find_sub_topic:
            raise Exception("sub topic not found")
    files = [f for f in os.listdir(bvids_origin_topic_path) if os.path.isfile(
        os.path.join(bvids_origin_topic_path, f)) and f.endswith(".mp4")]
    files.sort()
    if TR_MODE:
        print("Files:", files)
    OneDrive_KG_current_note_directory_path = get_OneDrive_KG_note_path(
        OneDrive_KG_note_root_directory_path, sub_topic1_to_sub_topicn_folder_list)

    if TR_MODE:
        print("OneDrive KG note directory_path:",
              OneDrive_KG_current_note_directory_path)
    current_bvid_name = get_current_bvid_name()
    if TR_MODE:
        print("current_bvid_name:", current_bvid_name)
    serial_number = current_bvid_name[:3]
    if TR_MODE:
        print("serial_number:", serial_number)
    bvids_destination_directory_path = get_bvids_destination_long(
        sub_topic1_to_sub_topicn_folder_list, BaiduSyncdisk_KG_note_root_directory_path)
    if TR_MODE:
        print("bvids_destination_directory_path:",
              bvids_destination_directory_path)
    # bvid_reg_string = r'.+\(P\d{1,3}\. \d{1,3}\.\d{1,3}\.\d{1,3}(.+)\)\.mp4'

    current_bvid_destination_file_path = os.path.join(
        bvids_destination_directory_path, current_bvid_name)
    if flag_one_by_one:

        if not os.path.exists(current_bvid_destination_file_path):
            vid_name_origin = files[0]
        # origin_current_vid_file_name = "\n"+re.sub(bvid_reg_string, r'\1', vid_name_origin)
            origin_current_vid_file_name = vid_name_origin
            os.rename(os.path.join(bvids_origin_topic_path,
                      vid_name_origin), current_bvid_destination_file_path)
        files_srt_dest = [f for f in os.listdir(bvids_destination_directory_path) if os.path.isfile(
            os.path.join(bvids_destination_directory_path, f)) and f.endswith(".srt")]
        current_bsrt_name = current_bvid_name[:-4]+".srt"
        if TR_MODE:
            print("current_bsrt_name:", current_bsrt_name)
        current_bsrt_name_en = current_bvid_name[:-4]+".en.srt"
        if TR_MODE:
            print("current_bsrt_name_en:", current_bsrt_name_en)
        current_bsrt_file_path = os.path.join(
            bvids_destination_directory_path, current_bsrt_name)
        current_bsrt_file_path_en = os.path.join(
            bvids_destination_directory_path, current_bsrt_name_en)
        if (not os.path.exists(current_bsrt_file_path)) and (not os.path.exists(current_bsrt_file_path_en)):

            srt_name_front = vid_name_origin[:-4]

            reg_string_srt = r"^"+srt_name_front+r"(.+)\.srt$"
            files_srt = [f for f in os.listdir(bvids_origin_topic_path) if os.path.isfile(
                os.path.join(bvids_origin_topic_path, f)) and f.endswith(".srt")]
            for file_srt in files_srt:
                match = re.search(reg_string_srt, file_srt)
                if match:
                    srt_name_origin = file_srt

                    new_srt_name = current_bvid_name[:-4]+match.group(1)+".srt"
                    if TR_MODE:
                        print("srt_name_origin:", srt_name_origin)
                        print("new_srt_name:", new_srt_name)
                    new_srt_file_path = os.path.join(
                        bvids_destination_directory_path, new_srt_name)
                    os.rename(os.path.join(
                        bvids_origin_topic_path, srt_name_origin), new_srt_file_path)
                else:
                    reg_string_srt2 = r"^"+srt_name_front+r"\.srt$"
                    match = re.search(reg_string_srt2, file_srt)
                    if match:
                        srt_name_origin = file_srt

                        new_srt_name = current_bvid_name[:-4]+".srt"
                        if TR_MODE:
                            print("srt_name_origin:", srt_name_origin)
                            print("new_srt_name:", new_srt_name)
                        new_srt_file_path = os.path.join(
                            bvids_destination_directory_path, new_srt_name)
                        os.rename(os.path.join(
                            bvids_origin_topic_path, srt_name_origin), new_srt_file_path)

    else:
        bvid_reg_string, bvid_srt_reg_string = get_bvid_reg_string(
            sub_topic1_to_sub_topicn_folder_list, TR_MODE)
        flag_match = 0
        for file in files:
            match = re.search(bvid_reg_string, file)
            if match:
                flag_match = 1
                vid_name_origin = file
                if TR_MODE:
                    print("vid_name_origin:", vid_name_origin)
                    print(match.group(0))
                break

        if flag_match == 0 and (not os.path.exists(current_bvid_destination_file_path)):
            raise ValueError("No match found.")
        if not os.path.exists(current_bvid_destination_file_path):

            os.rename(os.path.join(bvids_origin_topic_path,
                      vid_name_origin), current_bvid_destination_file_path)

        files_srt = [f for f in os.listdir(bvids_origin_topic_path) if os.path.isfile(
            os.path.join(bvids_origin_topic_path, f)) and f.endswith(".srt")]
        for file_srt in files_srt:
            match = re.search(bvid_srt_reg_string, file_srt)
            if match:
                new_srt_name = current_bvid_name[:-4]+".srt"
                new_srt_path = os.path.join(
                    bvids_destination_directory_path, new_srt_name)
                if not os.path.exists(new_srt_path):
                    os.rename(os.path.join(
                        bvids_origin_topic_path, file_srt), new_srt_path)
    return origin_current_vid_file_name, current_bvid_destination_file_path, OneDrive_KG_current_note_directory_path


def merge_all_content_into_md_note_file(note_name, file_summary_path, origin_current_vid_file_name, current_vid_md_link_content, OneDrive_KG_current_note_directory_path):
    with open(os.path.join(OneDrive_KG_current_note_directory_path, note_name), "r", encoding="utf-8") as f:
        current_note_origin_content = f.read()
    with open(file_summary_path, "r", encoding="utf-8") as f:
        current_vid_summary = f.read()
    with open(os.path.join(OneDrive_KG_current_note_directory_path, note_name), "w", encoding="utf-8") as f:
        f.write(current_note_origin_content+origin_current_vid_file_name +
                current_vid_md_link_content+current_vid_summary)


def convert_chatgpt_summary_text_to_one_line_summary(directory_path=None):
    if directory_path is None:
        directory_path = os.getcwd()

    files_md = [f for f in os.listdir(directory_path) if f.endswith('.md')]

    reg_string_list = []
    reg_string1 = [
        r'Section \d{1,2}: (.+)\n{1,2}(Start|Start Timestamp): (\d{1,2}:\d{1,2})\nSummary(: |:\n)(.+)', r"- \1 (\3) \5"]
    reg_string_list.extend([reg_string1])
    reg_string2 = [
        r'Title: (.+)\nStart Timestamp: (\d{1,2}:\d{1,2})\nSummary(: |:\n)(.+)', r"- \1 (\2) \4"]
    reg_string_list.extend([reg_string2])
    reg_string2 = [
        r'Title: (.+)\nStart Timestamp: \d{1,2}:(\d{1,2}:\d{1,2}),\d{1,3}\nSummary(: |:\n)(.+)', r"- \1 (\2) \4"]
    reg_string_list.extend([reg_string2])

    perform_regex_replacement_on_files(
        reg_string_list, directory_path, files_md)


def convert_md_vid_link_to_html(directory_path=None):
    if directory_path is None:
        directory_path = os.getcwd()

    files_md = [f for f in os.listdir(directory_path) if f.endswith('.md')]

    reg_string_list = []

    reg_string2 = [r'(!\[\]|!\[.+\])\((file:///.+(\.mp4|\.mp4#t=.+))\)',
                   r'<video src="\2" controls></video>']
    reg_string_list.extend([reg_string2])

    perform_regex_replacement_on_files(
        reg_string_list, directory_path, files_md)


def convert_md_vid_link_to_html_tree(directory_path=None):
    if directory_path is None:
        directory_path = os.getcwd()

    reg_string_list = []

    reg_string2 = [r'(!\[\]|!\[.+\])\((file:///.+(\.mp4|\.mp4#t=.+))\)',
                   r'<video src="\2" controls></video>']
    reg_string_list.extend([reg_string2])

    perform_regex_replacement_on_files_tree(reg_string_list, directory_path)


def generate_vid_notes_with_timeline_from_timestamps():
    TR_MODE = 1

    origin_current_vid_file_name, current_bvid_destination_file_path, OneDrive_KG_current_note_directory_path = move_origin_vid_to_destination(
        TR_MODE)
    current_bvid_name = get_current_bvid_name(
        current_bvid_destination_file_path)
    md_show_url, md_url = vid_path_2_md_vid_link(
        current_bvid_destination_file_path, current_bvid_name)
    current_vid_md_link_content = '\n\n'+md_url+'\n'+md_show_url+'\n\n'
    if TR_MODE:
        print("md_show_url:", md_show_url)
        print("md_url:", md_url)

    output_dir, file_summary = timestamps_3blue1brown_2_timeline(md_show_url)
    file_summary_path = os.path.join(output_dir, file_summary)
    note_name = get_note_vid_name()
    if TR_MODE:
        print("note_name:", note_name)
    if not os.path.exists(os.path.join(OneDrive_KG_current_note_directory_path, note_name)):
        # print(os.path.join(OneDrive_KG_current_note_directory_path, note_name),"is note exists")
        # raise Exception("note not found")
        with open(os.path.join(OneDrive_KG_current_note_directory_path, note_name), "w", encoding="utf-8") as f:
            pass
    merge_all_content_into_md_note_file(
        note_name, file_summary_path, origin_current_vid_file_name, current_vid_md_link_content)
    convert_md_vid_link_to_html(OneDrive_KG_current_note_directory_path)


def zfill_folder_files(path=None, zfill_num=3):
    if path is None:
        path = os.getcwd()

    files = [f for f in os.listdir(
        path) if os.path.isfile(os.path.join(path, f))]
    for file in files:
        file_name, file_ext = os.path.splitext(file)
        file_name_zfilled = file_name.zfill(zfill_num)
        os.rename(os.path.join(path, file), os.path.join(
            path, file_name_zfilled + file_ext))
    dirs = [f for f in os.listdir(
        path) if os.path.isdir(os.path.join(path, f))]
    for dir in dirs:
        dir_name, dir_ext = os.path.splitext(dir)
        dir_name_zfilled = dir_name.zfill(zfill_num)
        os.rename(os.path.join(path, dir), os.path.join(
            path, dir_name_zfilled + dir_ext))


def os_file_process(num=0):
    operations = {
        1: get_kg_bassets_folder_keyword,
        2: add_timestamp_to_filenames,
        3: get_current_timestamp,
        4: zfill_folder_files,


    }

    if num in operations:
        operations[num]()
    elif num == 0:
        print("Available operations:")
        for num, func in operations.items():
            print(f"{num}: {func.__name__}")
    else:
        raise ValueError("Invalid operation number.")


# def get_prompt_explain_c_cpp():
#     import prompts
#     prompts.get_prompt_explain_c_cpp()


def get_prompts(num=0):
    import prompts
    operations = {
        1: prompts.video_summarization_expert_one,
        2: prompts.get_prompt_explain_c_cpp,
        3: prompts.chatbot_prompt_expert,
        4: prompts.Translate_Chinese_sentence_into_function_name,


    }

    if num in operations:
        operations[num]()
    elif num == 0:
        print("Available operations:")
        for num, func in operations.items():
            print(f"{num}: {func.__name__}")
    else:
        raise ValueError("Invalid operation number.")


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
    parser.add_argument('-hn', '--head_num', type=int, default=r'1',
                        help='input head_num to pass to the function')
    parser.add_argument('-gt', '--get_timestamp',
                        action='store_true', help='call get_current_timestamp')
    parser.add_argument('-at', '--add_timestamp', action='store_true',
                        help='call add_timestamp_to_filenames')

    parser.add_argument('-mdx', '--mdx2md',
                        action='store_true', help='call mdx2md')
    parser.add_argument('-oaf', '--open_b_assets_folder',
                        action='store_true', help='call open_b_assets_folder')

    parser.add_argument('-md', '--md_note_process',
                        action='store_true', help='call md_note_process')
    parser.add_argument('-wiki', '--wiki_note_process',
                        action='store_true', help='call wiki_note_process')
    parser.add_argument('-vid', '--vid_note_process',
                        action='store_true', help='call vid_note_process')
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
                        help='call create_file_subtitle_summary_gpt_md')
    parser.add_argument('-h2m', '--html2md',
                        action='store_true', help='call html2md')
    parser.add_argument('-h2m2', '--html2md2',
                        action='store_true', help='call html2md2')

    parser.add_argument('-h2mt', '--html2md_tree',
                        action='store_true', help='call html2md_tree')
    parser.add_argument('-m2hl', '--convert_md_vid_link_to_html',
                        action='store_true', help='call convert_md_vid_link_to_html')
    parser.add_argument('-init', '--init_note',
                        action='store_true', help='call init_note')
    parser.add_argument('-test', '--test',
                        action='store_true', help='call test')
    parser.add_argument('-zbp', '--zhi_book_process',
                        action='store_true', help='call zhi_book_process')
    parser.add_argument('-osf', '--os_file_process',
                        action='store_true', help='call os_file_process')
    parser.add_argument('-vls', '--full_fill_vid_link_2_summary',
                        action='store_true', help='call full_fill_vid_link_2_summary')
    parser.add_argument('-gp', '--get_prompts',
                        action='store_true', help='call get_prompts')
    # parse the command-line arguments
    args = parser.parse_args()

    # call the appropriate function based on the arguments
    if args.md_note_process:
        md_note_process(args.input_int, args.head_num)
    elif args.wiki_note_process:
        wiki_note_process(args.input_int)
    elif args.vid_note_process:
        vid_note_process(args.input_int)
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

    elif args.create_imgs_folder:
        create_directory_assets_imgs()
    elif args.creat_concept_folder:
        create_directory_assets_concept_structure()
    elif args.creat_subtitle_summary:
        create_file_subtitle_summary_gpt_md()
    elif args.html2md:
        html2md()
    elif args.html2md2:
        html2md2()
    elif args.html2md_tree:
        html2md_tree()
    elif args.convert_md_vid_link_to_html:
        convert_md_vid_link_to_html()
    elif args.init_note:
        init_note()
    elif args.full_fill_vid_link_2_summary:
        full_fill_vid_link_2_summary()
    elif args.test:
        test(args.input_int)

    elif args.zhi_book_process:
        zhi_book_process(args.input_int)
    elif args.os_file_process:
        os_file_process(args.input_int)
    elif args.get_prompts:
        get_prompts(args.input_int)
    else:
        print("Invalid argument")


if __name__ == "__main__":
    main()
