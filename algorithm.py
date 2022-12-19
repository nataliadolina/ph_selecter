import os
import shutil
from os import path
import re

folder_from = "C:\\Users\\ACER\Desktop\\test"
folder_to = "C:\\Users\\ACER\Desktop\\test\\test1"
needed_files = ["DSCF0614.RAF", "DSCF0596.RAF"]


def pwd(dir):
    try:
        data = [i for i in os.listdir(dir)]
    except FileNotFoundError:
        data = []
    return data


def copy_files(dir_from, dir_to, files_to_copy):
    all_files = {re.findall("\d{4}", i)[0]: i for i in pwd(dir_from) if path.isfile(path.join(dir_from, i))}
    for key in files_to_copy:
        if key in all_files.keys():
            file_dir = path.join(dir_from, all_files[key])
            shutil.copy2(file_dir, dir_to)
