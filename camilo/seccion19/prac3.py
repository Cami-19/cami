estudiante = {
    "nombre": "andrés",
    "edad": 19,
    "curso": "python"
}
print(estudiante["nombre"])

estudiante["nota"] = 95

del estudiante["curso"]

for clave, valor in estudiante.items():
    print(clave, ":", valor)
