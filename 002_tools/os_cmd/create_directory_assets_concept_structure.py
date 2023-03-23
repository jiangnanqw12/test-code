import os

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

if __name__ == "__main__":
    create_directory_assets_concept_structure()
