import random
import time

def sort_by_mix (my_lista):

    if len(my_lista) > 1:
        mid = len(my_lista) // 2
        left = my_lista [:mid]
        right = my_lista [mid:]

        print (left, '*'*5, right)

        ##recursive call in each half
        sort_by_mix(left)
        sort_by_mix(right)

        ##iterators to go through the two sublists
        i = 0
        j = 0

        ##Iterator for the main list
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right [j]:
                my_lista[k] = left[i]
                i += 1
            else:
                my_lista[k] = right[j]
                j += 1
            
            k += 1

        while i < len(left):
            my_lista[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            my_lista[k] = right[j]
            j += 1
            k += 1
        
        print(f'left {left}, right {right}')
        print(my_lista)
        print('-'*5)
    
    return my_lista

if __name__ == '__main__':

    list_size = int(input('How big will the list be? '))

    start = time.time()
    my_lista = [random.randint(0, 100) for i in range(list_size)]
    print(my_lista)
    print('-'*20)

    sorted_list = sort_by_mix(my_lista)
    print(sorted_list)

    end = time.time()
    print(f'this sorting algorithm takes an execution time of {round(end - start, 3)}')