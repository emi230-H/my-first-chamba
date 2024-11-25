#Crear funciones

#funcion llamada saludar, va a recibir el nombre
def saludar_my_hommie(nombre):
    print("hey there", nombre)

nom=input("enter your name ")
saludar_my_hommie(nom)

#Funcion llamada sumita, va recibir 5 numeros
#va a regresar el valor de la suma
def sumita(n1,n2,n3,n4,n5):
    Resultado=n1+n2+n3+n4+n5
    return Resultado
n1=int(input("enter the first number "))
n2=int(input("enter the second number "))
n3=int(input("enter the third number "))
n4=int(input("enter the forth number "))
n5=int(input("enter the fifth number "))

#mandar a llamar la funcion
print(sumita(n1,n2,n3,n4,n5))

#crear una funcion llamada area triangulo
#que reciba base y altura
#regrese el resultado del area
def area_triangulo(b,h):
    area=(b*h)/2
    return area
#usar la funcion
print(area_triangulo(4,5))

#usar la funcion multiplicar
#multipicar(4,5,6)
def multiplicar(n1, n2, n3):
    multiplicacion=n1*n2*n3
    return multiplicacion
print(multiplicar(4,5,6))

'''2)crear una funcion llamada largo_cadena
que reciba un texto y devuelva 
la cantidad de caracteres de la misma'''
#usar la funcion print(largo cadena("el mundo es bonito"))
def largo_cadena(txt):
    text=len(txt)
    return text
print(largo_cadena("el mundo es bonito"))

'''3) crear una funcion llamda promedio 
que reciba 2 calificaciones y devuelva el promedio'''
#pedir calif. primer y segundo parcial
#print("el promedio es: " promedio(cal1, cal2))
def promedio(cal1, cal2):
    prom=(cal1+cal2)/2
    return prom
cal1=int(input("ingresa la primera calificacion "))
cal2=int(input("ingresa la segunda calificacion "))
print(promedio(cal1,cal2))

#crear una funcion que reciba el nombre de la persona, su edad y el mes de nacimiento
#devuelva:
#las dos primeras letras del nombre-edad-primer letra del mes
#ejemplo: MA17O

def disk_CURP(Nom, age, mes):
    letras=nom[0:2],age[0:2],mes[0:1]
    return letras
nom=input("ingresa tu nombre")
age=input("ingresa edad")
mes=input("ingresa mes")
print(disk_CURP(Nom,age,mes))