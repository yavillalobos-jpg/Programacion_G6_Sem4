#El siguiente ejercicio consiste en pedir leer n de nota decir si es aprendizaje incial, fundamental, sastifactorio y avanzado, mostrar todas las notas.
def clasificar_nota(note):
    if 1.0 <= note < 59:
        return "Aprendizaje inicial"
    elif note < 69:
        return "Aprendizaje fundamental"
    elif note < 89:
        return "Aprendizaje satisfactorio"
    elif note <= 100:
        return "Aprendizaje avanzado"
    else:
        return "Nota inválida"


# Función principal
def programa():
    notas = []
    n = int(input("¿Cuántas notas desea ingresar? "))

    for i in range(n):
        note = float(input(f"Ingrese la nota {i + 1} (1 - 100): "))
        notas.append(note)

    print("\nListado de notas:")
    for note in notas:
        print(f"Nota: {note} - {clasificar_nota(note)}")


programa()