magnitud = input("¿Qué magnitud quieres calcular: masa (m), densidad (d) o volumen (v)? ")

if magnitud == "m":
    densidad = float(input("Dime la densidad de la sustancia: "))
    volumen = float(input("Dime el volumen de la sustancia: "))
    print("La masa es {:.2f}".format(volumen * densidad))

elif magnitud == "d":
    masa = float(input("Dime la masa de la sustancia: "))
    volumen = float(input("Dime el volumen de la sustancia: "))
    if volumen == 0:
        print("Error: No es posible la idvision por 0.")
    else:
        print("La densidad es {:.2f}".format(masa / volumen))

elif magnitud == "v":
    masa = float(input("Dime la masa de la sustancia: "))
    densidad = float(input("Dime la densidad de la sustancia: "))
    if densidad == 0:
        print("Error: No es posible la division por 0")
    else:
        print("El volumen es {:.2f}".format(masa / densidad))

else:
    print("Esta opción no existe, no es una magnitud válida")