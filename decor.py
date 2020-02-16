def f1():
    print("f1")

    def f2():
        print("f2")  
          
        def f3():
            print("f3")
            return 4
        return f3
    return(f2)


x = f1()  # x has return f2
print(x)
y = x()
print(y)
z = y()
print(z)
