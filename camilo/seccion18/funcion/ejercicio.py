n = int(input("Cuántas personas quieres procesar? "))

menores = 0
mayores = 0
total_edades = 0

i = 0

while i < n:
    edad = int(input("Digita una edad: " + str(i + 1) + ": "))
    
    if edad < 18:
        menores += 1
    elif edad >=18:
        mayores += 1
    
    total_edades = total_edades + edad
    i += 1

print("total de personas menores de 18 años:", menores)
print("total de personas mayores o iguales a 18 años:", mayores)
print("total acumulado de las edades:", total_edades)