#   EJERCICIO 1
# Defina una variable edad y asignale un numero entero
# Muestra su valor por pantalla
# Define otra variable edad_cadena que contenga el valor de edad como una cadena de caracteres
# Comprueba el tipo de la nueva variable
# Utiliza la variable edad que has definido previamente y calcula la edad que tendría esa persona en el año 2035

#   Define la variable
edad = 26

print("La edad del pibe es "+str(edad))

#   Define la variable en str (caracter)
edad_cadena = str(edad)

#   Se muestra por pantalla
print(edad_cadena)

#   Ves de que tipo es la variable de la variable llamada
print(type(edad_cadena))

# Se calcula 2035 - 2020 (para sacar la diferencia del año) y se le suma la edad, para que de el total
calculo = (2035 - 2020) + edad


#   Se muestra por pantalla el resultado
print(calculo)




#   EJERCICIO 2
# Se entrega el nombre del alumno al revez
# NOMBRE APELLIDO ha sacado un NOTA
# VIDEO PARA ENTEDER EL EJERCICIO --> https://www.youtube.com/watch?v=lcv7NsEBU7E

cadena = "naitsirC sotsuB , 01"

cadena_volteada = cadena[::-1]

# Bustos Cristian, 10 ( ASI QUEDA )

print(cadena_volteada[4::], "ha sacado un ", cadena_volteada[:2])


#   EJERCICIO 3
# Utilizando operadores lógicos (AND, OR, O) determine si una cadena de texto introducido por el usuario tiene
# una longitud mayor o igual a 3 y menor o igual a 12

#   ACA SE PIDE AL USUARIO UN VALOR
texto = input("Escriba una cadena de caracteres: ")

#   len() esto cuenta una por una las letras de una palabra
#   if se usa como un SI pasa esto, tanto. El else se usa para como un SINO pasa esto.

if(len(texto) >= 3 and len(texto) <= 12):
   print("La cadena es correcta")
else:
    print("La cadena es incorrecta")



# EJERCICIO 4
# Realiza un programa que lea 2 numeros por teclado y determine los sigueintes aspectos
# Los 2 numeros son iguales?
# Los 2 numeros son diferntes?
# El primero es mayor al segundo?
# El segundo es mayor o igual que el primero?

n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))
flag = False
iguales = False
mayor = 0
diferentes = False

if(n1 > n2):
    flag = True
    mayor = n1
    diferentes = True
    print("El mayor es: "+str(mayor))
if(n2 >= n1):
    flag = True
    mayor = n2
    diferentes = True
    print("El mayor es: "+str(mayor))
if(n1 == n2):
    iguales = True
    diferentes = False
if(iguales == True):
    print("Los numeros son iguales")
if(diferentes == True):
    print("Los numeros son diferentes")

