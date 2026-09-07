import aritmetica as arit

def menu():
    print("Bienvenido a mi Calculadora")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("0. Salir")
    op = int(input("Digita el # de la opcion que sea usar: "))
    return op

def showAdd(num1, num2):
    print(F"La suma de {num1} + {num2} = {arit.add(num1, num2)}")

def showSub(num1, num2):
    print(F"La resta de {num1} - {num2} = {arit.sub(num1, num2)}")

def showMul(num1, num2):
    print(F"La multiplicación de {num1} * {num2} = {arit.mul(num1, num2)}")

def showDiv(num1, num2):
    print(F"La división de {num1} / {num2} = {arit.div(num1, num2)}")

def readValues():
    num1 = float(input("Digita el primervalor: "))
    num2 = float(input("Digita el segundo valor: "))
    return num1, num2

def chooseOption(op):
    if op == 1:
        num1, num2 = readValues()
        showAdd(num1, num2)
    elif op == 2:
         num1, num2 = readValues()
         showSub(num1, num2)
    elif op == 3:
         num1, num2 = readValues()
         showMul(num1, num2)
    elif op == 4:
         num1, num2 = readValues()
         showDiv(num1, num2)
    elif op == 0:
         print("Adios.")
         return
    else:
        print("Opción no válida...")

def main():
    while True:
         op = menu()
         chooseOption(op)
         if op == 0: break
            
main()