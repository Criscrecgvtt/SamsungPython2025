from collections import defaultdict
#1.Converting List and tupple into dictionary
    
#1.1 From Lists
keys = ['a','b','c','d']
x = dict.fromkeys(keys)
print(x)

#1.1 From tuples
keys = ('a','b','c','d')
x = dict.fromkeys(keys)
print(x)

#1.2 You can add a default value to the dict like this
y = dict.fromkeys(keys,100)
print(y)

#generadores, si lo usasa luego se quedara en en el ultimo como un puntero
g = (x for x in range(10))
print(g)

#1.4 How to use defaultdic, it creates a default dict with vaues of 0
z = y
z = defaultdict(int)
print(z['z'])  #There is no key z in the dictionary but 
#so you can use default dic as a counter as it automaticalaly puts o un all the values
counter = defaultdict(int)
print(counter)