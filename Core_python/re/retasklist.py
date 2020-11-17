import re

"""
patt = '\w+@(\w+.)?\w+\.com'
res = re.match(patt, 'nobody@www.com').group()
print(res)

s = 'This and that.'
res1 = re.finditer(r'(th\w+) and (th\w+)', s, re.I)
print(next(res1).groups())
"""
with open('tasklist.txt', 'r') as f:
    for eachLine in f:
        print(re.findall(
            r'([\w.]+(?: [\w.]+)*)\s\s+(\d+) \w+\s\s+\d+\s\s+([\d,]+ K)',
            eachLine.rstrip()))
