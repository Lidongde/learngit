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

2018/7/29 17:02:54 

---

Decorator(装饰器）：

假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为装饰器。本质上，decorator就是一个**返回函数**的高阶函数。

* 装饰器涉及两个方面：一个是装饰器即(返回一个函数的函数)的定义，另一个是使用@语法将decorator至于函数定义处*（也即是def关键字前）*

>[@语法](https://blog.csdn.net/yjreset/article/details/79329979):*"@修饰符"*  修饰符必须出现在函数定义前一行，不允许和函数定义在同一行。也就是说＠A def f(): 是非法的。 只可以在模块或类定义层内对函数进行修饰，不允许修修饰一个类。一个修饰符就是一个函数，它将被修饰的函数做为参数，并返回修饰后的同名函数或其它可调用的东西。

>使用decorator后,被修饰的函数的__name__会发生改变, 会导致某些依赖函数签名的代码执行出错,措施是使用python内置的functools.wraps,`import functools`后在wrapper()的定义前面加上@functools.wraps(func)即可。

---

python中函数块内再定义函数是python的**[闭包](https://blog.csdn.net/ChangerJJLee/article/details/52598629)**

1. 如果试图在外部函数的外部调用内部函数将会报错
2. 如果函数形成闭包,则外部函数调用时需要传递**内部加外部函数的所有参数**
3. 传参时允许"把外部函数赋给一个变量(此时该变量成为一个函数),再用该变量来传递内部函数的参数(类似于一般的函数调用)"
4. 内部函数不能直接引用外部函数定义的变量(如`x *= x`)但可以定义同名变量(如`x = 32`),同名变量返回后能屏蔽外部函数作用域内的变量

---

`__name__`相当于python内置的一个*名称*属性，可以**查询函数的名称** (专业术语,函数签名就是指函数名称)

---

**默认参数**可以简化函数的调用。设置默认参数时，有几点要注意：
一是必选参数在前，默认参数在后，否则 Python 的解释器会报错（思考一下为什么默认参数不能放在必选参数前
面）；
二是如何设置默认参数。
当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。
使用默认参数有什么好处？最大的好处是能降低调用函数的难度。
有多个默认参数时，调用的时候，既可以按顺序提供默认参数，比如调用enroll('Bob', 'M', 7)，意思是，除
了name，gender这两个参数外，最后 1 个参数应用在参数age上，city参数由于没有提供，仍然使用默认值。
也可以不按顺序提供部分默认参数。当不按顺序提供部分默认参数时，需要把参数名写上。比如调用enroll('Adam',
'M', city='Tianjin')，意思是，city参数用传进去的值，其他默认参数继续使用默认值。

默认参数有个坑：Python 函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，每
次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
所以，定义默认参数要牢记一点：默认参数必须指向不变对象！

可变参数：函数定义时参数名前加一个*符号，表示参数可以接收list或tuple，在调用函数时便可以实现“传入任意个参数“，（在传递参数时自动实现tuple的构造）；当已经有一个list或tuple时，调用函数有两种方法，一是将list或tuple的元素依次取出组成参数列表，二是直接在list或tuple名字前加上*作为参数名。（参数传递到函数内部后全都转为tuple型）

关键字参数：函数定义时参数名前加两个*符号，可变参数允许你传入 0 个或任意个参数，这些可变参数在函数调用时自动组装为一个 tuple 。而关键字参数允许你传入 0
个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个 dict，函数参数的传递同可变参数。

参数组合：能且只能以必选参数、默认参数、可变参数和关键字参数的顺序使用四种参数定义函数，调用时自动按照参数位置和参数名把对应参数传入；最神奇的是通过一个 tuple 和 dict ，你也可以调用该函数，如此用时，tuple对应前三项（tuple最少等于必选参数的数量，依次赋给必选、默认和可变，可变变量可为空），dict对应关键字参数。

使用*args和**kw是 Python 的习惯写法，当然也可以用其他参数名，但最好使用习惯用法


二、>>>d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
>>> d['Michael']
暗示：｛…｝[…]这种用法可以从dict中依据key 查出value值，上面两行代码仅是将这种形式拆分开而已。

三、filter map reduce三个函数都接收一个函数和一个序列，区别在于map()依次将序列（list）的元素作为所接收函数的参数进行处理，然后返回一个list；reduce（）以（（a1，a2），a3）这样的顺序进行对序列的累积操作；filter（）把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留（True时）还是丢弃该元素。

四、高阶函数：一个函数接收另一个函数作为参数，这种函数就称之为高阶函数，在高阶函数的定义时，形参列表中函数名的形参在最后。