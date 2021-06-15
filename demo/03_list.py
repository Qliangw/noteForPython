
bicycles = ['trek','cannondale','redline','specialized']
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

