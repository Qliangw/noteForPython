class MusicPlayer(object):

    # 记录第一个被创建对象的引用
    instance = None

    # 记录是否被执行过初始化动作
    init_flag = False

    def __new__(cls, *args, **kwargs):

        # 判断类属性是否为空对象
        if cls.instance is None:
            # 调用父类的方法,为第一个对象分配空间
            cls.instance = super().__new__(cls)

        # 返回对象的引用
        return cls.instance

    def __init__(self):
        if MusicPlayer.init_flag:
            return
        print("播放器初始")
        MusicPlayer.init_flag = True


# 创建播放器对象
player1 = MusicPlayer()
print(player1)

player2 = MusicPlayer()
print(player2)
