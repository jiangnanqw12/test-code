
import pyperclip


def get_prompt_explain_c_cpp():
    prompt_string1 = '''## Exploring Key C/C++ Concepts: A Guide to Understanding and Resources
Please provide a detailed explanation for the following C/C++ concepts that I'll specify. Can you also recommend some comprehensive books or resources to aid my understanding of these concepts
concepts is :
```\n'''
    prompt_string2 = '''```\n'''
    combine_strings_with_clipboard(prompt_string1, prompt_string2)


def combine_strings_with_clipboard(prompt_string1, prompt_string2):
    string3 = pyperclip.paste()
    final_string = prompt_string1 + string3 + "\n" + prompt_string2
    pyperclip.copy(final_string)
    # print(final_string)
    return final_string
