import os
import re

root_directory = "project_unzipped/My_Big_Directory"

pattern = r"N[A-Za-z]{3}-\d{5}"

for dirpath, dirnames, filenames in os.walk(root_directory):
    for filename in filenames:
        if filename.endswith(".txt"):  # checks if the file is a text file
            file_path = os.path.join(dirpath, filename)
            with open(file_path, "r", encoding="utf-8") as file:
                matches = re.findall(pattern, test_string)
                for match in matches:
                    print(match)
