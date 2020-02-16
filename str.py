print("""hello 
            World
        I like
        ....
        """.lower())

class Mystr(str):
    def __str__(self):
        return self[::-1]

s = Mystr("hello who is it")
print (s)

print("heLLO 123$#%^&".casefold())
print("heLLO 123$#%^&".capitalize())
print("heLLO 123123$#%^&".count('123'))

