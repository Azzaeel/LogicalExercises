#Diccionarios
#
#diccionario = {
#    "clave1" : "valor1",
#    "clave2" : "valor2",
#    "clave3" : "valor3"
#}
#

#diccionario["clave4"] = "valor"
#
#Imprimir el diccionario
#
# print(diccionario)
# print(diccionario["clave1"])
#
# for n  in diccionario:
#     print(diccionario[n])
#
#Eliminar un elemento del diccionario

#diccionario.popitem()
#
#for n  in diccionario.values():
#     print(n)
#


# class Arreglo:

#     def __init__(self):
#         self.__length = 0
#         self.__values = {}
    
#     def pop(self, index=-1):
#         if self.__length > 0:
#             if 0 <= index < self.__length:
#                 for n in range(index, self.__length - 1):
#                     self.__values[n] = self.__values[n + 1]
#                 self.__values.popitem()
#             else:
#                 self.__values.popitem()
#             self.__length -= 1
#         return self.__values
    
#     def append(self, value):
#         self.__values[self.__length] = value
#         self.__length += 1

#     def mostrar(self):
#         return self.__values

#     def getLength(self):
#         return self.__length



# arreglo = Arreglo()
# arreglo.append(2)
# arreglo.append(3)
# arreglo.append(4)
# arreglo.append(5)
# arreglo.pop(1)
# print(arreglo.mostrar())




# class Lista:

#     def __init__(self):
#         self.__values = {}
#         self.__length = 0

#     def append(self, value):
#         self.__values[self.__length] = value
#         self.__length += 1

#     def pop(self, index=-1):
#         try:
#             if 0 < index >= self.__length:
#                 self.__values.pop(index)
#             else:
#                 self.__values.popitem()
#             self.__length -= 1
#             return self.__values
#         except:
#             return None

#     def Length(self):
#         return self.__length

#     def getValue(self, index):
#         try:
#             return self.__values[index]
#         except:
#             return None

#     def getValues(self):
#         return self.__values


# listaDeMaterialesLuis = Lista()

# nombre = input("""Hola, ¿Cómo es tu nombre?
# """)

# elemento = input(
#     "¡Hola %s! Digita un elemento que quieras agregar a tu Lista [Enter finalizar la ejecución]: " % nombre)

# while elemento != "":
#     listaDeMaterialesLuis.append(elemento)
#     elemento = input("Luis, Digita otro elemento a tu lista [Enter para finalizar la ejecución]: ")

# listaDeMaterialesLuis.pop()
# print("La cantidad de materiales en su lista es de: %i" % listaDeMaterialesLuis.Length())
# print("Tu lista de materiales es:")
# for n in range(listaDeMaterialesLuis.Length()):
#     print("%i.%s" % (n + 1, listaDeMaterialesLuis.getValue(n)))


#print("En el Ñágara encontré un Ñandú")


#Ejercicios de universidad de python

#1: Califica tu dia

#calificacion = input("Como estuvo tu dia (1 al 10): ")
#print("mi dia estuvo de: ", calificacion)


#2: El libro

#titulo = input("Proporciona el título: ")
#autor = input("Proporciona el autor: ")
#
#print(titulo, "fue escrito por", autor)


#3: Circulos

#radius = int(input("Ingrese el radio: "))
#pi = 3.1416
#perimeter = 2 * pi * radius
#area = pi * radius**2
#print(perimeter)
#print(area)

#4: Promedio

#primera = int(input("Ingrese la primera nota: "))
#segunda = int(input("Ingrese la segunda nota: "))
#tercera = int(input("Ingrese la tercera nota: "))
#cuarta = int(input("Ingrese la cuarta nota: "))
#
#suma = primera + segunda + tercera + cuarta
#promedio = suma / 4
#print("El promedio es:", promedio)


#5: Conversor de cm a pulgadas

#cm = int(input("Ingrese la longitud"))
#pulgadas = cm/2.54
#print(cm, "cm =", pulgadas, "in")


#6: Area y perimetro de un cuadrilatero

#alto = int(input('Proporciona el alto: '))
#ancho = int(input('Proporciona el ancho: '))
#
#area = alto * ancho
#perimetro = (alto + ancho)**2
#
#print(f'Area: {area}')
#print(f'Perímetro: {perimetro}')


#7: Par o impar 

#a = int(input('Ingrese un numero '))
#
#if a % 2 == 0:
#    print(f'El número ingresado {a} es par')
#else:
#    print(f'El número ingresado {a} es impar')


#8: Mayor de edad

#edad = int(input('Escribe tu edad '))
#
#if edad >= 18:
#    print('Usted es mayor de edad')
#else:
#    print('Usted es menor de edad')


#9: Valor dentro de un rango (Operador and)

#valor = int(input('Escribe el valor: '))
#valorMinimo = 0
#valorMaximo = 5
#
#dentroRango = valor >= valorMinimo and valor <= valorMaximo
#
#if dentroRango:
#    print(f'El valor {valor} está dentro de rango')
#else: 
#    print(f'El valor {valor} está fuera de rango')


#10: Asistencia del padre (Operador or)

#vacaciones = True
#diaDescanso = True
#
#if vacaciones or diaDescanso:
#    print('Puede asistir al juego')
#else:
#    print('No puede asistir al juego')


#11: rango entre 20's y 30's

#edad = int(input('Introduce tu edad '))
#
#veintes = edad >= 20 and edad < 30
#treintas = edad >= 30 and edad < 40
#
#if veintes or treintas:
#    print("Tu edad se encuentra en el rango de 20's y 30's")
#else:
#    print("Tu edad no se encuentra en el rango de 20's y 30's")


#12: Numero mayor

#numero1 = int(input('Proporciona el numero1: '))
#numero2 = int(input('Proporciona el numero2: '))
#
#if numero1 > numero2:
#    print(f'El mumero mayor es: {numero1}')
#elif numero2 > numero1:
#    print(f'El numero mayor es: {numero2}')
#else:
#    print('Los numeros son iguales')



#13: Tienda de libros

#print('Proporcione los siguientes datos del libro')
#nombre = input('Proporcione el nombre: ')
#ide = int(input('Proporcione el ID: '))
#precio = int(input('Proporcione el precio: '))
#envioGratis = input('Indica si el servicio es gratuito (si/no): ')
#
#if envioGratis == 'si':
#    envioGratis = True
#elif envioGratis == 'no':print(f'La palabra {val1} tiene {i} letras mas que {val2}')
#    envioGratis = False
#else:
#    envioGratis = 'Valor incorrecto'
#
#print(f'''Id: {ide}
#    Nombre: {nombre}
#    Precio: {precio}
#    Envio gratuito: {envioGratis}
#''')


#14: Numero invertido

#num = input('Ingrese un numero ')
#print(num[::-1])


#15: Pitagoras

#catetoA = int(input('Ingrese el cateto a '))
#catetoB = int(input('Ingrese el cateto b '))
#
#hipotenusa = catetoA ** 2 + catetoB ** 2
#raiz = hipotenusa ** (1/2)
#print(raiz)


#16: convercion de numeros del uno al tres de numero a texto

#numero = int(input('Proporcione un numero del 1 al 3: '))
#numtex = ''
#
#if numero == 1:
#    numtex = 'Número uno'
#elif numero == 2:
#    numtex = 'Número dos'
#elif numero == 3:
#    numtex = 'Número tres'
#else:
#    numtex = 'fuera de rango'
#    
#
#print(f'El numero proporcionado es igual a {numtex}')


#17: Calcular la estacion segun el mes proporcionado

#mes = int(input('Proporcione el mes del año (1/12): '))
#estacion = None
#
#if mes == 1 or mes == 2 or mes == 12:
#    estacion = 'Invierno'
#elif mes == 3 or mes == 4 or mes == 5:
#    estacion = 'Primavera'
#elif mes == 6 or mes == 7 or mes == 8:
#    estacion = 'Verano'
#elif mes == 9 or mes == 10 or mes == 11:
#    estacion = 'Otoño'
#else:
#    estacion = 'Mes incorrecto'
#print(f'La estacion para el mes {mes} es: {estacion}')


#18: Etapas de la vida segun la edad

#edad = int(input('Proporciona tu edad '))
#mensaje = None
#
#if edad >= 0 and edad <= 10:
#    mensaje = 'La infacia es increible...'   
#elif edad > 10 and edad <= 20:
#   mensaje = 'Muchos cambios y mucho estudio..'
#elif edad > 20 and edad <= 30:
#   mensaje = 'Amor y comienza el trabajo...' 
#else:
#   mensaje = 'Etapa de vidad no reconocida'
#
#print(f'Tu edad es {edad}, {mensaje}')


#19: Sistema de calificaciones

#nota = int(input('Proporciona un valor entre 0 y 10'))
#calificacion = None
#
#if nota >= 9 and nota <= 10:
#    mensaje = 'A'
#elif nota >= 8 and nota < 9:
#    mensaje = 'B'
#elif nota >= 7 and nota < 8:
#    mensaje = 'c;'
#elif nota >= 6 and nota < 7:
#    mensaje = 'D'
#elif nota >= 0 and nota < 6:
#    mensaje = 'F'
#else:
#    mensaje = 'Valor desconocido'
#
#print(mensaje)


#20: Hora futura, escribir un programa que pregunte la hora actual del reloj y un numero entero de horas que indique que hora marca el reloj

#horaActual = int(input('Digite la hora actual en un formato de 12h: '))
#cantidadHoras = int(input('Dijite la cantidad de horas que quiere que pasen: '))
#
#horaFutura = (horaActual + cantidadHoras) % 24
#
#print(horaFutura)


#21: Parte decimal. Escriba un programa que entregue la parte decimal de un numero real ingresado por el usuario.

#num = float(input('Ingrese un número real: '))
#
#entera = int(num)
#decimal = abs(num) - abs(entera)
#decimal = round(decimal, 2)
#print(decimal)


#22: Cuanto debo sacar en el examen 3 para pasar?

#c1 = int(input('Ingrese la nota del primer examen'))
#c2 = int(input('Ingrese la nota del segundo examen'))
#nl = int(input('Ingrese la nota del laboratorio'))
#
#nc = (60 - nl * 0.3) / 0.7
#
#c3 = 3 * nc - c1 - c2 
#
#c3 = round(c3, 2)
#
#print(f'Necesita sacar en el tercer examen la nota de {c3}')


#23:Huevos a la copa

#from math import *
#
#masa = 55
#densidad = 1.038
#caCalorifica = 3.7
#conTermica = 0.0054
#aguEbull = 100
#temHuevo = int(input('Ingrese la temperatura actual del huevo: '))
#temFinal = 70
#
#tiemCocina = ((masa ** (2/3) * caCalorifica * densidad ** (1/3)) / (conTermica * pi **2 *((4 * pi)/3)**(2/3)) * log(0.76 * ((temHuevo - aguEbull)/ (temFinal - aguEbull)) ))
#
#tiemCocina = round(tiemCocina, 2)
#
#print(f'El tiempo que debe cocinarse el huevo es de {tiemCocina} segundos')


#24: Numero par


#num = int(input('Ingrese un número par '))
#
#num = num % 2
#
#if num == 0:
#    print('Su numero es par')
#else:
#    print('Su numero es impar')


#25: Años bisietos

# anno = int(input('Ingrese un año: '))
# 
# prue1 = anno % 400
# 
# prue2 = anno & 100
#  
# if prue1 == 0 and prue2 != 0:
#     print(f'El año {anno} es bisiesto')
# else:
#     print(f'El año {anno} no es bisiesto') 


#26: Division

#dividendo = int(input('Dividendo: '))
#divisor= int(input('Divisor: '))
#
#cosiente = dividendo / divisor
#resto = dividendo % divisor
#
#if resto == 0:
#    print('La division es exacta')
#else:
#    print('La division no es exacta')
#
#print(f'''cosiente: {int(cosiente)}
#resto: {resto}
#''')


#27: Palabra mas larga

#palabra1 = input('Ingrese una palabra: ')
#palabra2 = input('Ingrese otra palabra: ')
#
#val1 = len(palabra1)
#val2 = len(palabra2)
#
#if val1 > val2:
#    i =  val1 - val2
#    print(f'La palabra {palabra1} tiene {i} letras mas que {palabra2}')
#elif val2 > val1:
#    i = val2 -  val1
#    print(f'La palabra {palabra2} tiene {i} letras mas que {palabra1}')
#else:
#    print('Las dos palabras tienen el mismo largo')
#


#28: Ordenamiento

#def burbuja(nums):
#    intercambio = True
#
#    while intercambio:
#        intercambio = False
#        for i in range(len(nums)-1):
#            if nums[i] > nums[i + 1]:
#                nums[i], nums[i + 1] = nums[i + 1], nums[i] 
#                intercambio = True
#
#n = 0
#numeros = []
#while n < 4:
#    ing = int(input('Ingrese un numero: '))
#    numeros.append(ing)
#    n += 1
#
#burbuja(numeros)
#print(numeros)

#29: diferencia de caracteres

#val = input('Ingrese un caracter: ')
#
#if len(val) == 1:
#    if ord(val) >= 48 and ord(val) <= 57:
#        print(f'El caracter {val} es un número')
#    elif ord(val) >= 65 and ord(val) <= 90:
#        print(f'El caracter {val} es una letra mayuscula')
#    elif ord(val) >= 97 and ord(val) <= 122:
#        print(f'El caracter {val} es una letra minuscula')
#    else:
#        print(f'El caracter ingresado {val} no es ni letras ni numeros')
#else:
#    print('Ingrese un solo caracter')


#30: calculadora

#num1 = int(input('Operando: '))
#operador = input('Operador: ')
#num2 = int(input('Operando: '))
#
#if operador == '+':
#    suma = num1 + num2
#    print(f'{num1} {operador} {num2} = {suma}')
#elif operador == '-':
#    resta = num1 - num2
#    print(f'{num1} {operador} {num2} = {resta}')
#elif operador == '*':
#    mult = num1 * num2
#    print(f'{num1} {operador} {num2} = {mult}')
#elif operador == '/':
#    div = num1 / num2
#    print(f'{num1} {operador} {num2} = {div}')
#elif operador == '^':
#    elv = num1 ** num2
#    print(f'{num1} {operador} {num2} = {elv}')
#else:
#    print(f'El operador {operador} no es valido')


#31: Edad

# from time import localtime
# 
# t = localtime()
# dia = t.tm_mday
# mes = t.tm_mon
# year = t.tm_year
# 
# print('Ingrese su fecha de nacimiento')
# diNa = int(input('Dia: '))
# meNa = int(input('Mes: '))
# anNa = int(input('año: '))
# 
# if mes > meNa:
#     actual = (anNa - year) * (-1)
#     print(f'usted tiene {actual} años')
# elif mes < meNa:
#     actual = ((anNa - year) * (-1)) - 1
#     print(f'usted tiene {actual} años')
# elif mes == meNa and diNa >= dia:
#     actual = (anNa - year) * (-1)
#     print(f'usted tiene {actual} años')


#32: Set de tenis

#a = int(input('Juegos Ganados por A: '))
#b = int(input('Juegos Ganados por B: '))
#
#if a == 6 and b <= 4:
#    print('gano A')
#elif b == 6 and b <= 4:
#    print('Gano B')
#elif a <= 5 and b <= 5:
#    print('Aun no termina')
#elif a == 7 and b >= 5:
#    print('Gano A')
#elif b == 7  and b >= 5:
#    print('Gano B')
#elif a == 7 and b < 5:
#    print('Invalido')
#elif b == 7 and a < 5:
#    print('Invalido')
#elif a >= 7 and b >= 7:
#    print('Invalido')
#else:
#    print('Aun no termina')


#33: Triangulos:

#lad1 = float(input('Ingrese a: '))
#lad2 = float(input('Ingrese b: '))
#lad3 = float(input('Ingrese c: '))
#
#if lad1 == lad2 and lad1 == lad3:
#    print('El triangulo es equilatero')
#elif lad1 > (lad2 + lad3) or lad2 > (lad1 + lad3) or lad3 > (lad2 + lad1):
#    print('El triangulo no es valido')
#elif lad1 == lad2 and lad1 != lad3 or lad2 == lad3 and lad2 != lad1:
#    print('El triangulo es isóceles')
#elif lad1 != lad2 and lad1 != lad3 and lad2 != lad3:
#    print('El tirangulo es escaleno')
#elif lad1 > (lad2 + lad3):
#    print('El triangulo no es valido')


#34: Indice de masa corporal

#peso = float(input('ingrese su peso: '))
#altura = float(input('Ingrese su altura: '))
#edad = int(input('ingrese su edad: '))
#
#imc = (peso) / (altura ** 2)
#
#if edad < 45 and imc < 22:
#    print('Bajo')
#elif edad < 45 and imc >= 22 or edad >= 45 and imc < 22:
#    print('Medio')
#elif edad >= 45 and imc >= 22:
#    print('Alto')


#34: Multiplos

#mult = int(input('Ingrese un numero: '))
#cont = 1
#
#while cont <= 10:
#    res = mult * cont
#    print(f'{mult} x {cont} = {res}')
#    cont += 1


#35: Potencias de dos

#cant = int(input('Ingrese un numero'))
#i = 0
#while i <= cant:
#    print(2**i)
#    i += 1


#36: Suma de numeros 

#num1 = int(input('Ingrese un numero: '))
#num2 = int(input('Ingrese un numero mayor al anterior: '))
#
#lista = []
#if num1 < num2:
#    for i in range(num1 + 1, num2):
#        lista.append(i)
#
#    res = sum(lista)
#    print(f'La suma es {res}')
#    
#print('El primer numero tiene que ser menor')



#36: Tabla de multiplicar

#for i in range(1, 11):
#   for j in range(1, 11):
#       print('{:3}'.format(i*j), end=' ')
#   print()


#38: divisores

#div = int(input('Ingrese numero: '))
#i = 1
#while i <= div:
#   if (div % i) == 0:
#       print('{:2}'.format(i), end=' ')
#   i += 1
#print()

#39: Tiempo de viaje

#tiempoMin = 0
#
#while True:
#    durTramo= int(input('Duracion tramo '))
#    tiempoMin += durTramo
#
#    if durTramo == 0:
#        break
#horas = tiempoMin / 60
#segundos = tiempoMin % 60
#print(f'{int(horas)}:{segundos}')

#40: Dibujo de asteriscos
#altura = int(input('Altura: '))
#ancho = int(input('Ancho: '))
#
#for i in range(altura):
#    for j in range(ancho):
#        print("*", end=" ")
#    print()
#altura = int(input('Altura: '))
#ancho = 1
#for i in range(altura):
#    for j in range(ancho):
#        print("*", end=" ") 
#    ancho += 1
#    print()

#Pi
# num = int(input('Ingrese un numero '))

# serie = 0
# for i in range(1, num + 1): 
#    serie += (-1)**(i+1) / (2 * i - 1) 

# serie = serie * 4
# print(serie)


#Suma de fracciones

#cont = 1
#suma = 0
#print('Potencia    Fraccion     Suma' )
#while cont <= 10:
#    f = 0.5**cont
#    suma += f
#    f = round(f, 5) 
#    suma = round(suma, 5)
#    
#    print(cont, "        " + "  ", f, "  " , "    ", suma)
#    cont += 1
    
#    
#Accediendo a intervalos de listas

#lista = ['a', 'b', 'c', 'd', 'f']
#
#rango = lista[0:3]
#print(rango)
#cont = 0
#
#for i in lista:
#    cont += 1
#
#print(cont)
#

#lista.pop(0)
#print(lista)

#
#for i in range(11):
#    if i % 3 == 0:
#        print(i)

#Crear una lista que contenga numeros menores a 5 a partir de una tupla.

#tupla = (13, 1, 8, 3, 2, 5, 8) 
#lista = []
#
#for i in tupla:
#    if i < 5:
#        lista.append(i)
#
#print(lista)

#diccionario = {
#	'Nombre': 'Jhonatan',
#	'Apellido': 'Duran',
#	'Edad': '21'}
#
#for i, j in diccionario.items():
#    print(i, j)

# lista = [2, 4, 5, 1, 4]

# tamano = len(lista)
# newLista = []
# cont = 0

# for j in range(5):
#     menor = lista[0]
#     for i in range(tamano):
#         if lista[i] <= menor:
#             menor = lista[i]

#     newLista.append(menor)
#     lista.remove(menor)
#     tamano -= 1
#     cont += 1
# print(lista)
# print(newLista)

#list = [4, 3, 2, 6, 5, 7]
#
#for i in range(len(list)):
#    menor = i
#    for j in range(i + 1, len(list)):
#        if list[j] < list[menor]:
#            menor = j 
#
#    list[i], list[menor] = list[menor], list[i]
#    print(list)
#print(list)

#def sumarNumeros(*args):
#    suma = 0
#    for i in args:
#        suma += i
#    return suma
#
#print(sumarNumeros(2,2,2,2))

#def listarTerminos(**kwargs):
#    for key, valor in kwargs.items():
#        print(f'{key}: {valor}')
#
#listarTerminos(Nombre = 'Jhonatan', Apellido = 'Apellido')

#Funciones recursivas

#def factorial(number):
#    if number > 1:
#        number *= factorial(number -1)
#    return number
#
#factorial(5)

#Fibonachi con recursividad

# def fibonachi(number):
#     if number <= 1:
#         return number
#     else:
#         number = fibonachi(number -1) + fibonachi(number -2)
#     return number

# print(fibonachi(4))

#Funcion recursiva

# def countDown(number):
#     if number >= 1:
#         print(number)
#         number -= countDown(number - 1)
#     return number

# countDown(3)

#Pago de total de una compra

def calcularPago(pagoSinImpuesto, impuesto):
    return pagoSinImpuesto +pagoSinImpuesto * (impuesto/100)


print(calcularPago(1000,16))