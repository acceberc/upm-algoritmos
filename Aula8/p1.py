listacarro=[]
listaconsumo=[]

def entrada_carro():
    for i in range(0,4):
        carro=input()
        listacarro.append(carro)

def entrada_consumo():
    for i in range(0,4):
        consumo=int(input())
        listaconsumo.append(consumo)

def economico():
    if listaconsumo[0]<listaconsumo[1] and listaconsumo[0]<listaconsumo[2]and listaconsumo[0]<listaconsumo[3]:
        return listacarro[0]
    elif listaconsumo[1]<listaconsumo[0] and listaconsumo[1]<listaconsumo[2]and listaconsumo[1]<listaconsumo[3]:
        return listacarro[1]
    elif listaconsumo[2]<listaconsumo[0] and listaconsumo[2]<listaconsumo[1]and listaconsumo[2]<listaconsumo[3]:
        return listacarro[2]
    else:
        return listacarro[3]

listaconsumo=[]
def entrada_carro():
    for i in range(0,4):
        carro=input()
        listacarro.append(carro)

def entrada_consumo():
    for i in range(0,4):
        consumo=int(input())
        listaconsumo.append(consumo)
def economico():
    if listaconsumo[0]<listaconsumo[1] and listaconsumo[0]<listaconsumo[2]and listaconsumo[0]<listaconsumo[3]:
        return listacarro[0]
    elif listaconsumo[1]<listaconsumo[0] and listaconsumo[1]<listaconsumo[2]and listaconsumo[1]<listaconsumo[3]:
        return listacarro[1]
    elif listaconsumo[2]<listaconsumo[0] and listaconsumo[2]<listaconsumo[1]and listaconsumo[2]<listaconsumo[3]:
        return listacarro[2]
    else:
        return listacarro[3]

def main():
    entrada_carro()
    entrada_consumo()
    print(economico())
    
main()