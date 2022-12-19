import re

test = "-DSCF0614.jpg, DSCF0596.RAF errgeg\nDSCF0637\tDSCF0606dewwwwwwwwwwww"
result = re.findall("\d{4}", test)
test1 = "-DSCF0614.jpg"
result1 = re.findall("\d{4}", test1)
print(result)
