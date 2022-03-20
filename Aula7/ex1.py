import math


def atualiza_preco(valor):
    return (valor * 1.1)


def taxa(valor):
    return ((valor * 1.1) * 0.025)


def main():
    valor = float(input("Informe o valor: "))
    print('%.2f' % atualiza_preco(valor))
    print('%.2f' % taxa(valor))


main()
