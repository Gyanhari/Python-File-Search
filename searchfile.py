import os
import string


def get_available_drives():
    return ['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]

def search_file(file_name):
    all_matched_files = []
    for drive in get_available_drives():
        matched_files = file_existence(drive, file_name)
        all_matched_files.extend(matched_files)
    return all_matched_files

def file_existence(drive, file_name):
    matched_files = []
    for root, dirs, files in os.walk(drive):
        for file in files:
            if file == file_name:
                temp = file_address(root, file)
                matched_files.append(temp)
    return matched_files

def file_address(root, file_name):
    return os.path.join(root, file_name)