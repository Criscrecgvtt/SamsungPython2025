tup = [(), (1,), [], 'abc', (), (), (1,), ('a',), ('a', 'b'), ((),), '']
aux_tup =[]

for i in tup:
    if i: #Si esta vacío en python se evalua a false
        aux_tup.append(i)
        
print(aux_tup)