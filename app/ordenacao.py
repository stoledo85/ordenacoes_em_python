import random
import time
from sort import (
    bubble_sort,
    comb_sort,
    insertion_sort,
    merge_sort,
    selection_sort,
    heap_sort,
    gnome_sort,
)


def sorteio_numeros(num: int):
    """Gerador de Numeros aleatórios

    Args:
        num (int): Número de elemntos que esta lista terá

    Returns:
        list: retornará uma lista desordenada de elementos.
    """
    numeros = list(range(1, num + 1))
    n = random.sample(numeros, num)
    return n


def relatorio_sorts(listas_de_numeros):
    print(f"#" * 20, "Bubble", "#" * 20)
    for i in range(len(listas_de_numeros)):
        start_time = time.perf_counter()
        bubble_sort(sorteio_numeros(listas_de_numeros[i]))
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(f"Lista com {listas_de_numeros[i]}: {execution_time: .6f} segundos")

    print(f"#" * 20, "Insertion", "#" * 20)
    for i in range(len(listas_de_numeros)):
        start_time = time.perf_counter()
        insertion_sort(sorteio_numeros(listas_de_numeros[i]))
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(f"Lista com {listas_de_numeros[i]}: {execution_time: .6f} segundos")
    
    print(f"#" * 20, "Selection", "#" * 20)
    for i in range(len(listas_de_numeros)):
        start_time = time.perf_counter()
        selection_sort(sorteio_numeros(listas_de_numeros[i]))
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(f"Lista com {listas_de_numeros[i]}: {execution_time: .5f} segundos")
    
    print(f"#" * 20, "Comb", "#" * 20)
    for i in range(len(listas_de_numeros)):
        start_time = time.perf_counter()
        comb_sort(sorteio_numeros(listas_de_numeros[i]))
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(f"Lista com {listas_de_numeros[i]}: {execution_time: .5f} segundos")
    
    print(f"#" * 20, "Merge", "#" * 20)
    for i in range(len(listas_de_numeros)):
        start_time = time.perf_counter()
        merge_sort(sorteio_numeros(listas_de_numeros[i]))
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(f"Lista com {listas_de_numeros[i]}: {execution_time: .5f} segundos")
    
    print(f"#" * 20, "Heap", "#" * 20)
    for i in range(len(listas_de_numeros)):
        start_time = time.perf_counter()
        heap_sort(sorteio_numeros(listas_de_numeros[i]))
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(f"Lista com {listas_de_numeros[i]}: {execution_time: .5f} segundos")

    print(f"#" * 20, "Gnome", "#" * 20)
    for i in range(len(listas_de_numeros)):
        start_time = time.perf_counter()
        gnome_sort(sorteio_numeros(listas_de_numeros[i]))
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(f"Lista com {listas_de_numeros[i]}: {execution_time: .5f} segundos")


def main():
    listas_de_numeros = [50, 100, 200, 400, 800, 1600]

    relatorio_sorts(listas_de_numeros)


if __name__ == "__main__":
    main()
