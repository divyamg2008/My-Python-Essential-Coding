f = open('log1.txt','r+')
count = 0
for i in range(1, 10):
    count += 2

    f.write(f"aaaaaaaaAh {i:05} + this is a disaster{count:+3}\n")
    
