import math

num = float(input("Por favor ingrese un número: "))

seno = math.sin(num)
coseno = math.cos(num)
tangente = math.tan(num)
raiz1 = math.sqrt(num)
lognatural = math.log(num)
log10 = math.log(num) / math.log(10)

print("EL SENO ES:", seno)
print("EL COSENO ES:", coseno)
print("LA TANGENTE ES:", tangente)
print("LA RAIZ CUADRADA ES:", raiz1)
print("EL LOGARITMO NATURAL ES:", lognatural)
print("EL LOGARITMO EN BASE 10 ES:", log10)