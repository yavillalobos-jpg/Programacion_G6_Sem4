def calcular_pago(horas, tarifa):
    pago = horas * tarifa
    print("Pago dentro de la función: C$", pago)

def askhours():
    print("Dime cuántas horas trabajaste:")
    return int(input())

calcular_pago(40, 120)

# La siguiente instrucción produciría NameError:
#print(pago)
""" 
#Este (pago) da error porque la variable pago está definida dentro de la función calcular_pago y no es accesible fuera de ella.
"""