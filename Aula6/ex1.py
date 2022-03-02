numero = int(input("Informe um numero: "))

while (numero < 0 or numero > 10):
        print("VALOR INVÁLIDO") 
        numero = int(input("Informe um numero: "))
if (numero >= 0 or numero <= 10):
    for count in range (10):
        print("%dx%d=%d" % (numero, count+1, numero*(count+1)))
    
    