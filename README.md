# python--start
python 学习入门笔记
----------------------------------------------------------------------------
import re
p = re.split('(\W+)','runoob,runoob,runoob.')
p1 = re.split('\W+','runoob,runoob,runoob.')

['runoob', ',', 'runoob', ',', 'runoob', '.', '']
['runoob', 'runoob', 'runoob', '']
----------------------------------------------------------------------------
import re
def double(matched):
    value = int(matched.group('value'))
    print(value*2)
    return str(value * 2)
s = 'A23G4HFD567'
p = re.sub(r'(?P<value>\d+)',double,s)
print(p)
  
46
8
1134
A46G8HFD1134
----------------------------------------------------------------------------
import re
p = re.compile(r'\b(\w+)\s+\1\b')
q = p.search('hu wi ji zhan hi shi ha ha wi de').group()
print(q)
# 这是一个国外电话号码
phone = '2004-959-559 # 这是一个国外电话号码'
num = re.sub(r'#.*$','',phone)#从#开始匹配，匹配{0，}任何字符，直到字符串结尾        ''替换字符串为空
number = re.sub(r'[^\d-]','',phone)#匹配非数字 ，非-
print(num)
print(number)

# num = re.sub(r'[^0-9]','',phone)
num = re.sub(r'\D','',phone)
print(num)
  
ha ha
2004-959-559 
2004-959-559
2004959559
---------------------------------------------------------------------------- 
包（Packages）、模块（Module）名使用意义完整的英文描述，采用小写加下划线（lower_with_under）的风格命名；
类（Class）名使用意义完整的英文描述，采用大写字母开头的单词（CapWords）风格命名；
函数（Function）、方法（Method）、函数参数（Function Parameters）使用意义完整的英文描述，采用小写加下划线（lower_with_under）的风格命名；

任何模块代码的第一个字符串都被视为模块的文档注释；

默认情况下，python解释器会搜索当前目录、所有已安装的内置模块和第三方模块，搜索路径存放在sys模块的path变量中。
通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类。

继承和多态
继承的子类获得了父类的全部功能，
当子类和父类存在相同的方法时，子类的方法覆盖了父类的方法，在代码运行的时候，总是会调用子类的方法。这就是继承的另一个好处：多态。
子类只需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写。

如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法

