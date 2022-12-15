
import os
#get current working directory
cwd = os.getcwd()
#get current folder name
folder_name = os.path.basename(cwd)
#print(folder_name)
folder_name_string= str(folder_name)
#print(folder_name_string)
#if in the current folder there is a folder named assets
if os.path.isdir(cwd+'/assets'):
    pass
else:
    #make a new folder in the current directory named assets
    os.mkdir(cwd+'/assets')
if os.path.isdir(cwd+'/assets/images'):
    pass
else:
    #make a new folder in the assets folder named images
    os.mkdir(cwd+'/assets/images')
if os.path.isdir(cwd+'/assets/pdfs'):
    pass
else:

    os.mkdir(cwd+'/assets/pdfs')
#make a new file in the current directory named mindmap.md
f_mindmap = open(cwd+'/mindmap.md', 'w',encoding='utf-8')
#make a new file in the current directory named annotatae.md
f_annotatae = open(cwd+'/annotatae.md', 'w',encoding='utf-8')
#get all the files in the current directory
files = os.listdir(cwd)
#loop through all the files in the current directory
for file in files:
    #if the file is a pdf file
    if file.endswith('.pdf'):
        # get current pdf file name
        pdf_file_name = os.path.basename(file)
        print(type(file))
        #copy the pdf file to the pdfs folder
        os.system('cp '+cwd+'/'+file+' '+cwd+'/assets/pdfs/'+pdf_file_name)

        #print(pdf_file_name)

f_annotatae.write('---\n')
f_annotatae.write("annotate-target: 111.pdf\n")
f_annotatae.write("annotate-type: pdf\n")
f_annotatae.write("annotate-image-target: /assets/images\n")
f_annotatae.write("id: "+folder_name_string+"\n")
f_annotatae.write("---\n")

str_mindmap = '''
---

mindmap-plugin: rich

---

# Root
``` json
{"mindData":[[{"id":"4c8a77d7-a9e3-96ca","text":"Root","isRoot":true,"main":true,"x":4000,"y":4000,"isExpand":true,"layout":{"layoutName":"mindmap2","direct":"right"},"stroke":""}]],"induceData":[],"wireFrameData":[],"relateLinkData":[],"calloutData":[]}
```
'''
f_mindmap.write(str_mindmap)