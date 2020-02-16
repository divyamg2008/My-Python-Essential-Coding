a= ('abc','def','123')
b ='abc'

if b not in a:
    print(id(b),id(a[0]))

if b is not a[0]:
    print ('same')

for x in range(3):
    print(a[x])