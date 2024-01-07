import os

root_directory = "project_unzipped/My_Big_Directory"

search_word = "search_word"

for dirpath, dirnames, filenames in os.walk(root_directory):
    for filename in filenames:
        if filename.endswith(".txt"):  # checks if the file is a text file
            file_path = os.path.join(dirpath, filename)
            with open(file_path, "r", encoding="utf-8") as file:
                for line in file:
                    if search_word in line:
                        print(f"'{search_word}' found in {file_path}")
                        break  # assuming you only want to know if the word exists at least once in the file
