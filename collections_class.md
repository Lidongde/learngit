# python-内建的模块
## 1. collections

collections提供了许多有用的集合类(使用时需要import相应的类,如`from collections import deque`):
> **namedtuple**
>> 用namedtuple可以很方便地定义一种*数据类型*，它具备 tuple 的不变性，又可以根据属性来引用:

	>>> from collections import namedtuple
	>>> Point = namedtuple('Point', ['x', 'y'])
	>>> p = Point(1, 2)
	>>> p.x
	1
	>>> p.y
	2

> **deque**
>> list存储数据时存在索引快速但插入和删除元素缓慢的问题,借用deque是为了高效实现插入和删除操作的双向列表.

	>>> from collections import deque
	>>> q = deque(['a', 'b', 'c'])
	>>> q.append('x')
	>>> q.appendleft('y')
	>>> q
	deque(['y', 'a', 'b', 'c', 'x'])
deque除了实现 list 的append()和pop()外，还支持appendleft()和popleft()，这样就可以非常高效地往头部添加或删除
元素。

> **defaultdict**
>> 使用dict时，如果引用的 Key 不存在，就会抛出KeyError。如果希望 key不存在时，返回一个默认值，就可以用defaultdict(除此之外,defaultdict的其他行为跟dict是完全一致的):

	>>> from collections import defaultdict
	>>> dd = defaultdict(lambda: 'N/A')
	>>> dd['key1'] = 'abc'
	>>> dd['key1'] # key1 存在
	'abc'
	>>> dd['key2'] # key2 不存在，返回默认值
	'N/A'

> **OrderedDict**
>> 保持dict的key的顺序,待续

> **Counter**
>> Counter是一个简单的计数器,例如统计自负出现的个数:

	>>> from collections import Counter
	>>> c = Counter()
	>>> for ch in 'programming':
	... c[ch] = c[ch] + 1
	...
	>>> c
	Counter({'g': 2, 'm': 2, 'r': 2, 'a': 1, 'i': 1, 'o': 1, 'n': 1, 'p': 1})