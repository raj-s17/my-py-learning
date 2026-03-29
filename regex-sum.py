fname = input("Enter file name: ")
if len(fname)<1:
    fname = "regex_sum_42.txt"

handle = open(fname)

import re
total = 0

for line in handle:
    nums = re.findall('[0-9]+',line)
    for num in nums: 
        total = total + int(num)
print(total)