ventas_registradas = 0


def registrar_venta():
    global ventas_registradas
    ventas_registradas += 1
    print("Venta registrada")


registrar_venta()
registrar_venta()

print("Total de ventas:", ventas_registradas)

#El siguiente código no funcionará correctamente si se intenta acceder a la variable ventas_registradas sin declararla como global dentro de la función registrar_venta.