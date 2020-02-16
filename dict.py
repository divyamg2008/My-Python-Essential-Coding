a = {1: 'one', 2: 'two', 3: 'three'}
for i in a:
    print(f"{i}:{a[i]}")
for k, v in a.items():
    print(f"{k}:{v} from items")

b = dict()

b[0] = 'onenow'
b[1] = 'two'
print(b)
for k, v in b.items():
    print(k, v)
for k in b.keys():
    print(k)
for v in b.values():
    print(v)
print(b.get(0))
print(1 in b)
