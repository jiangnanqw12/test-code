import os
import subprocess


def choco_install_through_config():
    # Get the current working directory
    path_cwd = os.getcwd()
    # Get the script directory
    path_file = os.path.dirname(os.path.abspath(__file__))
    config_location = os.path.join(path_file, "packages.config")
    cmd = [
        'choco',
        'install', config_location,
        "-y",

    ]

    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Subprocess failed with error: {e}")


def main():
    choco_install_through_config()


if __name__ == "__main__":
    main()
