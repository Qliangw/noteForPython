# 注意 申明函数与上方必须有两行的空行，否则会出现警告

def print_split_line(char, times):
    """
    打印单行分割线
    :param char: 要打印的字符
    :param times: 要打印字符的次数
    :return:空
    """
    print(char * times)


def multi_split_line(char, times, nums):
    """
    打印多行参数
    :param char: 要打印的字符
    :param times: 每行要打印的次数
    :param nums: 要打印多少行
    :return: 空
    """
    row = 0
    while row < nums:
        print_split_line(char, times)
        row += 1
