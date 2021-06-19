
action_str = input("请选择希望执行的操作:")
print("您选择的操作是【%s】" % action_str)
# 1.2.3 针对名片的操作
if action_str in ["1", "2", "3"]:
    # 如果在开发程序时,不希望立刻编写分支内部的代码
    # 可以使用pass关键字,表示占用一个占位符,能够保证程序的代码结果正确运行
    # 程序运行时,pass关键字不会执行任何的操作
    pass
# 0 退出
elif action_str == "0":
    pass
# 其他内容输入错误
else:
    print("输入错误")
