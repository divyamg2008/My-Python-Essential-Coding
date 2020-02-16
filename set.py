a = set("Hello this is my set")
b = set("This is my second set called zzz")
print(a)
print(sorted(a))

for x in a:
    print(x, end=' ')

print(a - b)
print(a | b)
print(a ^ b)
print(a & b)
