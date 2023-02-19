
import os
import shutil


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
    f_mindmap_rich = open(cwd + '/mindmap_rich.md', 'w', encoding='utf-8')
    f_mindmap_rich.write(str_mindmap_rich)
    f_mindmap_rich.close()
    f_mindmap_basic = open(cwd + '/mindmap_basic.md', 'w', encoding='utf-8')
    f_mindmap_basic.write(str_mindmap_basic)
    f_mindmap_basic.close()


def create_annotator_4pdf_file(file_name_with_endswith_pdf):
    # get the file name without the .pdf
    file_name_without_pdf = file_name_with_endswith_pdf[:-4]
    # replace the space in the file name with underscore
    file_name_without_space = file_name_without_pdf.replace(' ', '_')
    cwd_after_obsidian_workspace2 = cwd_after_obsidian_workspace.replace(
        " ", "_")
    cwd_after_obsidian_workspace2 = cwd_after_obsidian_workspace2.replace(
        "/", "_")
    cwd_after_obsidian_workspace2 = cwd_after_obsidian_workspace2.replace(
        "=", "_")
    # Traversal the current directory

    f_annotate.write('---\n')
    f_annotate.write("annotate-target: " + cwd_after_obsidian_workspace +
                     "/assets/pdfs/" + file_name_with_endswith_pdf + "\n")
    f_annotate.write("annotate-type: pdf\n")
    f_annotate.write("annotate-image-target: " +
                     cwd_after_obsidian_workspace + "/assets/images\n")
    f_annotate.write("id: " + cwd_after_obsidian_workspace2 +
                     file_name_without_space + "\n")
    f_annotate.write("---\n")


def create_floder(cwd):
    # if in the current folder there is a folder named assets
    if os.path.isdir(cwd + '/assets'):
        pass
    else:
        # make a new folder in the current directory named assets
        os.mkdir(cwd + '/assets')
    if os.path.isdir(cwd + '/assets/images'):
        pass
    else:
        # make a new folder in the assets folder named images
        os.mkdir(cwd + '/assets/images')
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
            # copy the pdf file to the pdfs folder in the assets folder
            shutil.copy(cwd + '/' + file, cwd + '/assets/pdfs/')

            f_annotate = open(
                cwd + '/assets/pdfs/' + file_name_without_pdf + '_annotate.md', 'w', encoding='utf-8')
            create_annotator_4pdf_file(file)
            # print(pdf_file_name)

    make_mindmap_file(cwd)
if __name__ == '__main__':
    main()
