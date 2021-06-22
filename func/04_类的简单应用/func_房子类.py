import func_家具类


class House:

    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area

        self.free_area = area

        self.item_list = []

    def __str__(self):
        return ("户型:%s\n总面积:%.2f平方米\n剩余面积:%.2f\n家居:%s\n"
                % (self.house_type, self.area,
                   self.free_area, self.item_list))

    def add_item(self, item):
        print("要添加的家具:%s" % item)

        if item.area > self.free_area:
            print("%s太大了" % item.name)
            return

        self.item_list.append(item.name)
        self.free_area -= item.area
