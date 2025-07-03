#1.Creating a set
""" Características : 
    - Unordered
    - Mutable
    - Iterable
    - No indexado
"""
set1 = {1,2,3,4} 
set2 = set((1,2,3,4)) #With the function set you can make froma tuples or lists

# a set is a collection of elements that are not in order, the index cannot be used
#slicing is impossible

days_list = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']  # list
days_set = set(days_list)   # making sets from list
print(days_set)


fruits_tuple = ('apple', 'orange', 'water melon')  # tuple
fruits_set = set(fruits_tuple)  # making sets from tuple
print(fruits_set)


#2.Check the specific value in the set
numbers ={2,1,3}
if 1 in numbers:
    print("1 is in the set") 

#2.2 Indexing in sets
numbers ={1,2,3}
numbers.add(4)
print(numbers)

numbers.remove(4)
print(numbers)

#4.Set Calculation

#Union calculation 
s1={1,2,3,4,5,6}
s2 ={4,5,6,7,8,9}
print(s1|s2)
print(s1.union (s2))

#Intersection calculation
print(s1&s2)
print(s1.intersection(s2))

#Difference of sets calculation
print(s1-s2)
print(s1.difference(s2))

#Symmetric diference of set calculations
print(s1^s2)
print(s1.symmetric_difference(s2))

#Methods of sets

"""
methods                    role
------------------------   --------------------------------------------------------
add(x)                    Add element x to the set.
discard(x)                Delete element x from the set.
clear                     Delete all elements in the set.
union(s)                  Find union with set s. Same as | operator.
difference(s)             Find difference of set with set s. Same as – operator.
intersection(s)           Find intersection of set with set s. Same as & operator.
symmetric_difference(s)   Find symmetric difference of set with set s. Same as ^ operator.
issubset(s)               Find if set s is a subset. Return True/False.
issuperset(s)             Find if set s is a superset. Return True/False.
isdisjoint(s)             Find if set s is a coprime. Return True/False.
"""

#Calculing subset and superset
s1 = {1, 2, 3, 4, 5}
s2 = {1, 2, 3}        # is s1’s subset
s3 = {1, 2, 6}        # not s1’s subset

s2.issubset(s1)       # method asking if s2 is subset of s1
# True

s3.issubset(s1)       # method asking if s3 is subset of s1
# False

s1.issuperset(s2)     # method asking if s1 is superset of s2
# True

s1.issuperset(s3)     # method asking if s1 is superset of s3
# False

#5.Set Comparison
A = {1,2,3}
B = {1,2,3}

A == B #True
A = {1, 2, 3, 4, 5}
B = {1, 2, 3}

B < A   # True subset: B is subset of A and B ≠ A
# Output: True

#6.Iteration Statements and Sets
for i in A:
    print(i,end=" ")

#No estan ordenados, pero los podemos ordenar con sorted
# Sorted devuelve una lista