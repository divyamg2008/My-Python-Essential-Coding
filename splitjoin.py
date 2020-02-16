s = "this is the best python course I have attended until today"
print(s.split('i'))
l = s.split(' ')
print(l)
s2 = " -- ".join(l)
print(s2)

a=1
b=-1
print('{1:<+04} {0:+04}'.format(a,b))