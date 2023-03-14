import os


def remove_comments_and_whitespace(filename):
    file_extention = filename.split(".")[-1]
    comment_list = [["py", "#"], ["m", "%"], [
        "cpp", "//"], ["c", "//"], ["h", "//"]]
    # get index of comment
    for i in range(len(comment_list)):
        if file_extention in comment_list[i]:
            comment_index = i
            # print(comment_list[comment_index][1])
            break
    comment_str = comment_list[comment_index][1]
    current_path = os.getcwd()
    release_path = os.path.join(current_path, "release")
    if not os.path.exists(release_path):
        os.mkdir(release_path)
    # Open the file in read mode
    with open(filename, 'r', encoding='UTF-8') as file:
        # Read all lines into a list
        lines = file.readlines()

    # Open the file again in write mode
    new_file_name = filename[:-(len(file_extention)+1)] + \
        "_release." + file_extention
    with open(os.path.join(release_path, new_file_name), 'w', encoding='UTF-8') as file:
        # Loop through each line in the list
        for line in lines:

            # Remove leading and trailing whitespace from the line
            line_temp = line.strip()
            # Check if the line is a comment or empty
            if line_temp.startswith(comment_str) or not line_temp:
                # If it is, skip this line
                continue
            if line == "\n":
                continue
            # If it's not a comment or empty, write the line to the file
            if line[-1] != "\n":
                file.write(line + '\n')
            elif line[-1] == "\n":
                file.write(line)


def test_remove_comments_and_whitespace_m():
    file_list = os.listdir(os.getcwd())
    for file in file_list:
        if file.endswith(".m"):
            remove_comments_and_whitespace(file)


if __name__ == '__main__':
    # Call the function
    remove_comments_and_whitespace(
        't.c')
    # test_remove_comments_and_whitespace_m()
