
#### 多值参数

##### 定义支持多值参数的函数

- 有时可能需要一个函数能够处理的参数的个数是不确定的,这个时候,就可以使用多值参数
- Python中有两种多值参数
    - 参数名前增加一个`*`可以接受元组
    - 参数名前增加两个`*`可以接受字典
- 一般在给多值参数命名时,习惯使用以下两个名字
	- `*args`--存放元组参数,前面有一个`*`
	- `**kwargs`--存放字典参数,前面有两个`*`
- `args`是arguments的缩写,有变量的含义
- `kw`是keyword的缩写,kwargs可以记忆键值对参数


----------


	def demo(num, *args, **kwargs)
		print(num)
		print(args)
		print(kwargs)

	demo(1, 2, 3, 4, 5, name="test", age=18,gender=True)


----------

#### 元组和字典的拆包

- 在调用带有多值参数的函数时,如果希望:
	- 将一个元组变量,直接传递给args
	- 将一个字典变量,直接传递给kwargs
- 就可以使用拆包,简化参数的传递,拆包的方式是:
	- 在元组变量前,增加一个*
	- 在字典变量前,增加两个**



----------

	def demo(*args, **kwargs):
		print(args)
		print(kwargs)
	
	# 需要将一个元组变量/字典变量传递给函数对应的参数
	gl_nums = (1, 2, 3)
	gl_xiaoming = {"name": "小明", "age": 18}

	# 会把num_tuple和xianming作为元组传递给args
	# demo(gl_nums, gl_xiaoming)
	demo(*gl_nums, **gl_xiaoming)

----------
