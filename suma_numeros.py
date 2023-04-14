#Aplicación 03: Suma de n números anteriores
#Enunciado: obtener la suma de los primeros N número natural positivo.
#Análisis: Para la solución de este problema, se requiere que el usuario ingrese un número 
#y el sistema realice el proceso para devolver la suma de los N primeros números.

numero = int(input("ingrese un nuemero: "))

suma = 0

for i in range(1, numero + 1):
    suma += i
    print("la suma de numeros anteriores es: ",suma)