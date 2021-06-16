# 保存每个程序时，使用符合标准Python约定的文件名：使用小写字母和下划线，如simple_message.py
# *-1 打印
# 直接打印
print("直接打印：" + "Hello my Bug1")
print("---------------------------------")
# *-2 变量
# 使用变量，就目前而言，应使用小写的Python变量名。
# 在变量名中使用大写字母虽然不会导致错误，但避免使用大写字母是个不错的习惯。
message = "Hello my Bug2"
print("打印变量：" + message)
print("---------------------------------")
# *-3 字符串 在Python中，用括号引起的都是字符串，其中的引号可以是单引号，也可以是双引号。
name = "ada lovelace"
print("首字母大写：" + name.title())
# 将字符串改为全部大写、小写
print("字符串大写：" + name.upper())
print("字符串小写：" + name.lower())

# 合并（拼接）字符串
first_name = 'ada'
last_name = 'lovelace'
full_name = first_name + ' ' + last_name

print('字符串拼接：' + full_name)
print('拼接其他信息：' + "Hello," + full_name.title() + '!')
print("---------------------------------")

# 使用制表符
# 对比以下输出
print("比对以下输出：")
print("Python")
print("\tPython")
print("---------------------------------")

print("Languages:\nPython\nC\nJava")
print("---------------------------------")

print("Languages:\n\tPython\n\tC\n\tJava")
print("---------------------------------")

# 删除空白
# .rstrip()方法删除右面空白为临时的，不改变原有变量的值,要永久剔除需要赋值给原变量
favorite_language = 'python '
print(favorite_language + '.')
print(favorite_language.rstrip() + '.')
print(favorite_language + '.')
print("---------------------------------")

# .lstrip()方法删除左面空白为永久的，改变原有变量的值
favorite_language = ' python '
print("lstrip:" + favorite_language.lstrip() + '.')
print("rstrip:" + favorite_language.rstrip() + '.')
print(" strip:" + favorite_language.strip() + '.')
# *-
# *-
# *-

