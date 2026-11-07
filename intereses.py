cant = float(input("Digite la cantidad de dinero invertida: "))
porc_interes = float(input("Digite el porcentaje de interes: "))
periodo = float(input("Digite los dias: "))

valor_interes = (cant * porc_interes * periodo) / 360
impuesto = valor_interes * 0.07
total_pagar = cant + valor_interes - impuesto

print("El valor de sus intereses ganados es de:", valor_interes)
print("Su valor total a retirar es de:", total_pagar)