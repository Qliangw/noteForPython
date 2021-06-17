from src import print_split_line
row = 1

print("九九乘法表")
print_split_line.print_split_line('*', 70)
while row <= 9:
    col = 1
    while col <= row:
        print("%d*%d=%d" % (row, col, row*col), end="\t")
        col += 1
        # print("*", end="")
    print("")
    row += 1
print_split_line.print_split_line('*', 70)
print("结束")
