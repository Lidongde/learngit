## python 中MethodType的使用解析

MethodType将方法绑定到类，并不是将这个方法直接写到类内部，而是在内存中创建一个link指向外部的方法，在创建实例的时候这个link也会被复制。[具体参见](https://www.baidu.com/
)

三种形式：

 `object_name.function_to_be_used = MethodType(function_to_be_used, object_name, class_name)`

该命令是将函数（方法）单一绑定到类的一个实例上，只有绑定过的实例才能调用该函数。

`class_name.function = MethodType(function, None, class_name)`

该命令将函数绑定到class上，类的所有实例都能调用该函数。

`class_name.function = MethodType(function, class_name)`

该命令同上一个命令只差一个none，在实例调用函数时产生的返回值有且仅有一个即第一次调用时的返回值。

## 使用`__slots__`限制可以绑定的属性
*注意属性不等于方法*

class定义时在类的内部加上如下代码：

`__slots__ = ('character_name1', 'character_name2', ...)`用tuple哦！

然后该类（不包括子类，但子类若定义有__slots__的话则自动加上父类的__slots__，相当于单向有效）的实例只能绑定给定的tuple中的元素