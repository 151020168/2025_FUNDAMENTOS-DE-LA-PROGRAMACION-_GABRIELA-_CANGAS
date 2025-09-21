def calcular_descuento(monto_total, porcentaje_descuento=0.10):
    """
    Calcula el monto del descuento aplicando el porcentaje al monto total de la compra.

    Args:
        monto_total (float): El monto total de la compra.
        porcentaje_descuento (float, opcional): El porcentaje de descuento a aplicar (ej. 0.10 para 10%).
                                                Por defecto es 0.10 (10%).

    Returns:
        float: El monto del descuento calculado.
    """
    descuento = monto_total * porcentaje_descuento
    return descuento

# Programa principal

# Primera llamada: solicitar monto total al usuario
monto_compra_1 = float(input("Introduce el monto total de la primera compra: "))
descuento_1 = calcular_descuento(monto_compra_1)
monto_final_1 = monto_compra_1 - descuento_1

print(f"\nCompra 1:")
print(f"  Monto total de la compra: ${monto_compra_1:.2f}")
print(f"  Descuento aplicado (10%): ${descuento_1:.2f}")
print(f"  Monto final a pagar: ${monto_final_1:.2f}")
print("-" * 30)

# Segunda llamada: solicitar otro monto total al usuario
monto_compra_2 = float(input("Introduce el monto total de la segunda compra: "))
porcentaje_personalizado = 0.20
descuento_2 = calcular_descuento(monto_compra_2, porcentaje_personalizado)
monto_final_2 = monto_compra_2 - descuento_2

print(f"\nCompra 2:")
print(f"  Monto total de la compra: ${monto_compra_2:.2f}")
print(f"  Descuento aplicado ({porcentaje_personalizado*100:.0f}%): ${descuento_2:.2f}")
print(f"  Monto final a pagar: ${monto_final_2:.2f}")