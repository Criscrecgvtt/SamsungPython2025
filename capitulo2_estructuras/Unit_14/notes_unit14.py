dic = {'a':10,'b':20,'c':30,'d':40}
print(dic)
dic.update(a = 90) #modifies the value of the key in the dictionary
print(dic)

#you can modify multiple files in the dictionary
dic.update(a=900, f =60)
print(dic)
#and if the item is not in there ut adds it , like f

#if the key is a number, the value may be modified by inserting a dictionary like update(dict)
dic2 = {1:'one',2:'two'}
dic2.update({1:'ONE',3:'THREE'})
print(dic2)

#Another method to do thids is by list or tuple
dic2.update([[2,'TWO'],[4,'FOUR']])
print(dic2)

#The we have setdefault taht can ONLY add it does not mofify
dic3 = {'a':10,'b':20,'c':30,'d':40}
print(dic3)
dic3.setdefault('a',9) 
print(dic3)

#popitem method, it pops any utem the beahaviour depends on the version
dic4 = {'a':10,'b':20,'c':30,'d':40}
print(dic4.popitem())

#the clear method it emptys the dictionary
dic4.clear()
print(dic4)

#print values
print(dic.values())

#prints both key and value
print(dic.items())

#pritnt it nice

for str1, num in dic.items():
    print(str1,':',num)