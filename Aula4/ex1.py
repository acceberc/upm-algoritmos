idade = int(input("informe sua idade"))

if idade < 5:
    print("NÃO TEM IDADE PARA SER ATLETA")
elif idade >=5 and idade <= 7:
    print("INFANTIL A")
elif idade >=8 and idade <= 10:
    print("INFANTIL B")
elif idade >=11 and idade <= 13:
    print("JUVENIL A")
elif idade >=14 and idade <= 17:
    print("JUVENIL B")
else:
    print("SÊNIOR")