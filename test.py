import re
from functions import read_file_data, copy_files
from Config import get_new_dirs_list

test = "-DSCF0614.jpg, DSCF0596.RAF errgeg\nDSCF0637\tDSCF0606dewwwwwwwwwwww"
result = re.findall("\d{4}", test)
test1 = "-DSCF0614.jpg"
result1 = re.findall("\d{4}", test1)  # print(result)
# print(read_file_data("instruction.txt"))

# test_string = re.findall("\d{4}", "DSCF9354DSCF9368-3 DSCF9385DSCF94799629iii9801")

# print(copy_files("C:\\Users\\ACER\\Desktop\\AI\\Britain\\ps", "C:\\Users\\ACER\\Desktop\\AI\\Britain\\ps\\Новая папка",
#           test_string))

dirs1 = ["1", "2"]
dirs2 = ["1", "2", "3", "4"]
dirs3 = ["1", "2", "3", "4", "5"]
print(get_new_dirs_list("3", dirs1))
print(get_new_dirs_list("3", dirs2))
print(get_new_dirs_list("6", dirs2))
