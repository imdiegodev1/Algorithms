import random
import time

def lineal_search(my_list, target, iterations=0):
    match = False

    for element in my_list:
        iterations += 1
        if element == target:
            match = True
            break
    return (match, iterations)


if __name__ == '__main__':
    list_size = int(input('How big will the list be? '))
    target = int(input('What number do you want to find? '))

    start = time.time()
    my_list = [random.randint(0, 100) for i in range(list_size)]

    (found, iterations) = lineal_search(my_list, target)
    print(my_list)
    print(f'The {target} {"is" if found else "is not"} in the list')
    end = time.time()
    print(f'this linear search algorithm takes an execution time of {round(end - start, 3)}')
    print (f'the number of iterations performed in the search was of {iterations}')