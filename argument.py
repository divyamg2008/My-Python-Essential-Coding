a = ("sun", "mon", "tue")

def days(*args):
    for each in (args):
        print (each)
        

days(*a)




def match(**kwargs):
    for each in kwargs:
        print (each, kwargs[each])

b= dict(filen='log1',lno = 27, description ='no file found')
match(**b)