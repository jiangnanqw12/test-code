import os
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

def test():
    folder_list, OneDrive_KG_root = get_bvids_path(key_word="mc_1683793602")

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


if __name__ == "__main__":
    test()