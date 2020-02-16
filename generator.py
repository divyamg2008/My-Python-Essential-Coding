

def inclu_range(*args):
    start = 0
    step = 1

    if(len(args) < 1):
        raise TypeError("less arguments")
    elif(len(args) == 1):
        stop = args[0]
    elif(len(args) == 2):
        start = args[0]
        stop = args[1]
    elif(len(args) == 3):
        start = args[0]
        stop = args[1]
        step = args[2]
    else:
        raise TypeError("too many arguments")

    i = start
    while i <= stop:
        yield i
        i += step


for i in inclu_range(2, 10):
    print(i, sep=' ')
