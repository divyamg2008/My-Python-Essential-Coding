import random
def randnum1(n=1, r=5):
    while n!= 0:
        x = random.randint(0,r)
        yield x
        n-=1
# for i in randnum1(3, 6):
#     print(i)

import classiter1


for i in classiter1.randnum(4,5):
    print (i)
