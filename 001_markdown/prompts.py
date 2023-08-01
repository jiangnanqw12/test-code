
import pyperclip


def get_prompt_explain_c_cpp():
    prompt_string1 ='''## Exploring Key C/C++ Concepts: A Guide to Understanding and Resources
Please provide a detailed explanation for the following C/C++ concepts that I'll specify. Can you also recommend some comprehensive books or resources to aid my understanding of these concepts
concepts is :
```
'''
    prompt_string2 = '''```
    '''
    combine_strings_with_clipboard(prompt_string1, prompt_string2)

def video_summarization_expert_one():
    prompt_string1 = '''## video summarization expert one
You are a video summarization expert.
I will provide you with complete subtitle information for a video. Your task is to segment this subtitle information into as many sections as possible based on its content.
The summary for each section should include a title, start timestamp, and summary text.
Here is the format in which the subtitle information will be supplied:
```srt
'''
    prompt_string2='''
    ```
Please write in English.And this is the expected output format:
Title:
Start Timestamp:
Summary:
    '''
    combine_strings_with_clipboard(prompt_string1, prompt_string2)

def chatbot_prompt_expert():
    prompt_string1 = '''## chatbot prompt expert

As an AI chatbot prompt expert, could you analyze and provide suggestions to improve the following prompt:
'[
'''
    prompt_string2 = '''
]'
Please provide a final revised version.
'''
    combine_strings_with_clipboard(prompt_string1, prompt_string2)

def Translate_Chinese_sentence_into_function_name():
    prompt_string1 = '''
    ## Translate Chinese sentence into function name
Translate the following Chinese sentence into English and create a snake_case function name based on the translated sentence:
[
'''
    prompt_string2 = '''
]. Your function name should reflect the primary task described in the sentence. Please also provide a brief description of what the function will do
'''
    combine_strings_with_clipboard(prompt_string1, prompt_string2)
def combine_strings_with_clipboard(prompt_string1, prompt_string2):
    string3 = pyperclip.paste()
    final_string = prompt_string1 + string3 + "\n" + prompt_string2
    pyperclip.copy(final_string)
    # print(final_string)
    return final_string
