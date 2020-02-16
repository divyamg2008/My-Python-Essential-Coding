def f1(f):
    def f2():
        print("before fn call")
        f()
        print("after fn call")
    return f2
@f1
def f3():
    print("I am f3")

f3()
