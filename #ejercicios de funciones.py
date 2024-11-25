#ejercicios
'''1) crear una funcion llamada multiplicar 
que reciba 3 numeros, regresar el resultado
'''
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
