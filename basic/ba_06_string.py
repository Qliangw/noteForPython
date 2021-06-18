str_hello = "hello hello"

# 统计字符串长度
print("字符串总长度:", end="")
print(len(str_hello))

# 统计某个子字符串出现的次数
print("\"ll\"出现的次数:", end="")
print(str_hello.count("ll"))
print("\"xyz\"出现的次数:", end="")
print(str_hello.count("xyz"))

# 某个子字符串的位置
print("\"ll\"出现的位置:", end="")
ll_info = str_hello.index("ll")
print(ll_info)
print("打印出ll_info的字符:", end="")
print(str_hello[ll_info])
