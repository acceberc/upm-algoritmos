import math

ctotal = float(input("Gasto total do evento: "))
vingresso  = float(input("Valor de cada ingresso: "))

qnt_ingressos = (ctotal / vingresso)
qnt_lucro = math.ceil((ctotal + ctotal * 0.23) / vingresso)

print(math.ceil(qnt_ingressos))
print(math.ceil(qnt_lucro))

