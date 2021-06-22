import func_家具类
import func_房子类


bed = func_家具类.HouseItem("席梦思", 4)
chest = func_家具类.HouseItem("衣柜", 2)
table = func_家具类.HouseItem("餐桌", 1.5)
my_home = func_房子类.House("两室一厅", 80)

print(my_home)
my_home.add_item(func_家具类.bed)
my_home.add_item(func_家具类.table)
my_home.add_item(func_家具类.chest)
print(my_home)
