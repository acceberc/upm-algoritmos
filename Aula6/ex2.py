numero = int(input("digite numero inteiro: "))

while (numero <= 0):
    print("VALOR INVÁLIDO")
    numero = int(input("digite numero inteiro: "))
else:
    for i in range (1,100):
        if numero % i == 0:
            print(i, end = ' ')