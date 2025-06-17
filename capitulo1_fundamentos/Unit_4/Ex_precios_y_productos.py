precio = float(input("Introduce el precio del producto :"))
dinero = float(input("Introduce el dinero entregado :"))

cambio = dinero -precio
print("El cambio es",cambio)

num500 = cambio // 500
resto = cambio % 500
num100 = resto // 100

print("Te devuelvo",num500,"billetes de 500 y",num100,"billetes de 100")