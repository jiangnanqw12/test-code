
import os
import shutil
import time
import re
def make_mindmap_file(cwd):
    # make a new file in the current directory named mindmap.md

    str_mindmap_rich = '''
---

mindmap-plugin: rich

---

# Root
``` json
{"mindData":[[{"id":"4c8a77d7-a9e3-96ca","text":"Root","isRoot":true,"main":true,"x":4000,"y":4000,"isExpand":true,"layout":{"layoutName":"mindmap2","direct":"right"},"stroke":""}]],"induceData":[],"wireFrameData":[],"relateLinkData":[],"calloutData":[]}
```
'''
    str_mindmap_basic = '''
---

mindmap-plugin: basic

---


'''
    with open(os.path.join(cwd, 'mindmap_rich.md'), 'w', encoding='utf-8') as f_mindmap_rich:
        f_mindmap_rich.write(str_mindmap_rich)

    with open(os.path.join(cwd, 'mindmap_basic.md'), 'w', encoding='utf-8') as f_mindmap_basic:
        f_mindmap_basic.write(str_mindmap_basic)

    # f_mindmap_rich = open(cwd + '/mindmap_rich.md', 'w', encoding='utf-8')
    # f_mindmap_rich.write(str_mindmap_rich)
    # f_mindmap_rich.close()
    # f_mindmap_basic = open(cwd + '/mindmap_basic.md', 'w', encoding='utf-8')
    # f_mindmap_basic.write(str_mindmap_basic)
    # f_mindmap_basic.close()
def make_mindmap_basic_file(cwd,file_name_without_pdf):
    # make a new file in the current directory named mindmap.md


    str_mindmap_basic = '''
---

mindmap-plugin: basic

---


'''


    with open(os.path.join(cwd, file_name_without_pdf+'_mindmap_basic.md'), 'w', encoding='utf-8') as f_mindmap_basic:
        f_mindmap_basic.write(str_mindmap_basic+"# "+file_name_without_pdf)

def remove_chinese_characters(text):

    # 匹配中文字符的正则表达式
    chinese_pattern = re.compile("[\u4e00-\u9fa5]+")

    # 将中文字符替换为空字符串
    result = chinese_pattern.sub("", text)

    return result
def create_annotator_4pdf_file(file_name_with_endswith_pdf,f_annotate,cwd_after_obsidian_workspace):
    # get the file name without the .pdf
    file_name_without_pdf = file_name_with_endswith_pdf[:-4]
    timestamp = int(time.time())
    # replace the space in the file name with underscore
    file_name_without_space = file_name_without_pdf.replace(' ', '_')
    file_name_without_space = remove_chinese_characters(file_name_without_space)
    cwd_after_obsidian_workspace2 = cwd_after_obsidian_workspace.replace(
        " ", "_")
    cwd_after_obsidian_workspace2 = cwd_after_obsidian_workspace2.replace(
        "/", "_")
    cwd_after_obsidian_workspace2 = cwd_after_obsidian_workspace2.replace(
        "=", "_")
    cwd_after_obsidian_workspace2=remove_chinese_characters(cwd_after_obsidian_workspace2)
    # Traversal the current directory

    f_annotate.write('---\n')
    f_annotate.write("annotate-target: " + cwd_after_obsidian_workspace +
                     "/assets/pdfs/" + file_name_with_endswith_pdf + "\n")
    f_annotate.write("annotate-type: pdf\n")
    f_annotate.write("annotate-image-target: " +
                     cwd_after_obsidian_workspace + "/assets/imgs\n")
    f_annotate.write("id: "  +
                     file_name_without_space+"\n")
    f_annotate.write("---\n")


def create_floder(cwd):
    # if in the current folder there is a folder named assets
    if os.path.isdir(cwd + '/assets'):
        pass
    else:
        # make a new folder in the current directory named assets
        os.mkdir(cwd + '/assets')
    if os.path.isdir(cwd + '/assets/imgs'):
        pass
    else:
        # make a new folder in the assets folder named images
        os.mkdir(cwd + '/assets/imgs')
    if os.path.isdir(cwd + '/assets/pdfs'):
        pass
    else:

        os.mkdir(cwd + '/assets/pdfs')

def main():
    # get current working directory
    cwd = os.getcwd()

    # replace all the \ with /
    cwd = cwd.replace('\\', '/')
    # print(cwd)
    obsidian_workspace = "KG/"
    # get cwd after obsidian_workspace
    cwd_after_obsidian_workspace = cwd.split(obsidian_workspace)[1]
    print(cwd_after_obsidian_workspace)
    # get current folder name

    create_floder(cwd)
    # get all the files in the current directory
    files = os.listdir(cwd)
    # loop through all the files in the current directory
    for file in files:
        # if the file is a pdf file
        if file.endswith('.pdf'):
            # get current file name without filename extension
            file_name_without_pdf = file[:-4]
            file_name_without_pdf_without_timestamp=file_name_without_pdf.split("_")[0]
            src_file = os.path.join(cwd, file)
            dest_file = os.path.join(cwd, 'assets', 'pdfs', file)
            if not os.path.isfile(dest_file):
                # copy the pdf file to the pdfs folder in the assets folder
                shutil.copy(src_file, dest_file)
            annotate_file = os.path.join(cwd, 'assets', 'pdfs', f"{file_name_without_pdf}_annotate.md")
            if not os.path.isfile(annotate_file):
                with open(annotate_file, 'w', encoding='utf-8') as f_annotate:
                    create_annotator_4pdf_file(file, f_annotate, cwd_after_obsidian_workspace)
            mindmap_basic_file=os.path.join(cwd, file_name_without_pdf+'_mindmap_basic.md')
            if not os.path.isfile(mindmap_basic_file):
                make_mindmap_basic_file(cwd,file_name_without_pdf)
            # check if there is a file named file_name_without_pdf + '_annotate.md' exists
            # if not os.path.isfile(cwd + '/assets/pdfs/' + file_name_without_pdf + '_annotate.md'):
            #     f_annotate = open(cwd + '/assets/pdfs/' + file_name_without_pdf + '_annotate.md', 'w', encoding='utf-8')
            #     create_annotator_4pdf_file(file,f_annotate,cwd_after_obsidian_workspace)
            # print(pdf_file_name)


if __name__ == '__main__':
    main()
