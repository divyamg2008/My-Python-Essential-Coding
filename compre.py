from math import pi
list1 = range(11)
list2 = [x*2 for x in list1]
list3 = [(x, x ** 2) for x in list1 if x % 3 == 0]
list4 = [round(pi, x) for x in list1]
list5 = [dict(x=x * 2) for x in list1]
list6 = {x: x*2 for x in list1}
list7 = {x for x in 'superDuper' if x not in 'p'}


def print_list(list):
    for i in list:
        print(i, end=' ')


print_list(list1)
print_list(list2)
print_list(list3)
print_list(list4)
print(list5)
print(list6)
print(list7)
