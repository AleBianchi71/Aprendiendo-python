#Aplicación 02: Crear un sistema que detecte si un carácter es vocal o no
#Enunciado: dado un carácter determinar si es una vocal.
#Análisis: para la solución de este problema, se requiere que el usuario ingrese un carácter
# y el sistema verifique si es una vocal.




letra = str(input( "\n   Introduzca una letra: " ))
 

if ( letra == 'a' or letra == 'A' or
         letra == 'e' or letra == 'E' or
         letra == 'i' or letra == 'I' or
         letra == 'o' or letra == 'O' or
         letra == 'a' or letra == 'U' ):
        print( "\n   ES UNA VOCAL" );
else:
        print( "\n   NO ES UNA VOCAL" );



