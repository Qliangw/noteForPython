

def zero():
    return "zero"


def one():
    return "one"


def two():
    return "two"


def num2str(arg):
    switcher = {
        0: zero,
        1: one,
        2: two,
        3: lambda: "three"
    }
    func = switcher.get(arg, lambda: "nothing")
    return func()


if __name__ == '__main__':
    print(num2str(2))
