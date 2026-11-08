salario_base = float(input("Ingrese el salario base de el empleado: "))

aporte_salud = salario_base * 0.04
aporte_pension = salario_base * 0.04
descuento = aporte_salud + aporte_pension
salario_neto = salario_base - descuento

print("El aporte a salud es de", aporte_salud)
print("El aporte a pension es de", aporte_pension)
print("El descuento es de", descuento)
print("El salario neto a pagar es", salario_neto)