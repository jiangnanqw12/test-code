
import os
import shutil
import time
import re


def make_mindmap_file(cwd):
    """Create mindmap files in the given directory."""
    str_mindmap_rich = '''
---
mindmap-plugin: rich
---
# Root
``` json
{"mindData":[[{"id":"4c8a77d7-a9e3-96ca","text":"Root","isRoot":true,"main":true,"x":4000,"y":4000,"isExpand":true,"layout":{"layoutName":"mindmap2","direct":"right"},"stroke":""}]],"induceData":[],"wireFrameData":[],"relateLinkData":[],"calloutData":[]}
'''
str_mindmap_basic = '''
mindmap-plugin: basic
'''

with open(os.path.join(cwd, 'mindmap_rich.md'), 'w', encoding='utf-8') as f_mindmap_rich:
    f_mindmap_rich.write(str_mindmap_rich)

with open(os.path.join(cwd, 'mindmap_basic.md'), 'w', encoding='utf-8') as f_mindmap_basic:
    f_mindmap_basic.write(str_mindmap_basic)
