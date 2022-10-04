# função para remover repetidos
def remove_repetidos(lista):
    # criando uma lista vazia
    nova_lista = []
    # percorrendo a lista toda
    for i in lista :
	# verificando elementos que não tem em nova lista
        if i not in nova_lista :
	    # passando os elementos que já não possui igual
            nova_lista.append(i)
    # retornando colocando a lista em ordem crescente
    return sorted(nova_lista)
