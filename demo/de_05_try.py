try:
    num = int(input("请输入一个整数:"))
    res = 8 / num
    print(res)

except ZeroDivisionError:
    print("除数不能为零")
except ValueError:
    print("请输入一个整数")
except Exception as result:
    print("未知错误:\n%s" % result)
else:
    print("尝试成功")
finally:
    print("啥时候都会被执行")


def test_ex():
    pwd = input("请输入一个密码:")

    if len(pwd) >= 8:
        return pwd

    ex = Exception("密码少于8位")
    raise ex


try:
    test_ex()
except Exception as result:
    print(result)
