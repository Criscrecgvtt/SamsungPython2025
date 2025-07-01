tp = (1, 2, 5, 4, 3, 2, 1, 4, 7, 8, 9, 9, 3, 7, 3, 9)
max_elem = 0
max_frec = 0
hash_aux = {}

for i in tp:
    if i in hash_aux :
        temp_frec = hash_aux[i]
        temp_frec += 1
        hash_aux[i] = temp_frec
        if temp_frec>max_frec:
            max_elem = i
            max_frec = temp_frec
        elif temp_frec == max_frec:
            if i >max_elem:
                max_elem = i
             
    else:
        hash_aux[i]= 1

print("El elmento mas frecuente es", max_elem)