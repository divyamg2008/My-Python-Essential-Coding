x = (1, 5, 2, 3, 11, 12)
for i,j in enumerate(x):
    print(i,j)
y = list(reversed(x))
print(x)
print(y)
z = reversed(x)
for i in z:
    print(i, end=' ')
print(sum(y, 10))
print(max(y), min(y))
a = [0, 0, 0, 0, 1, 9]
print(any(a))  # any true
print(all(x))  # all true

r = zip(a,y)
print(isinstance(r,zip))
print(id(x),id(y))

# for a, b in r:
#     while (True):
#         #print (r)
#         #print(r.__next__())
#     #print(f"{a} -> {b}")

