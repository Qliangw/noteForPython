## 数据类型

Python中数据类型可以分为数字型和非数字型

### 数字型

- 整型 `int`
- 浮点型 `float`
- 布尔型 `bool`
  
        真 True 非0--非零即为真
        假 False 0

- 复数型 `complex`

### 非数字型

- 字符串
- 列表
- 元组
- 字典

-------------

### 在Python中，所有非数字型变量都支持以下特点

1. 都是一个序列`sequence`，也可以理解为容器
2. 取值`[]`
3. 遍历 `for in`
4. 计算长度、最大值/最小值、比较、删除
5. 链接 `+` 重复 `*`
6. 切片


----------

### 1 列表

#### 1.1 列表的定义

- `list`列表 是Python中使用**最频繁**的数据类型，在其他语言中通常叫做**数组**
- 专门用于存储一串信息
- 列表用`[]`定义，数据之间用`,`分割
- 列表的索引从`0`开始
	- 索引就是数据在列表中的位置编号，索引被称为下标
	>  注意： 从列表中取值时，如果超出索引范围，程序会报错

#### 1.2 列表常用操作


|序号|分类|方法|说明|
|---|---|---|---|
|1|增加|`list.insert(索引,数据)`|
| | |`list.append(数据)`|在末尾添加数据|
| | |`list.extetnd(list2)`|将列表2的数据追加到列表上|
|2|删除|`del list[索引]`|删除指定索引的数据|
| | |`list.remove(数据)`|
| | |`list.pop`|删除末尾数据|
| | |`list.pop(索引)`|删除指定索引数据|
| | |`list.clear`|清空列表|
|3|修改|`list[索引] = 数据`| 修改制定索引的数据|
|4|统计|`len(list)`| 列表长度|
| | |`list.count(数据)`|数据在列表中出现的次数|
| | |`list.index(数据)`|查询数据的索引|
|5|排序 |`list.sort()`|升序排序|
| | |`list.sort(reverse=True)`|降序排序|
| | |`list.reverse()`| 反转，逆序|
|6 |其他|`list.copy`|复制

### 2 元组

#### 2.1 元组的定义

- Tuple(元组)与列表类似，不同之处在于元组的元素不修改
	- 元组表示多个元素组成的序列
	- 元组在Python开发中，有特定的使用场景
- 用于存储一串信息，数据直接使用`,`分割
- 使用`()`定义元组
- 元组的索引从0开始
 - 索引就是数据在元组中的位置编号


创建空元组

    info_tuple=()

创建只包含一个元素的元组，需要记得添加`，`

	info_tuple=(1,)

#### 2.2 元组的使用

元组一旦被定义，则该元组的元素不可修改。

|序号|分类|方法|说明|
|---|---|---|---|
|1 | |tuple.count()|
|2 | |tuple.index()|

#### 2.3 循环遍历

- 取值就是从元组中获取存储在指定位置的数据
- 遍历就是从头到尾依次从元组中获取数据

> - 在Python中，可以使用for循环遍历所有非数字型类型的变量：列表、元组、字典及字符串
> - 提示：在实际开发中，除非能够确认元组中的数据类型，否则针对元组的循环遍历需求并不是很多


#### 2.4 应用场景

- 尽管可以使用`for in`遍历元组，但开发中更多场景为：
 - 函数的参数和返回值，一个函数可以接受多个任意多个参数，或者一次返回多个数据
 - 格式字符串，格式化字符串后面的`()`本质上就是一个元组
 - 让列表不可以被修改，以保护数据安全


 ### 3 字典

#### 3.1 字典的定义

- 和列表的区别
	- 列表是有序的对象集合
	- 字典是无序的对象集合 
- 字典用`{}`定义、
- 字典使用**键值对**存储数据，键值对之间使用`,`分隔
	- 键`key`是索引
	- 值`value`是数据
	- 键 和 值 之间用`:`分隔
	- 键必须是唯一的
	- 值可以是任何数据类型，但键只能使用字符串、数字或元组


----------

	test = {
		"name": "test",
		"age": 99,
		"gender": True,
		"height": 188} 

----------



#### 3.2 字典的增删改查

#### 3.3 字典的遍历

#### 3.4 字典的应用

- 使用多个键值对，描述一个物体的相关信息--描述更复杂的数据信息
- 将多个字典放在一个列表中，再进行遍历，在循环体内针对每一个字典进行相同的处理

### 4 字符串

#### 4.1 字符串定义

- 字符串就是一串字符，是编程语言中表示文本的数据类型
- 在Python中可以是使用一对双引号`"`，也可以使用一对单引号`'`定义一个字符串
	- 虽然可以使用`\"`或者`\'`做字符串的转义，但是在实际开发中：
		- 如果字符串内部㤇使用`"`，可以使用`'`定义字符串
		- 如果字符串内部需要使用`'`,可以使用`"`定义字符串
	- 可以使用索引获取一个字符串指定位置的字符,索引从0开始
	- 也可以使用for循环遍历字符串中的每一个字符



#### 4.2 字符串常用操作

##### 1) 判断类型

|方法|说明|
|---|---|
| string.isspace() | 如果string只包含空格,则返回True|
| string.isalnum() | 如果string至少有一个字符并且所有字符都是字母或者数字则返回True |
| string.isalpha() | 如果string至少有一个字符并且所有字符都是字母则返回True|
| string.isdecimal() | 如果string只包含数字则返回True,全角数字|
| string.isdigit() |  如果string只包含数字则返回True,全角数字 (1) \u00b2|
| string.isnumeric() | 如果string只包含数字则返回Ture,全角数字 汉字数字|
| string.istitle() | 如果string是标题化的(每个单词的首字母大写),则返回True|
| string.islower() | 如果string中包含至少一个区分大小写的字符,并且所有这些字符都是小写,则返回True|
| string.isupper() | 如果string中包含至少一个区分大小写的字符,并且所有这些字符都是大写,则返回True|
| string.isascii() | 如果string中的所有字符串都是ascii,则返回True|
| string.isidentifier() | 如果string是有效的标识符,则返回Ture|
| string.isprintable() | 如果string中所有字符都是可打印的或者字符串为空,则返回True|

##### 2) 查找和替换

|方法|说明|
|---|---|
| string.startswith() | 检查字符串是否以`xx`开头,是则返回True|
| string.endswith() | 检查字符串是否以`xx`结尾,是则返回True|
| string.find(str,start=0,end=len(string) | 检测str是否包含在string中,如果start和end指定范围,则检查是否包含在指定范围内,如果是返回开始的索引值,否则返回`-1`|
| string.rfind() | 同上,不过是倒序开始查找|
| string.index(str,start=0,end=len(string) | 与上面类似,只不过str不在string中会报错|
| string.rindex() | 同上|
| string.replace(old_str,new_str,num=sting.count(old) | 把string的内容替换,注意num的长度|

##### 3) 大小写替换

|方法|说明|
|---|---|
| string.capitalize() | 把字符串的第一个字符大写|
| string.title() | 把字符串的每个单词首字母大写|
| string.lower() | 转换string中所有大写->小写|
| string.upper() | 转换string中所有小写->大写|
| string.swapcase() | 反转string中的大小写|

##### 4) 文本对齐

|方法|说明|
|---|---|
| string.ljust(width) | 返回一个原字符串左对齐,并使用空格填充至长度width的新字符串|
| string.rjust(width) | 返回一个原字符串右对齐,并使用空格填充至长度width的新字符串|
| string.center(width) | 返回一个原字符串居中,并使用空格填充至长度width的新字符串|

##### 5) 去除空白符


|方法|说明|
|---|---|
| string.lstrip() | 截掉左边(开始)的空白字符|
| string.rstrip() | 截掉右边(开始)的空白字符|
| string.strip() | 截掉左右两边的空白字符|

##### 6) 拆分和链接


|方法|说明|
|---|---|
| string.partition(str) | 把字符串分成一个3元素的元组`(str前,str,str后)`|
| string.rpartition(str) | 类似,倒序|
| string.split(str="",nmu) | 以str为分隔符切片string,如果num有指定值,则仅分隔num+1个子字符串,str默认包含 `\r \n \r\n`和空格|
| string.rsplit() | |
| string.splitlines() | 按照行(\r \n \r\n)分隔,返回一个包含各行作为元素的列表|
| string.join(seq) | 以string作为分隔符,将seq中所有的元素(的字符串表示)合并为一个新的字符串|

##### 7 其他--暂未整理

|方法|说明|
|---|---|
| string.casefold() | |
| string.expandtabs() | |
| string.zfill() | |
| string.maketrans() | |
| string.count() | |
| string.format() | |
| string.encode() | |
| string.format_map() | |
| string.removesuffix() | |
| string.removeprefix() | | 
| string.translate() | |
