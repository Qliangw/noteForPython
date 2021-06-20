# 记录所有的名片字典
card_list = []


def show_menu():
    """显示菜单"""
    print("*" * 50)
    print("欢迎使用【名片管理系统】Ver0.1\n")
    print("1. 新增名片")
    print("2. 显示全部")
    print("3. 搜索名片\n")
    print("0. 退出")
    print("*" * 50)


def new_card():
    """新增名片"""
    print("-" * 50)
    print("新增名片")

    # 提示用户输入名片信息
    name_str = input("请输入姓名：")
    phone_str = input("请输入电话：")
    email_str = input("请输入邮箱：")

    # 使用用户输入信息建立名片字典
    card_dict = {"name": name_str,
                 "phone": phone_str,
                 "email": email_str}

    # 将名片字典添加列表
    card_list.append(card_dict)
    print(card_list)

    # 提示成功
    print("添加%s的名片成功" % name_str)
    print("-" * 50)


def show_all():
    """显示所有名片"""
    print("-" * 50)
    print("显示所有名片")

    # 打印表头
    print("-" * 50)
    for name in ["姓名", "电话", "邮箱"]:
        print(name, end="\t\t")
    print("")

    # 打印分割线
    print("=" * 50)

    # 遍历名片列表
    for card_dict in card_list:
        print("%s\t\t%s\t\t%s" % (card_dict["name"],
                                  card_dict["phone"],
                                  card_dict["email"]))


def search_card():
    """搜索名片"""
    print("-" * 50)
    print("搜索名片")
