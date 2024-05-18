import random


def bubble_sort(lista: list[int]):
    """Ordena a Lista de forma crescente."""
    n = len(lista)
    for i in range(n):
        for j in range(n - 1):
            x = lista[j]
            y = lista[j + 1]
            aux = x > y
            if aux:
                lista[j], lista[j + 1] = y, x
    return lista


def insertion_sort(lista: list[int]):
    """Ordena um elemento por vez"""
    n = len(lista)
    for i in range(n):
        aux = lista[i]
        k = i
        while k > 0 and aux < lista[k - 1]:
            lista[k] = lista[k - 1]
            k -= 1
        lista[k] = aux
    return lista


def selection_sort(lista: list[int]):
    """Ordenação procurando sempre o menor valor

    Args:
        lista (list[int]): _description_
    """
    n = len(lista)

    if n == 1:
        return lista[0]

    for i in range(n - 1):

        men = i

        for j in range(i + 1, n):
            if lista[j] < lista[men]:
                men = j
        if lista[i] != lista[men]:
            aux = lista[i]
            lista[i] = lista[men]
            lista[men] = aux
    return lista


def comb_sort(lista: list[int]):
    """É uma variação do algoritmo Bubble

    Args:
        lista (list[int]): _description_

    """
    dist = len(lista)
    troca = True
    while dist > 1 or troca:
        dist = max(1, int(dist / 1.25))
        troca = False
        for i in range(len(lista) - dist):
            j = i + dist
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
                troca = True
    return lista
    # # def bogo_sort(lista: list[int]):
    # """O algoritmo menos eficiente de ordenação

    # Args:
    #     lista (list[int]): lista de numeros a ser ordenado

    # Returns:
    #     _type_: _description_
    # """
    # n = len(lista)

    # def isSorted(lista):
    #     if n < 2:
    #         return True
    #     for i in range(n - 1):
    #         if lista[i] > lista[i + 1]:
    #             return False
    #     return True

    # while not isSorted(lista):
    #     random.shuffle(lista)
    # return lista


def merge_sort(lista: list[int]):
    """Ordenação que usa como seu principal trunfo metodo dividir e conquistar"""
    n = len(lista)
    if n > 1:
        meio = n // 2
        lista_esq = lista[:meio]
        lista_dir = lista[meio:]
        merge_sort(lista_esq)
        merge_sort(lista_dir)
        i = 0
        j = 0
        k = 0
        while i < len(lista_esq) and j < len(lista_dir):
            if lista_esq[i] < lista_dir[j]:
                lista[k] = lista_esq[i]
                i += 1
            else:
                lista[k] = lista_dir[j]
                j += 1
            k += 1
        while i < len(lista_esq):

            lista[k] = lista_esq[i]
            i += 1
            k += 1

        while j < len(lista_dir):
            lista[k] = lista_dir[j]
            j += 1
            k += 1
    return lista


def heapify(array, a, b):
    largest = b
    l = 2 * b + 1
    root = 2 * b + 2

    if l < a and array[b] < array[l]:
        largest = l

    if root < a and array[largest] < array[root]:
        largest = root

    if largest != b:
        array[b], array[largest] = array[largest], array[b]
        heapify(array, a, largest)


def heap_sort(lista: list[int]):
    """Ordenação que se organiza apartir dos elementos inseridos na lista."""
    n = len(lista)
    for b in range(n // 2 - 1, -1, -1):
        heapify(lista, n, b)

    for b in range(n - 1, 0, 1):
        lista[b], lista[0] = lista[0], lista[b]
        heapify(lista, b, 0)

    return lista


def gnome_sort(lista: list[int]):
    pivot = 0
    n = len(lista)
    while pivot < n - 1:
        if lista[pivot] > lista[pivot + 1]:
            lista[pivot + 1], lista[pivot] = lista[pivot], lista[pivot + 1]
            if pivot > 0:
                pivot -= 2
        pivot += 1
    return lista


def bucket_sort(lista: list[int]):
    return lista


def cocktail_sort(lista: list[int]):
    pass


def quick_sort(lista: list[int]):
    pass


def shell_sort(lista: list[int]):
    pass
