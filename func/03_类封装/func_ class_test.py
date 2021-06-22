class Person:

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        print("我是%s,体重是%.2f公斤" % (self.name, self.weight))

    def __str__(self):
        return "我是%s,体重是%.2f公斤" % (self.name, self.weight)

    def run(self):
        print("%s跑步减肥" % self.name)
        self.weight -= 0.5

    def eat(self):
        print("干饭人%s补充能量" % self.name)
        self.weight += 1


zhang = Person("张三", 75.0)
wong = Person("王五", 69.0)
print("-" * 50)

wong.run()
print(wong)

zhang.eat()
print(zhang)

