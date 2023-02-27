import os
import shutil
from os import path, makedirs
import re


def pwd(dir):
    try:
        data = os.listdir(dir)
    except FileNotFoundError:
        data = []
    return data


def get_all_files1(dir):
    b = {}
    keys = []
    for i in pwd(dir):
        if not path.isfile(path.join(dir, i)):
            continue
        key = re.findall("\d{4}", i)
        for k in key:
            if k not in keys:
                b[k] = []
                keys.append(k)
            b[k].append(i)

    return b, keys


def get_all_files(dir):
    b = {}
    keys = []
    for i in pwd(dir):
        if not path.isfile(path.join(dir, i)):
            continue
        key = re.findall("\d{4}", i)
        for k in key:
            if k not in keys:
                b[k] = []
                keys.append(k)
            b[k].append(i)

    return b, keys


def operate_files(dir_from, dir_to, files, operation):
    if not path.exists(dir_from) or dir_from == dir_to:
        raise Exception

    all_files, filenames_keys = get_all_files(dir_from)
    not_found = []
    operated = []
    not_operated = []
    if not path.exists(dir_to):
        makedirs(dir_to)
    for key in files:
        if key in filenames_keys:
            file_names = all_files[key]
            for file_name in file_names:
                file_dir = path.join(dir_from, file_name)
                target_dir = path.join(dir_to, file_name)
                if not path.exists(target_dir):
                    operation(file_dir, dir_to)
                    operated.append(file_name)
                else:
                    not_operated.append(file_name)

        else:
            not_found.append(key)
    return operated, not_operated, not_found


def copy_files(dir_from, dir_to, files_to_copy):
    return operate_files(dir_from, dir_to, files_to_copy, shutil.copy2)


def move_files(dir_from, dir_to, files_to_move):
    return operate_files(dir_from, dir_to, files_to_move, shutil.move)


def read_file_data(filename):
    with open(filename, "rt", encoding="utf-8") as file:
        t = file.read()
    return t
