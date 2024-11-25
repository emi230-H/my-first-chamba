deportes=["football", "voleiball", "natacion", "basqutbol"]
print(deportes)
print(deportes[2])
#poscicion de natacion
pos=deportes.index("natacion")
print("la posicion de natacion es: ", pos)

deportes.append("handball")
print(deportes)
deportes.insert(2, "rugby")
print(deportes)


cantidad_saludos=int(input("¿cuantos saludos quieres? "))
for i in range(cantidad_saludos):
    print("hola")
num_deportes=int(input("¿cuantos deportes quieres agregar?"))
for i in (range(num_deportes)):
    dep=input("ingresa deporte ")
    deportes.append(dep)
print(deportes)
