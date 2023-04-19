import os
import argparse
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
        "assets/imgs",
        "assets/lectures",
        "assets/paper"
    ]

    for directory in dirs:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"Created directory: {directory}")
        else:
            print(f"Directory already exists: {directory}")

def create_file_subtitle_summary_base_on_chatgpt_md():
    # Create a file named subtitle.md and summary_base_on_chatgpt.md
    with open(os.path.join(os.getcwd(), "subtitle.md"), "w") as f:
        pass
    with open(os.path.join(os.getcwd(), "summary_base_on_chatgpt.md"), "w") as f:
        pass
def main():
    # create a parser object
    parser = argparse.ArgumentParser()

    # add arguments for each function
    parser.add_argument('-ci', '--create_imgs_folder', action='store_true', help='call create_directory_assets_imgs')
    parser.add_argument('-cc', '--creat_concept_folder', action='store_true', help='call create_directory_assets_concept_structure')
    parser.add_argument('-css', '--creat_subtitle_summary', action='store_true', help='call create_file_subtitle_summary_base_on_chatgpt_md')

    # parse the command-line arguments
    args = parser.parse_args()

    # call the appropriate function based on the arguments
    if args.create_imgs_folder:
        create_directory_assets_imgs()
    elif args.creat_concept_folder:
        create_directory_assets_concept_structure()
    elif args.creat_subtitle_summary:
        create_file_subtitle_summary_base_on_chatgpt_md()
    else:
        print("Invalid argument")

if __name__ == "__main__":
    main()