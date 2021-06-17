from src import print_split_line
# for循环的使用
magicians = ['alice', 'david', 'carolina']
print("使用for打印出数组元素：")
for magician in magicians:
    print(magician)
print_split_line.print_split_line('*', 20)

for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can`t wait to see your next trick, " + magician.title() + ".\n")
print("Thank you, everyone. That was a great magic show!")
print_split_line.print_split_line('*', 20)

# 数值列表
for value in range(1, 5):
    print(value)
print_split_line.print_split_line('*', 20)

# 使用list方法自动转换为数字列表
numbers = list(range(1, 6))
print(numbers)
print_split_line.print_split_line('*', 20)

even_numbers = list(range(2, 11, 2))
print(even_numbers)
print_split_line.print_split_line('*', 20)

# squares
squares = []
for value in range(1, 11):
    # square = value ** 2
    # squares.append(square)
    squares.append(value ** 2)
print(squares)
print_split_line.print_split_line('*', 20)

# 简单统计
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print("digits:" + str(digits))
print("min:" + str(min(digits)))
print("max:" + str(max(digits)))
print("sum:" + str(sum(digits)))
print_split_line.print_split_line('*', 20)

# 列表解析
cube = [value**3 for value in range(1, 11)]
print(cube)

"""
开始
多行注释：
测试使用
结束
"""
