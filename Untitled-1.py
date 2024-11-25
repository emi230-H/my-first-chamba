def disk_CURP(Nom, age, mes):
    letras=nom[0:2],age[0:2],mes[0:1]
    return letras
nom=input("ingresa tu nombre")
age=input("ingresa edad")
mes=input("ingresa mes")
print(disk_CURP(Nom,age,mes))