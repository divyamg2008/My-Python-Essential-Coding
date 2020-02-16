x = 3
y = 'ttt'
print("the variables are {aa} and {bb}".format(aa=x, bb=y))
print("the variables are {0:<-05}, {0:+05} and {1}".format(x, y))
a = 4989
b = 654
print("{:,}".format(a*b).replace(',', '.'))
print("{:,.3f}".format(a*b))
print("{:0x}".format(a*b))
print("{:b}".format(a*b))
print(f"{a*b:,.3f}")

s= 'tEST'
t = 'Test'
print(t.swapcase()==s)

print('hello \n world')