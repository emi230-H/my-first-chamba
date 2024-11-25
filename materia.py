materia = {
    "nombre": "Programación",
    "codigo": "INFO2",
    "profesor": "Doña Pelos",
    "horarios": ["Lunes 9:00-11:00", "Miércoles 9:00-11:00"],
    "créditos": 8,
    "nivel": "Intermedio",
    "prerrequisitos": ["Computación I"],
    "descripción": "Desarrollo de algoritmos"
}

print(materia["profesor"])

alumno = {
    "nombre": "Doña Pelos",
    "matrícula": "A1234567",
    "edad": 17,
    "semestre": "quinto",
    "calificaciones": {
        "Matemáticas": 8.5,
        "Física": 9.0,
        "Programación": 9.5,
        "Química": 8.0
    },
    "dirección": {
        "calle": "Av. Libertad 456",
        "ciudad": "Ciudad X",
        "código_postal": "12345"
    },
    "teléfono": "555-1234-815",
    "email": "ale_pvr@example.com"
}

print(alumno["nombre"])
print(alumno["calificaciones"])
print("La calificación del alumno en programación es:")
print(alumno["calificaciones"]["Programación"])