# input函数的使用
price = float(input("单价："))
weight = float(input("重量："))

# 注意：input接收的数据类型为字符串，需要将字符串转换为float型再做计算
money = price * weight
print("金额：" + str(money))
print("---------------------------------")
print("单价是%.2f元/斤，购买了%.2f斤，需要支付%.2f元" % (price, weight, money))
print("---------------------------------")

