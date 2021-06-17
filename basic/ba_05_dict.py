from src import print_split_line
# 定义一个字典
dict_phone = {"品牌": "锤子"}

print(dict_phone)
print_split_line.print_split_line('*', 20)

# 新增键值对
dict_phone["价格"] = 5999
print(dict_phone)
print_split_line.print_split_line('*', 20)

# 修改 如果不存在为增加，存在为修改
dict_phone["品牌"] = "苹果"
print(dict_phone)
print_split_line.multi_split_line('*', 20, 1)

# 删除
dict_phone.pop("品牌")
print(dict_phone)

# 统计键值对数量
print("键值对数量：" + str(len(dict_phone)))
print_split_line.multi_split_line('*', 20, 1)

# 字典合并 如果键有相同 值会别替换
dict_temp = {"品牌": "锤子",
             "价格": 6999}
dict_phone.update(dict_temp)
print(dict_phone)
print_split_line.multi_split_line('*', 20, 1)

# 清空字典
dict_phone.clear()
print(dict_phone)
print_split_line.multi_split_line('*', 20, 1)

# 遍历字典
dict_test_phone = {"品牌": "锤子",
                   "价格": 6999,
                   "重量": "186g"}

for k in dict_test_phone:
    print("%s - %s" % (k, dict_test_phone[k]))
print_split_line.multi_split_line('*', 20, 1)

# 字典 + 列表
card_list = [
    {"品牌": "锤子",
     "价格": 5699,
     "子公司": "苹果"},
    {"品牌": "苹果",
     "价格": 8999,
     "母公司": "锤子"}
]
for card_info in card_list:
    print(card_info)
print_split_line.multi_split_line('*', 20, 1)
