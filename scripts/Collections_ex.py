from collections import namedtuple

a =namedtuple('cource', 'name, technology')
s = a('data sciance', 'python')
s = a('data structure', 'pythonNew')
print(s.count(a))
print(s)
