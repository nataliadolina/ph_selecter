import configparser
import json


def get_new_dirs_list(dir, last_dirs):
    if dir in last_dirs:
        last_dirs.remove(dir)
        last_dirs.insert(0, dir)
        return last_dirs

    if dir not in last_dirs and len(last_dirs) < 5:
        last_dirs.insert(0, dir)
        return last_dirs

    elif dir not in last_dirs and len(last_dirs) == 5:
        last_dirs.insert(0, dir)
        last_dirs = last_dirs[:-1]
        return last_dirs


class Config:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read("files/config.ini")

    def get_last_to_dirs(self):
        string = self.config["HASH"]["last_to_directories"]
        if string == '""':
            return []
        return self.parse_string_to_list(string)

    def get_last_from_dirs(self):
        string = self.config["HASH"]["last_from_directories"]
        if string == '""':
            return []
        return self.parse_string_to_list(string)

    def set_last_to_dir(self, dir):
        last_dirs = self.get_last_to_dirs()
        new_dirs_list = get_new_dirs_list(dir, last_dirs)
        self.config["HASH"]["last_to_directories"] = self.parse_list_to_string(new_dirs_list)

    def set_last_from_dir(self, dir):
        last_dirs = self.get_last_from_dirs()
        new_dirs_list = get_new_dirs_list(dir, last_dirs)
        self.config["HASH"]["last_from_directories"] = self.parse_list_to_string(new_dirs_list)

    def parse_list_to_string(self, lst):
        return "\n".join(lst)

    def parse_string_to_list(self, string):
        return string.split("\n")

    def save(self):
        with open('files/config.ini', 'w') as configfile:
            self.config.write(configfile)
