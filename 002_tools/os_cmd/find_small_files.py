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

def find_small_files(directory,size=1024):
    filepath_list=[]
    for root, dirs, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            if os.path.isfile(filepath) and os.path.getsize(filepath) < size:
                filepath_list.append(filepath)
                #print(filepath)
    print(f"Total number of files < {size}b: {len(filepath_list)}")
    print("\n")
    print("File list: ",filepath_list)
    print("\n")
def find_zero_files(directory):
    filepath_list=[]
    for root, dirs, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            if os.path.isfile(filepath) and os.path.getsize(filepath) == 0:
                if not filename.endswith('.md'):
                    filepath_list.append(filepath)
                #open_folder_in_windows(root)
                #print(filepath)
    print("Total number of files==0: ",len(filepath_list))
    print("\n")
    n2=0
    for file_path in filepath_list:

        n2+=1
        print(file_path)
        open_folder_in_windows(os.path.dirname(file_path))
    print(n2)
    print("\n")
def find_zero_files_open_it(directory):
    filepath_list=[]
    for root, dirs, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            if os.path.isfile(filepath) and os.path.getsize(filepath) == 0:
                if not filename.endswith('.md'):
                    filepath_list.append(filepath)
                    open_folder_in_windows(root)
                #print(filepath)
    print("Total number of files==0: ",len(filepath_list))
    print("\n")
    print("File list: ",filepath_list)
    print("\n")
if __name__ == '__main__':

    # Example usage:
    find_zero_files('.')
    #find_small_files('.',100)
