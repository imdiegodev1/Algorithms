import random
import time

def binary_search (my_list, start, end, target, iterations = 0):
    
    iterations += 1

    if start > end:
        return (False, iterations)
    
    mid = (start + end) // 2

    if my_list[mid] == target:
        return (True, iterations)
    elif my_list[mid] < target:
        return binary_search(my_list, mid + 1, end, target, iterations = iterations)
    else:
        return binary_search(my_list, start, mid - 1, target, iterations = iterations)

if __name__ == '__main__':
    
    list_size = int(input('How big will the list be?? '))
    target = int(input('What number do you want to find? '))

    start = time.time()
    my_list = sorted([random.randint(0, 100) for i in range(list_size)])

    (found, iterations) = binary_search(my_list, 0, len(my_list), target)
    print(my_list)
    print(f'The {target} {"is" if found else "is not"} in the list')
    end = time.time()
    print(f'This binary search algorithm takes an execution time of {round(end - start, 3)}')
    print (f'The number of iterations performed in the search was of {iterations}')