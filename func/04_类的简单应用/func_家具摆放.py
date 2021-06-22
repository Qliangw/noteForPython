class HouseItem:

    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "[%s]占地%.2f平方" % (self.name, self.area)


class House:

    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area

        self.free_area = area

        self.item_list = {}

    def __str__(self):
        return ("[户型]:%s\n[总面积]:%.2f平方米\n[剩余面积]:%.2f\n[家居]:%s\n"
                % (self.house_type, self.area,
                   self.free_area, self.item_list))

    def add_item(self, item):
        print("要添加的家具:%s" % item)

        if item.area > self.free_area:
            print("%s太大了,无法添加" % item.name)
            return

        self.item_list[item.name] = item.area
        self.free_area -= item.area


bed = HouseItem("席梦思", 4)
chest = HouseItem("衣柜", 2)
table = HouseItem("餐桌", 1.5)
my_home = House("两室一厅", 80)

# print(my_home)
my_home.add_item(bed)
my_home.add_item(table)
my_home.add_item(chest)
print(my_home)


