import time


def sumTime(sum):
    def calc():
        t1 = time.time()
        sum()
        t2 = time.time()
        total = t2-t1
        print(f"{total*1000} ms")
    return calc


@sumTime
def sum():
    x = []
    for i in range(0, 100, 1):
        x.append(i)
    print(x)


print("sum")
sum()
print("r")
r = sumTime(sum)
r()
