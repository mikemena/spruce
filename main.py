import os
import re
import time
from collections import Counter
from datetime import datetime


def serial_number_finder():
    root_directory = "project_unzipped/My_Big_Directory"
    pattern = r"N[A-Za-z]{3}-\d{5}"
    results = []

    for dirpath, dirnames, filenames in os.walk(root_directory):
        for filename in filenames:
            if filename.endswith(".txt"):
                file_path = os.path.join(dirpath, filename)
                with open(file_path, "r", encoding="utf-8") as file:
                    file_content = file.read()
                    matches = re.findall(pattern, file_content)
                    for match in matches:
                        results.append((filename, match))

    return results


beginning = time.time()
serial_numbers = serial_number_finder()
count = Counter(serial_numbers)
total_count = sum(count.values())
ending = time.time()

today_date = datetime.now()
formatted_date = today_date.strftime("%m/%d/%Y")

print("-" * 30)
print("\nSearch date: ", formatted_date, "\n")
print(f"{'FILE':<15} {'SERIAL NO.':<15}")
print(f"{'----':<15} {'----------':<15}")
for filename, serial_number in serial_numbers:
    print(f"{filename:<15} {serial_number:<15}")
print("\nNumbers found: ", total_count)
print("\nSearch duration: ", ending - beginning, "seconds\n")
print("-" * 30)
