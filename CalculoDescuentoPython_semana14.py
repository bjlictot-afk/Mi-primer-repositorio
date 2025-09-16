#Tarea de Programación: Cálculo de Descuento en Compras
#Semana 14
#Nombre:Belgica Licto
#Docente:Ing.Llerena Ocaña Luis Antonio
def calcular_descuento(monto_total, porcentaje_descuento=10):
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento


if __name__ == "__main__":
    monto1 = 200.0
    descuento1 = calcular_descuento(monto1)
    total1 = monto1 - descuento1
    print("Compra 1:")
    print(f"  Monto total: ${monto1}")
    print(f"  Descuento aplicado (10%): ${descuento1}")
    print(f"  Monto final a pagar: ${total1}\n")

    monto2 = 500.0
    descuento2 = calcular_descuento(monto2, 20)
    total2 = monto2 - descuento2
    print("Compra 2:")
    print(f"  Monto total: ${monto2}")
    print(f"  Descuento aplicado (20%): ${descuento2}")
    print(f"  Monto final a pagar: ${total2}")
