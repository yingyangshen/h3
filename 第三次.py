#作业
lines={}
b=[]
f=open('hello.txt','r')
for line in f.readlines():
    line=line.strip()
    k=line.split()[0]
    v1=line.split()[1]
    v2=line.split()[2]
    v=v1+" "+v2
    b.insert(-1,v1)
    b.insert(-1,v2)
    lines[k] = v
f.close()
print(lines)
c=set(b)
print(c)
#判断重复方法一(基础版）
if len(c) < 18:
    print("\n有人重复了")
else:
    print("\n没有人重复")
#判断重复方法二（进阶版）
dict={}
for key in b:
    n=dict.get(key,0)+1
    dict[key]=n
    if n>1:
        print(key)
        print(key,"出现重复的情况")
    else:
        continue
print(dict)

#运行结果
#{'python学习': '咖喱 胡骞', 'leetcode刷题': '老表 陈焕森', '编程集训': '孙超 小熊', '统计学': '李奇峰 蓝昔', 'ML项目实践': '杨冰楠 孙涛', '高级算法梳理': '于鸿飞 小雪', '基础算法梳理': 'sm1les 钱令武', '知乎小组': '李严 黑桃', '学习群': '咖喱 排骨'}
#{'黑桃', '小熊', '李奇峰', '孙超', 'sm1les', '李严', '排骨', '蓝昔', '咖喱', '于鸿飞', '陈焕森', '杨冰楠', '胡骞', '孙涛', '小雪', '钱令武', '老表'}

#有人重复了
#咖喱
#咖喱 出现重复的情况
#{'胡骞': 1, '老表': 1, '陈焕森': 1, '孙超': 1, '小熊': 1, '李奇峰': 1, '蓝昔': 1, '杨冰楠': 1, '孙涛': 1, '于鸿飞': 1, '小雪': 1, 'sm1les': 1, '钱令武': 1, '李严': 1, '黑桃': 1, '咖喱': 2, '排骨': 1}



#【dict字典】
#定义：在Python中，字典 是一系列键—值对 。每个键 都与一个值相关联，你可以使用键来访问与之相关联的值。与键相关联的值可以是数字、字符串、列表乃至字典。事实上，可将
#任何Python对象用作字典中的值。
#创建
#字典的相关方法
#1添加元素
#举例：alien_0 = {'color': 'green', 'points': 5}
#print(alien_0)
#alien_0['x_position'] = 0
# alien_0['y_position'] = 25
#print(alien_0)

#2修改元素
#alien_0 = {'color': 'green'}
#print("The alien is " + alien_0['color'] + ".")
#alien_0['color'] = 'yellow'
#print("The alien is now " + alien_0['color'] + ".")

#8.3删除元素
#alien_0 = {'color': 'green', 'points': 5}
#print(alien_0)
#del alien_0['points']
#print(alien_0)

#favorite_languages = {'jen': 'python','sarah': 'c','edward': 'ruby','phil': 'python',}
#print("Sarah's favorite language is " +  favorite_languages['sarah'].title() + ".")

#3.遍历
#ser_0 = {'username': 'efermi','first': 'enrico','last': 'fermi',}
#for key, value in user_0.items():
# print("\nKey: " + key)
# print("Value: " + value)

#favorite_languages = {'jen': 'python','sarah': 'c','edward': 'ruby','phil': 'python',}
# for name, language in favorite_languages.items():
# print(name.title() + "'s favorite language is " +language.title() + ".")

#favorite_languages = {'jen': 'python','sarah': 'c','edward': 'ruby','phil': 'python',}
#for name in favorite_languages.keys():
#print(name.title())

#alien_0 = {'color': 'green', 'points': 5}
#alien_1 = {'color': 'yellow', 'points': 10}
#alien_2 = {'color': 'red', 'points': 15}
#aliens = [alien_0, alien_1, alien_2]
#for alien in aliens:
#print(alien)

names = ['Michael', 'Bob', 'Tracy']
scores = [95, 75, 85]

#【set集合】
#特性:set 和 dict 类似，也是一组 key 的集合，但不存储 value。由于 key 不能重复，所以，在 set中，没有重复的 key。
#创建
#方法

#>>> s = set([1, 2, 3])
#>>> s
#set([1, 2, 3])

#>>> s.add(4)
#>>> s
#set([1, 2, 3, 4])
#>>> s.add(4)
#>>> s
#set([1, 2, 3, 4])

#>>> s.remove(4)
#>>> s
#set([1, 2, 3])

#set 可以看成数学意义上的无序和无重复元素的集合，因此，两个 set 可以做数学意义上的交集、并集等操作：
#>>> s1 = set([1, 2, 3])
#>>> s2 = set([2, 3, 4])
#>>> s1 & s2
#set([2, 3])
#>>> s1 | s2
#set([1, 2, 3, 4])

#文件编写
#读写文件是最常见的 IO 操作。Python 内置了读写文件的函数，用法和 C 是兼容的。
#读写文件前，我们先必须了解一下，在磁盘上读写文件的功能都是由操作系统提供的，现
#代操作系统不允许普通的程序直接操作磁盘，所以，读写文件就是请求操作系统打开一个
#文件对象（通常称为文件描述符），然后，通过操作系统提供的接口从这个文件对象中读
#取数据（读文件），或者把数据写入这个文件对象（写文件）。

#try:
#f = open('/path/to/file', 'r')
# print f.read()
#finally:
# if f:
# f.close()

#with open('/path/to/file', 'r') as f:
#print f.read(）

#编写
#with open('/Users/michael/test.txt', 'w') as f:
#f.write('Hello, world!')

#作业
lines={}
b=[]
f=open('hello.txt','r')
for line in f.readlines():
    line=line.strip()
    k=line.split()[0]
    v1=line.split()[1]
    v2=line.split()[2]
    v=v1+" "+v2
    b.insert(-1,v1)
    b.insert(-1,v2)
    lines[k] = v
f.close()
print(lines)
c=set(b)
print(c)
#判断重复方法一
if len(c) < 18:
    print("\n有人重复了")
else:
    print("\n没有人重复")
#判断重复方法二
dict={}
for key in b:
    n=dict.get(key,0)+1
    dict[key]=n
    if n>1:
        print(key)
        print(key,"出现重复的情况")
    else:
        continue
print(dict)




