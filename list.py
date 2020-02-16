num = list (range(5,50,5))
num[2] = 100
for i in num:
    print(f"Element {i:<5}")

# d = {1: 'sun', 2: 'mon'}
# for i,j in d.items(): # a function that will unpack a dictionary
#     print (f"{i:>5} {j}")

t= (1,2, "2333", ['a',2], 3)
s= (1,2,3, "2333", ['a',2])
r= (1,2,3, "2333", ['a',2])
print (id(t[4]))
print(id(s[2]))
print(type(t))
if t[4] is s[2]:
    print ("yep")

print(isinstance(t,tuple))
if r==s:
    print("ooook")
print('{1} {0}'.format('a','b'))
print(f'{"b"} {"a"}')