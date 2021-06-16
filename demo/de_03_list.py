# 列表的简单使用
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print("查看数组：", bicycles)

print("访问第一个元素：", bicycles[0])
print("访问第一元素（title方法）：", bicycles[0].title())

# 访问最后一个元素，Python提供了特殊方法：-1
print("访问最后一个元素：", bicycles[-1].title())
print("---------------------------------")
# 使用列表中的值
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)
print("---------------------------------")

# 修改、添加和删除元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print("初始元素：" + str(motorcycles))

motorcycles[0] = 'ducati'
print("改变第一个元素：" + str(motorcycles))

# 初始化
motorcycles[0] = 'honda'
# 在列表末尾添加元素
motorcycles.append('ducati')
print("列表末尾添加元素：" + str(motorcycles))

# 创建空列表，通过append方法添加亦可实现
motorcycles2 = []
motorcycles2.append('honda')
motorcycles2.append('yamaha')
motorcycles2.append('suzuki')
print(" append方法实现：" + str(motorcycles2))

# 在列表中插入
motorcycles.insert(0,'ducati')
print("在列表中插入：" + str(motorcycles))

# 使用del方法删除
del motorcycles[0]
del motorcycles[3]
print("del删除元素：" + str(motorcycles))

# 使用pop方法删除
popped_motocycles = motorcycles.pop()
print("pop删除末尾元素：" + str(motorcycles))
print("被删除的元素：" + popped_motocycles)

# 根据值删除元素
motorcycles.append('suzuki')
motorcycles.append('ducati')
print("remove删除前：" + str(motorcycles))
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print("remove删除后：" + str(motorcycles))
print("\nA" + too_expensive.title() + " is too expensive for me.E")
print("---------------------------------")

# 组织列表
# 使用sort()对列表进行永久性排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("原始数据：" + str(cars))
cars.sort()
print("sort排序后：" + str(cars))
cars.sort(reverse=True)
print("sort反向排序：" + str(cars))

# 使用sorted()对列表进行临时排序
# 使用reverse()是按照当前序列的顺序倒序，并不是按照字母顺序
cars.reverse()
print("reverse倒序当前序列：" + str(cars))

# len()确定长度
print("cars元素个数：" + str(len(cars)))
