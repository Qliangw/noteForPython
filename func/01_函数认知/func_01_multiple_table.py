def multiple_table():
    row = 1

    print("九九乘法表\n**********************************************************************")
    while row <= 9:
        col = 1
        while col <= row:
            print("%d*%d=%d" % (row, col, row * col), end="\t")
            col += 1
            # print("*", end="")
        print("")
        row += 1
    print("**********************************************************************\n结束")
