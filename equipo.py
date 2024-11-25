equipo=["mary"]
cant_integrantes=int(input("¿cuantos integrantes mas va a ingresar "))
for i in (range(cant_integrantes)):
    intg=input("agrega integrante ")
    equipo.append(intg)
print("los integrantes son", equipo)