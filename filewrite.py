for i in range(1,6):
    f=open(r"C:\Users\divya\OneDrive\Desktop\COdes\input\log{}.txt".format(i),"w+")
    for j in range(1,10):
        f.writelines("This is line no" + str(j)+ "\n")
