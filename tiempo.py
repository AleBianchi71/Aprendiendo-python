# Variables / Ingresar Datos
tiempoSegundos = input('Tiempo en Segundos: ')
HORA = 3600
MINUTO = 60

# Convertir de str a int
tiempoSegundos = int(tiempoSegundos)

# Solución 
h = tiempoSegundos // HORA
tiempoSegundos = tiempoSegundos % HORA
m = tiempoSegundos // MINUTO
s = tiempoSegundos % MINUTO

# Mostrar datos en pantalla 
print('Horas: ', h)
print('Minutos: ', m)
print('Segundos: ', s)