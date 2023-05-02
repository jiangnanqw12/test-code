
import os

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

def open_assets_folder():
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

def main():
    open_assets_folder()


if __name__ == "__main__":
    main()