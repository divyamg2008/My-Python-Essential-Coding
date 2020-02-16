days = ['sun','mon','tue','wed','thu','fri','sat']

# n = 0
# while n < 7:
#     print (days[n]) 
#     n+=1

for x in days:
    if x =='sat':continue
    print(x)
else:
    print("loop printed")