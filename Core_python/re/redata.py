import re

with open('data.txt', 'r') as f:
    data = (f.readlines())

# 搜索
patt1 = '\d+-\d+-\d+'
re1 = re.search(patt1, data[0])
print(re1.group())

# 匹配(贪婪匹配)
patt2 = '.+(\d+-\d+-\d+)'
re2 = re.match(patt2, data[0])
print(re2.group(0))
print(re2.group(1))  # 贪婪导致的结果

# 非贪婪
patt3 = '.+?(\d+-\d+-\d+)'  # 非贪婪操作符 ‘?’
re3 = re.match(patt3, data[0])
print(re3.group(0))
print(re3.group(1))