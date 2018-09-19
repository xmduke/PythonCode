#!/usr/bin/python3
##ex32. _32ListOperator.py
li = ["a", "b", "mpilgrim", "z", "example"]
print(li)
print(li[1])
print(li[-1])
print(li[-3])
print(li[1:3])
print(li[1:-1])
print(li[0:3])

li.append("new")
print(li)

li.insert(2, "new")
print(li)

li.extend(["two", "elements"])
print(li)

print(li.index("example"))

print(li.index("new"))

print("c" in li)

li.remove("z")
print(li)

li = li + ["sss", 'sd']
print(li)

'''
7.使用join链接list成为字符串
>>> params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}
>>> ["%s=%s" % (k, v) for k, v in params.items()]
['server=mpilgrim', 'uid=sa', 'database=master', 'pwd=secret']
>>> ";".join(["%s=%s" % (k, v) for k, v in params.items()])
'server=mpilgrim;uid=sa;database=master;pwd=secret'
join 只能用于元素是字符串的 list; 它不进行任何的类型强制转换。
连接一个存在一个或多个非字符串元素的 list 将引发一个异常。

8.list 分割字符串
>>> li = ['server=mpilgrim', 'uid=sa', 'database=master', 'pwd=secret']
>>> s = ";".join(li)
>>> s
'server=mpilgrim;uid=sa;database=master;pwd=secret'
>>> s.split(";")
['server=mpilgrim', 'uid=sa', 'database=master', 'pwd=secret']
>>> s.split(";", 1)
['server=mpilgrim', 'uid=sa;database=master;pwd=secret']
split 与 join 正好相反, 它将一个字符串分割成多元素 list。
注意, 分隔符 (";") 被完全去掉了, 它没有在返回的 list 中的任意元素中出现。
split 接受一个可选的第二个参数, 它是要分割的次数。

9.list 的映射解析
>>> li = [1, 9, 8, 4]
>>> [elem*2 for elem in li]
[2, 18, 16, 8]
>>> li
[1, 9, 8, 4]
>>> li = [elem*2 for elem in li]
>>> li
[2, 18, 16, 8]

10.dictionary中的解析
>>> params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}
>>> params.keys()
['server', 'uid', 'database', 'pwd']
>>> params.values()
['mpilgrim', 'sa', 'master', 'secret']
>>> params.items()
[('server', 'mpilgrim'), ('uid', 'sa'), ('database', 'master'), ('pwd', 'secret')]
>>> [k for k, v in params.items()]
['server', 'uid', 'database', 'pwd']
>>> [v for k, v in params.items()]
['mpilgrim', 'sa', 'master', 'secret']
>>> ["%s=%s" % (k, v) for k, v in params.items()]
['server=mpilgrim', 'uid=sa', 'database=master', 'pwd=secret']

11.list 过滤
>>> li = ["a", "mpilgrim", "foo", "b", "c", "b", "d", "d"]
>>> [elem for elem in li if len(elem) > 1]
['mpilgrim', 'foo']
>>> [elem for elem in li if elem != "b"]
['a', 'mpilgrim', 'foo', 'c', 'd', 'd']
>>> [elem for elem in li if li.count(elem) == 1]
['a', 'mpilgrim', 'foo', 'c']
'''
