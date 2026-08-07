print ("======Calculadora de Impuesto======")

precio = float(input("Escribe el precio del producto:"))
while True:
    if precio  <0:
        print("El precio no puede ser negativo")
        precio = float(input("Escribe el precio del producto:"))
    else:
        break

impuesto = float(input("Escribe el impuesto:"))
while True:
    if impuesto < 0 or impuesto > 100:
        print("El impuesto debe estar entre 0 y 100")
        impuesto = float(input("Escribe el impuesto:"))
    else:
        break
    
impuesto_total = precio * (impuesto / 100)
impuesto_total = round(impuesto_total, 2)
precio_final = precio + impuesto_total

print("======Resultado======")
print(f"Precio original: ${precio:.2f}")
print(f"Impuesto: {impuesto}%")
print(f"Impuesto total: ${impuesto_total:.2f}")
print(f"Precio final: ${precio_final:.2f}")
input("Presiona ENTER para continuar...")


print("======Gracias por usar la calculadora de impuestos======")
input("Presiona ENTER para continuar...")
while True:
    print("======Deseas calcular otro impuesto?======")
    respuesta = input().lower()
    if respuesta == "si":
        precio = float(input("Escribe el precio del producto:"))
        impuesto = float(input("Escribe el impuesto:"))
        impuesto_total = precio * (impuesto / 100)
        impuesto_total = round(impuesto_total, 2)
        precio_final = precio + impuesto_total

        print("======Resultado======")
        print(f"Precio original: ${precio:.2f}")
        print(f"Impuesto: {impuesto}%")
        print(f"Impuesto total: ${impuesto_total:.2f}")
        print(f"Precio final: ${precio_final:.2f}")

    else:
        break