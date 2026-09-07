"""
Operaciones aritméticas básicas: suma , resta, multiplicación y división.
"""

def add(number1, number2):
    return number1 + number2

def sub(number1, number2):
    return number1 - number2

def mul(number1, number2):
    return number1 * number2

def div(number1, number2):
    try:
        return number1 / number2
    except ZeroDivisionError:
        return "No se puede dividir entre 0"
    except ValueError:
        return "Tipo de dato incorrecto, debe ingresar número"