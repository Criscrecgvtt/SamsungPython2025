t1 ='a','b','c' #t1 es una tupla
t2 = ('a','b','c')
t3 = ('d','e')

print(t1 == t2)
print(t1>t3)
print(t1<t3)
print(t2+t3)
print(list(t2+t3))#reconvierta la tupla a lista
print([t2+t3])#una lista cuyo primer elemtno es una tupla
print(t1)