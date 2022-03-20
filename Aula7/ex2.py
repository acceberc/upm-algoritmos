def valorPagamento(valor, dias):
    if dias >= 1:
        return ((valor * 0.001) * dias) + (valor * 0.03) + valor
    elif dias == 0:
        return valor


def main():
    valor = float(input("Informe o valor: "))
    dias = int(input("Informe os dias: "))
    print(valorPagamento(valor, dias))


main()
