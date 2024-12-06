#1.Decraracion de variables
x=int(input("ingresa un entero: "))
w=float(input("ingresa un número flotante: "))
y=(input("ingresa cadena de caracteres: "))
z=input("¿todo perfecto? ")

print(x,w,y,z)
print("tu edad: " , x)
print("ingresa un valor en decimal: ", w)
print("¿cual es tu nombre?: ", y)
print("como te encuetras?: ", z)

#2.Operaciones Matematicas

numero1=int(input("valor del numero 1: "))
numero2=int(input("valor del numero 2: "))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2

print("la suma de:",numero1,"y",numero2,"es", suma )
print("la resta de:",numero1,"y",numero2,"es", resta )
print("la multiplicacion de:",numero1,"y",numero2,"es", multiplicacion )
print("la division de:",numero1,"y",numero2,"es", division )

#3.Manipulacion de cadena

a = input("escribe una frase: ")
b = input("escribre otra frase: ")
c = a +" "+ b
print(c)


print(f"esta es la concatenacion: {a} {b}")

#4.trabajar con lista
lista = [2,3,4,5,6,7,8,9,10,"dap"]
print(lista)

#cambiar dap por cami
lista[9]="cami"
print(lista)

lista.append("martin")
print(lista)

lista.pop(3)
print(lista)

lista.remove("martin")
print(lista)

#5.Uso de diccionario

persona={
    "nombre":"Camilo",
    "edad": 19,
    "ciudad":"Santa marta",
    "profesion": "Ingeniero de sistemas"
}
print("Diccionario actualizado:", persona)

#agregar un nuevo par clave-valor
persona["hobby"]="leer"
print("diccionario actualizado:",persona)

#modificar valores en el diccionario
persona["edad"]=26
print("diccionario actualizado:",persona)

