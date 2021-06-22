class Cat:
    def __init__(self, new_name):
        self.name = new_name
        print("%s已创建" % self.name)

    def __del__(self):
        print("*" * 20)
        print("-> %s已销毁" % self.name)
        print("*" * 20)

    def __str__(self):
        # 必须返回一个字符串
        return "Mow:我是%s" % self.name

    def eat(self):
        print("%s爱吃鱼" % self.name)

    def drink(self):
        print("%s不爱喝水" % self.name)


# 创建对象
htt_cat = Cat("黑炭头")
dd_cat = Cat("蛋丁")

# 打印对象信息
print(htt_cat)
print(dd_cat)

# 对象方法
htt_cat.eat()

# 删除对象
del htt_cat

# 对象方法
dd_cat.drink()

