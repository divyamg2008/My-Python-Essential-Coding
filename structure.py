x = {111, 222, 3}
print(type(x))

x = "hello I am Divya"
y = x.split()


def show(y):
    for i in y:
        if i == "am":
            print(y.index("am"))
            y.append("Mary")
            y.insert(-1, "George")
            y.remove("am")
            z = y.pop(3)
            print(z)
        print(i, end=' ', flush=True)


print(y)


show(y)

print(y)

q = [1, 2, 3, 4, 5, 6, 7, 8]
del q[0:2]

print(q)
