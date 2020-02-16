

for i in range (100):
    if i<=1:
        continue
    else:
        for x in range (2,i):
            if (i%(x)==0):
                #print(f"{i} is not prime")
                break
        else:
             print(f"{i}", end = ' ')


