print("Bienvenido al programa")

opcion=1

while opcion!=0:
    print("Menu")

    print("Ingresa 1. Area del triangulo")
    print("ingresa 2. Area del rectangulo")
    print("Ingresa 3. Area del circulo")
    print("Ingresa 4. converir temperatura °F a °C")
    print("Ingresa 5. convertir temperatura °C a °F")

    op=int(input("¿Que operacion deseas realizar? "))

    if(op==1):
        print("Area del triangulo")
        baseT=int(input("ingresa la base "))
        alturaT=int(input("ingresa la altura "))
        AT=(baseT*alturaT)/2
        print("El area del trangulo es:", AT)

    elif(op==2):
        print("Area del rectangulo")
        baseR=int(input("Ingresa la base "))
        alturaR=int(input("Ingresa la altura "))
        AR=baseR*alturaR
        print("El area del rectangulo es ", AR)
    elif(op==3):
        print("Area del circulo")
        radio=int(input("ingresa el radio "))
        AC=3.14*(radio*radio)
        print("el aerea del circulo es", AC)
    elif(op==4):
        Fa=int(input("ingresa la temperatura fahrenheit "))
        C=((Fa-32)*5)/9
        print("la temperatura en Celsius es", C)
    elif(op==5):
        Ce=int(input("ingresa la temperatura Celsuis "))
        F=(Ce*9/5)+32
        print("la temperatura en Fahrenheit es:", F)
    else:
        print("no valido")
        
    opcion=int(input("ingresa 0. para salir del programa o 1 para continuar "))