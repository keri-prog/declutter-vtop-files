import re
import os

folder_name = input("Enter Folder location: ").rstrip(f"\\")
try:
    file_names = os.listdir(folder_name)
    not_needed = re.compile(r'[A-Z]{7}[0-9]{4}-[0-9]{2}_[A-Z]{3}[0-9]{4}_[A-Z]{2,3}_[A-Z]{2}[0-9]{13}_[A-Za-z]{9}_[A-Za-z]{8}_[A-Z]+_')
    course_code = re.compile(r'_[A-Z]{3}[0-9]{4}')
    for file_name in file_names:
        if re.match('^[A-Z]{7}[0-9]{4}-[0-9]{2}_[A-Z]{3}[0-9]{4}_[A-Z]{2,3}_', file_name):
            new_name = re.sub(not_needed, '', file_name)
            src = folder_name+f"\{file_name}"
            dst = folder_name+f"\{new_name}"
            os.rename(src, dst)
except FileNotFoundError:
    print("Folder doesnt exist")



