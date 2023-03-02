"""
    ALGORITMO DE BUSCA BINÁRIA
    Dados uma lista, que deve estar PREVIAMENTE ORDENADA, e um valor de busca, divide a lista em duas metades procurando pelo valor de busca apenas na metade onde o valor poderia estar. Novas subdivisões são feitas até que se encontre o valor de busca ou que reste apenas uma sublista vazia, quando então se conclui que o valor de busca não existe na lista.
"""
def busca_binaria(lista, val):
    count = 0
    ini = 0               # Início da lista
    fim = len(lista) - 1   # Fim da lista

    while ini <=fim:
        meio = (ini + fim) // 2   # // = Divisão inteira

        # O valor de busca foi encontrado.
        # Retorna a posição
        if lista[meio] == val:
            count += 1
            return meio
        elif val < lista[meio]:
            count += 2
            fim = meio - 1
        else:
            count += 2
            ini = meio + 1
    return - 1   # Valor não existe na lista

from data.primos import primos

print(busca_binaria(primos, 2000))