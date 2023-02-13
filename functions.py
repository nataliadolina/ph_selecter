import os
import shutil
from os import path, makedirs
import re


def pwd(dir):
    try:
        data = [i for i in os.listdir(dir)]
    except FileNotFoundError:
        data = []
    return data


def copy_files(dir_from, dir_to, files_to_copy):
    if not path.exists(dir_from) or dir_from == dir_to:
        raise Exception

    all_files = [(k[0], v) for k, v in
                 [[re.findall("\d{4}", i), i] for i in pwd(dir_from) if path.isfile(path.join(dir_from, i))] if
                 len(k) >= 1]
    all_file_keys = [i[0] for i in all_files]
    not_copied = []
    copied = []
    if not path.exists(dir_to):
        makedirs(dir_to)
    for key in files_to_copy:
        if key in all_file_keys:
            file_names = [i[1] for i in all_files if i[0] == key]
            for file_name in file_names:
                file_dir = path.join(dir_from, file_name)
                copied.append(file_name)
                shutil.copy2(file_dir, dir_to)
        else:
            not_copied.append(key)
    return len(not_copied) == 0, not_copied, copied


def read_file_data(filename):
    with open(filename, "rt", encoding="utf-8") as file:
        t = file.read()
    return t
