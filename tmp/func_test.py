

def zero():
    return "zero"


def one():
    return "one"


def two():
    return "two"


def num2str(arg):
    """
    数字转换字符串

    :param arg: 要转换的数据
    :return:
    """
    # 使用字典
    switcher = {0: zero,
                1: one,
                2: two,
                3: lambda: "three"}
    func = switcher.get(arg, lambda: "nothing")
    return func()


if __name__ == '__main__':
    print(num2str(2))
