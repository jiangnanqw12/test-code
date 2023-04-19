import time
import os
import argparse
def get_current_timestamp():
    timestamp = int(time.time())
    print(timestamp)
    return timestamp
def add_timestamp_to_filenames():
    current_dir = os.getcwd()
    timestamp = int(time.time())
    print("add_timestamp is : ",timestamp)
    for filename in os.listdir(current_dir):
        if os.path.isfile(os.path.join(current_dir, filename)) and not filename.endswith(".py"):
            filename_without_ext, ext = os.path.splitext(filename)
            new_filename = f"{filename_without_ext}_{timestamp}{ext}"
            os.rename(os.path.join(current_dir, filename), os.path.join(current_dir, new_filename))
def main():
    # create a parser object
    parser = argparse.ArgumentParser()

    # add arguments for each function
    parser.add_argument('-gt', '--get_timestamp', action='store_true', help='call get_current_timestamp')
    parser.add_argument('-at', '--add_timestamp', action='store_true', help='call add_timestamp_to_filenames')

    # parse the command-line arguments
    args = parser.parse_args()

    # call the appropriate function based on the arguments
    if args.get_timestamp:
        get_current_timestamp()
    elif args.add_timestamp:
        add_timestamp_to_filenames()
    else:
        print("Invalid argument")
if __name__ == "__main__":
    main()