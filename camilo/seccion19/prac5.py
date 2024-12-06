#ingresar n valores

#muestre la cantidad de valores mayores o iguales a 1000

#muestre la cantidad de mavores menores a 1000 usando el ciclo for
saco1=0
saco2=0
suma1=0
suma2=0

n = int(input("ingrese n valores: "))

for j in range(n):
    valor = int(input("ingrese valor: "))
    if (valor>=1000):
        saco1=saco1+1
        suma1=suma1+valor

    else:
        saco2=saco2+1
        suma2=suma2+valor

print(f"los mayores o iguales a 1000 son: {saco1}")
print(f"los menores a 1000 son: {saco2}")

#sumar los mayores y los menores


