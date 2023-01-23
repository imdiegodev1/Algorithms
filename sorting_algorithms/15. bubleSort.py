import random
import time

def bubble_sort(my_list):
    n = len(my_list)
    for i in range(n):
        for j in range(0, n - i - 1):

            if my_list[j] > my_list[j+1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    return my_list


if __name__ == '__main__':
    
    list_size = int(input('How big will the list be? '))

    start = time.time()
    lista = [random.randint(0, 100) for i in range(list_size)]
    print(lista)

    sorted_list = bubble_sort(lista)
    print(sorted_list)
    end = time.time()
    print(f'this sorting algorithm takes an execution time of {round(end - start, 3)}')
    