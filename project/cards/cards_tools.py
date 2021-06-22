# 记录所有的名片字典
card_list = []


def show_menu():
    """显示菜单"""
    print("*" * 50)
    print("欢迎使用【名片管理系统】Ver0.1\n")
    print("【1】新增名片\t", end="")
    print("【2】显示全部\t", end="")
    print("【3】搜索名片\n", end="")
    print("【0】退出")
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

    # 判断是否为空
    if len(card_list) == 0:
        print("名片为空,请使用新增后再次查看")

        # 下方代码不会被执行
        # 如果return后面没有任何内容,表示会返回到调用函数的位置,并且不返回任何的结果
        return
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

    # 提示用户输入要搜索的内容
    find_name = input("请输入要搜索的内容:")

    # 遍历名片列表
    for card_dict in card_list:
        if card_dict["name"] == find_name:
            # 打印表头
            for name in ["姓名", "电话", "邮箱"]:
                print(name, end="\t\t")
            print("")

            # 打印分割线
            print("=" * 50)

            # 打印内容
            print("%s\t\t%s\t\t%s" % (card_dict["name"],
                                      card_dict["phone"],
                                      card_dict["email"]))

            # 对于查找到的信息进行修改和删除的操作
            deal_card(card_dict)

            break
    else:
        print("抱歉,没有找到%s" % find_name)


def deal_card(find_dict):
    """处理查找到的名片

    :param find_dict:查找到的名片
    """
    print("-" * 50)

    action_str = input("【1】修改\t【2】删除\t【0】主菜单\n"
                       "请选择要执行的操作:")

    if action_str == "1":
        print("您选择的操作是【%s】:修改名片[留空为原值]" % action_str)
        find_dict["name"] = input_card_info(find_dict["name"], "姓名:")
        find_dict["phone"] = input_card_info(find_dict["phone"], "电话:")
        find_dict["email"] = input_card_info(find_dict["email"], "邮箱:")
        print("修改名片成功")
    elif action_str == "2":
        print("您选择的操作是【%s】:删除名片" % action_str)

        action_del = input("输入[Y]确定,其他键退出,请输入:")
        if action_del == ("y" or "Y"):
            card_list.remove(find_dict)

        print("删除名片成功")


def input_card_info(dict_value, tip_message):
    """输入名片信息

    :param dict_value: 要替换的值
    :param tip_message: 提示信息
    :return: 如果输入为空,返回原值;不为空返回输入值
    """
    # 提示用户输入内容
    result_str = input(tip_message)

    # 针对用户的输入进行判断
    if len(result_str) > 0:
        return result_str
    # 如果为空,返回字典中的值
    else:
        return dict_value
