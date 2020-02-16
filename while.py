secret = 'sword'
x =''
count = 0
max = 5
auth = False
while x !=secret:
    count+=1
    if count >max:
        break
    if count == 5:
        print ("3")
        continue
    x=input(f'{count}: enter the secret word')

else:
    auth = True
    print("entered else")
print("Authorized" if auth ==True else "Locked")
