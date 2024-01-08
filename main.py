import os
import re
import time
from collections import Counter
from datetime import datetime


def serial_number_finder():
    root_directory = "project_unzipped/My_Big_Directory"
    pattern = r"N[A-Za-z]{3}-\d{5}"
    all_matches = []

    for dirpath, dirnames, filenames in os.walk(root_directory):
        for filename in filenames:
            if filename.endswith(".txt"):
                file_path = os.path.join(dirpath, filename)
                try:
                    with open(file_path, "r", encoding="utf-8") as file:
                        for line in file:
                            matches = re.findall(pattern, line)
                            all_matches.extend(matches)
                except Exception as e:
                    print(f"Error reading file {file_path}: {e}")
    return all_matches


beginning = time.time()
serial_numbers = serial_number_finder()
count = Counter(serial_numbers)
ending = time.time()
# print(serial_numbers)

today_date = datetime.now()
formatted_date = today_date.strftime("%m/%d/%Y")

print("-" * 30)
print("Search date: ", formatted_date)
print("Numbers found: ", count)
print("Search duration: ", ending - beginning)
print("-" * 30)
