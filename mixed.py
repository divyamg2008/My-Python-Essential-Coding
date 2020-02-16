d = dict(one='r', tw0='hahah')
li = [d, 1, 2, 3]
s = "This is my name"
se = set("you are my best friend")
t = (5, 6, 'rrr')
mixed = [d, li, s, t, se]
print(mixed)

if isinstance(li, tuple):
    print(li)
print(type(mixed))
