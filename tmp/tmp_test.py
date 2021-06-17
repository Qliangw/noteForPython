import keyword
from src import print_split_line

i = 0
while i < len(keyword.kwlist):
    print(keyword.kwlist[i])
    i += 1

print_split_line.multi_split_line('*', 20, 2)

for kw_name in keyword.kwlist:
    print(kw_name)
