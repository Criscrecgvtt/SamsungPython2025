def hanoi(n, origen, auxiliar, destino):
    if n == 1:
        print(f"Mover disco 1 de {origen} a {destino}")
        return
    
    # Mover n-1 discos del origen al auxiliar
    hanoi(n - 1, origen, destino, auxiliar)
    
    # Mover el disco más grande al destino
    print(f"Mover disco {n} de {origen} a {destino}")
    
    # Mover los n-1 discos del auxiliar al destino
    hanoi(n - 1, auxiliar, origen, destino)

# Ejemplo: mover 3 discos de A a C usando B
hanoi(5, 'A', 'B', 'C')
