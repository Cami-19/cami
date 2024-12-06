# parte 1: condicionales
#1-1
#n = int(input("ingresa un numero: "))


#if n % 2 == 0:
   # print(f"{n} es par")

#else:
    #print(f"{n} es impar")
    
#1-2

#numero = int(input("imgresa un numero aleatorio: "))
#contador=0
#if numero>0 and numero<1000:
    #while(numero>0):
        #numero=numero//10
        #contador=contador+1
    #print("el numero tiene ", contador, "cifras")
#else:
   # print("numero fuera de rango...")


#parte 2: bucles con listas

#n=int(input("cuantos empleados tiene la empresa: "))

#x =1
#contador1=0
#contador2=0
#gastos=0

#while x<=n:
    #sueldo=float(input("ingrese el sueldo del empleado: " ))
    #if sueldo >=1000000 and sueldo<=3000000:
        #contador1=contador1+1

        

   # elif sueldo >3000000 and sueldo<=5000000:
       # contador2=contador2+1
    
  #  x=x+1
  #  gastos=gastos+sueldo
#print(f"total de trabajadores que cobran entre el 1000000 y 3000000: {contador1}")
#print(f"total de trabajadores que cobran mayor a 3000000 y 5000000: {contador2}")
#print(f"total de gasto de la empresa: {gastos}")

#2-1

cont1 =0
cont2 =0
cont3 =0
cont4 =0

n =int(input("cantidad de puntos: "))
for i in range(n):
    print(f"punto {i+1}: ")
    x=int(input("ingrese la coordenada x: "))
    y=int(input("ingrese la coordenada y: "))

    if x >=0 and y >=0:
        cont1=cont1+1

    elif x <0 and y >=0:
        cont2=cont2+1
    
    elif x <0 and y <0:
        cont3=cont3+1
    
    elif x >=0 and y <0:
        cont4=cont4+1

print(f"numero de puntos del cuadrante 1: {cont1}")
print(f"numero de puntos del cuadrante 2: {cont2}")
print(f"numero de puntos del cuadrante 3: {cont3}")
print(f"numero de puntos del cuadrante 4: {cont4}")

        




    

  







