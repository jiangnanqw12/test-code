import os

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

open_assets_folder()
