# variables
integer = 1
string = 'string'
f = 0.1

# data structures
# списки (list)
l = [1, 2, 3]
l.append(4)
first_elem = l[0]
till_second = l[:2]
for elem in l:
    print(elem)

# словари (dictionary)
d = {'a': 1, 'b': 2}
d.update({'c': 3})
c_elem = d['c']  # 3
d['d'] = 4
for k, v in d.items():
    print(k, v)
d.keys()  # ['a', 'b', 'c', 'd']
d.values()  # [1, 2, 3, 4]

# функции
def f(s: str) -> str:
    return s.lower()

d = {'a': 1}
def change_by_link(d: dict) -> dict:
    d.update({'b': 2})
    return d
d = change_by_link(d)  # {'a': 1, 'b': 2}

# try - except
try:
    a = 1 / 0
except Exception:
    print('Error of division')
