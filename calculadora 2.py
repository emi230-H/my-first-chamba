opcion=1

while opcion!=0:
    num1=int(input("ingresa el primer numero "))
    num2=int(input("ingresa el segundo numero "))
    print("ingresa 1. Sumar")
    print("ingresa 2. Restar")
    print("ingresa 3. Multiplicar")
    print("ingresa 4. Dividir")
    op=int(input("¿que operacion quieres realizar? "))
    if(op==1):
        res=num1+num2
        print("la suma es:", res)
    elif(op==2):
        res=num1-num2
        print("la resta es:", res)
    elif(op==3):
        res=num1*num2
        print("la multiplicacion es:", res)
    elif(op==4):
        res=num1/num2
        print("la division es:", res)
    else:
        print("no valido")

    opcion=int(input("¿deseas continuar?, sino presiona 0 para salir "))