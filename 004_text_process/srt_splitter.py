import re
import sys

def read_srt_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
        blocks = content.strip().split("\n\n")
        return blocks

def split_blocks(blocks, max_length):
    chunks = []
    current_chunk = ""

    for block in blocks:
        if len(current_chunk + block) > max_length:
            chunks.append(current_chunk.strip())
            current_chunk = ""

        current_chunk += block + "\n\n"

    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks

def add_explanation(chunks):
    explained_chunks = []
    explanation = "This is a chunk of the SRT file for ChatGPT:\n\n"

    for chunk in chunks:
        explained_chunk = explanation + chunk
        explained_chunks.append(explained_chunk)

    return explained_chunks

def write_chunks(chunks, output_folder):
    for index, chunk in enumerate(chunks, start=1):
        output_path = f"{output_folder}/chunk_{index}.txt"
        with open(output_path, "w", encoding="utf-8") as file:
            file.write(chunk)

def main(file_path, output_folder, max_length=1024):
    blocks = read_srt_file(file_path)
    chunks = split_blocks(blocks, max_length)
    explained_chunks = add_explanation(chunks)
    write_chunks(explained_chunks, output_folder)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python srt_splitter.py <srt_file_path> <output_folder> [<max_length>]")
    else:
        file_path = sys.argv[1]
        output_folder = sys.argv[2]
        max_length = int(sys.argv[3]) if len(sys.argv) > 3 else 1024
        main(file_path, output_folder, max_length)
