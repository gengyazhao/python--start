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
