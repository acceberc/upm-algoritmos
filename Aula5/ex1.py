soma = 0.0
cont = 0

qnt_alunos = int(input("informe alunos"))
if qnt_alunos == 0:
    print("NÃO HOUVE PROCESSAMENTO")

while cont < qnt_alunos:
    media = float(input("informe a media"))
    soma += media
    cont += 1
    if media >= 6.0:
        print("PARABÉNS VOCÊ ESTÁ APROVADO")
    totalmedia = soma / qnt_alunos

if qnt_alunos > 0:
    print(totalmedia)
