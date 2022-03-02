n = int(input("Consumo em metros cúbicos:"))

if n <= 10:

    conta = 7

elif n >= 11 and n <= 30:

    conta = (n-10) * 1 + 7

elif n >= 31 and n <= 100:

    conta = (n-30) * 2 + 27

else:

    conta = (n-100) * 5 + 167

print(f'Valor  da conta = {conta}')
