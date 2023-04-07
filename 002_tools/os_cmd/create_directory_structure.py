import os
import argparse
def create_directory_assets_imgs():
    dirs = [
        "assets/imgs",
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

def main():
    # create a parser object
    parser = argparse.ArgumentParser()

    # add arguments for each function
    parser.add_argument('-ci', '--createimgs', action='store_true', help='call create_directory_assets_imgs')
    parser.add_argument('-cc', '--creatconcept', action='store_true', help='call create_directory_assets_concept_structure')

    # parse the command-line arguments
    args = parser.parse_args()

    # call the appropriate function based on the arguments
    if args.createimgs:
        create_directory_assets_imgs()
    elif args.creatconcept:
        create_directory_assets_concept_structure()
    else:
        print("Invalid argument")

if __name__ == "__main__":
    main()