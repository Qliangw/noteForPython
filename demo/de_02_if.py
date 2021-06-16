print("---------------------------------")
age = int(input("请输入年龄："))

i = 1
while i == 1:
    # 如果大于110或者小于0岁，重新输入
    if (age >= 110) or (age < 0):
        age = int(input("请输入正确年龄："))
    else:
        i = 0

if age >= 18:
    print("成年人")
else:
    print("未成年人")

print("结束")
print("---------------------------------")
