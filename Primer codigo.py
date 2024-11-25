print("hola")

edad=int(input("ingresa tu edad: "))
if(edad>=18):
    print("eres mayor de edad")
else:
    print("eres menor de edad")

temp=float(input("ingresa la temperatura "))
if(temp<=0):
    print("hace frio abrigate")
elif(temp>0 and temp<=35):
    print("esta templado")
elif(temp>35 and temp<=100):
    print("hace mucho calor")
else:
    print("temperatura no valida")