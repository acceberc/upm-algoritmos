def menu ():
    print("1 - Cadastrar amigo no final da lista")
    print("2 - Mostrar lista")
    print("3 - Cadastrar amigo no inicio da lista")
    print("4 - Remover um nome")
    print("5 - Substituir um nome")
    print("6 - Mostrar o número total de amigos cadastrados")
    print("7 - Colocar nomes em ordem alfabética")
    print("9 - Sair do programa")
    op = int (input("Opção Selecionada: "))
    while op < 1 or op > 9:
        op = int(input("Opção Selecionada: "))
    return op

def inserir_amigo(amigo):
    nome = input ("Nome: ")
    amigo.append(nome)

def mostrar_nomes(amigo):
    print(amigo)

def inserir_amigo_final(amigo):
    nome = input("Digite um nome: ")
    amigo.insert(0,nome)

def remover_amigo(amigo):
    nome = input("Qual o nome a ser removido: ")
    for i in range (0, len(amigo)):
        if amigo[i] == nome:
            pos = i
            break
    del amigo[pos]

def substituir_nome(amigo):
    nome = input("Qual é o nome a ser substituido? ")
    nomenovo = input("Qual é o novo nome? ")
    for i in range (0,len(amigo)):
        if amigo[i] == nome:
            amigo[i] == nomenovo
            break

def total_cadastro(amigo):
    print("Total de amigos = %d " %len(amigo))

def ordernar_amigos(amigo):
    amigo.sort()
    mostrar_nomes(amigo)

def main():
    amigo = []
    while True:
        op = menu()
        if op == 9:
            break
        if op == 1:
            inserir_amigo(amigo)
        elif op == 2:
            mostrar_nomes(amigo)
        elif op == 3:
            inserir_amigo_final(amigo)
        elif op == 4:
            remover_amigo(amigo)
        elif op == 5:
            substituir_nome(amigo)
        elif op == 6:
            total_cadastro(amigo)
        elif op == 7:
            ordernar_amigos(amigo)
        
main()