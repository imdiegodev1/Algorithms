import random
import time

def sort_by_insert (my_list):
    for index in range (1, len(my_list)):
        current_value = my_list[index]
        current_position = index

        while current_position > 0 and my_list[current_position - 1] > current_value:
            my_list[current_position] = my_list[current_position - 1]
            current_position -= 1

        my_list[current_position] = current_value
    return my_list

if __name__ == '__main__':

    list_size = int(input('How big will the list be? '))
    start = time.time()
    my_list = [random.randint(0, 100) for i in range(list_size)]
    sorted_list = (sort_by_insert(my_list))
    print(my_list)
    end = time.time()
    print(f'this sorting algorithm takes an execution time of {round(end - start, 3)}')