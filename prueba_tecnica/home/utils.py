def calcular_cabida(x, y, a, b):
    # Paso 1: Verificar que los rectángulos pequeños pueden caber dentro del contenedor
    if a > x and a > y or b > x and b > y:
        return 0

    # Paso 2: Determinar g1 (lado menor) y g2 (lado mayor)
    g1, g2 = sorted([x, y])

    # Paso 3: Dividir g1 entre a y b para determinar orientación
    resto_a = g1 % a
    resto_b = g1 % b

    if resto_a < resto_b or (resto_a == resto_b and g1 // a >= g1 // b):
        l1, l2 = a, b
        c1 = g1 // a
    else:
        l1, l2 = b, a
        c1 = g1 // b

    # Paso 4: Dividir g2 entre l2
    c2 = g2 // l2
    r1 = g2 % l2

    # Paso 5: Si no hay resto, retornar el producto de c1 y c2
    if r1 == 0:
        return c1 * c2

    # Paso 6: Evaluar si caben más rectángulos en el espacio sobrante
    if l1 <= r1 and l2 <= g1:
        c3 = r1 // l1
        return c1 * c2 + c3

    # Paso 7: Retornar la cantidad de rectángulos
    return c1 * c2
