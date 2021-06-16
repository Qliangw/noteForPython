# import的使用 导入随机工具包
import random
"""
猜拳游戏
    目标
        1. 强化多个条件的逻辑运算
        2. 初体验import的使用
    需求
        1. 控制台输入--石头(1)、剪刀(2)、布(3)
        2. 电脑随机出拳
        3. 比较胜负
"""
player = int(input("\033[1;40;47m猜拳游戏说明\n——石头(1)\n——剪刀(2)\n——布(3)\n——退出(0)\t请输入您的选项：\033[0m"))

while player != 0:
    if player == 0:
        break
    elif (player == 1) or (player == 2) or (player == 3):
        computer = random.randint(1, 3)
        dis_str = ["石头", "剪刀", "布"]
        print("\033[33m玩家：%s——电脑：%s\033[0m" % (dis_str[player-1], dis_str[computer-1]))
        if(player == 1 and computer == 2) or (player == 2 and computer == 3) or (player == 3 and computer == 1):
            print("\033[32m玩家胜利\033[0m\n")
        elif (player == 1 and computer == 1) or (player == 2 and computer == 2)or (player == 3 and computer == 3):
            print("\033[33m平局\033[0m\n")
        else:
            print("\033[34m电脑胜利\033[0m\n")
    else:
        print("\033[31m输入不合法！！！\n\033[0m")
    player = int(input("\033[1;40;47m石头(1)、剪刀(2)、布(3)\t请输入数字\033[0m："))

print("游戏结束")
