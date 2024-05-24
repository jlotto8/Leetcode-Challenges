
import re

str = "..Bob hit a ball, the hit BALL flew far after it's was hit."
# , ['hit'])

pattern = re.compile(r'\W+')

str_1 = pattern.split(str)

# print(str_1)

for i in "!?',;.":
    str = str.replace(i,"")
str = str.split()


print(str)

# remove chars that do not appear in words; 