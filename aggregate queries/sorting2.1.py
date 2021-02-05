# Description: If the titles' average ratings are inside specific ranges (0-1, 1.1-2, 2.1-3, ..., 9.1-10), for each range, find the number of titles whose average rating is inside that range. This version uses sorting (heap sort)

import csv

def heapify(lista, size, root):
    max_element = root              # Let the root be the largest element
    left_child = (2 * root) + 1
    right_child = (2 * root) + 2


    # If the left child is correctly placed and its value is larger than the max_element's value, then update the value of max_element
    if left_child < size and lista[left_child] > lista[max_element]:
        max_element = left_child

    # Repeat above step for the right child
    if right_child < size and lista[right_child] > lista[max_element]:
        max_element = right_child

    # If the root isn't the max_element, then swap them
    if root != max_element:
        temp = lista[root]
        lista[root] = lista[max_element]
        lista[max_element] = temp
        # Repeat function for the new root to make sure it is the max_element
        heapify(lista, size, max_element)


def heap_sort(lista):
    n = len(lista)

    # Create a new heap from the list. Second parameter in range is -1 as I want to stop at the element before -1. Third parameter in range is also -1 because each time i is decremented by 1.
    for i in range(n, -1, -1):
        heapify(lista, n, i)


    # Move the root of the largest heap at the end
    for i in range(n - 1, 0, -1):
        temp = lista[i]
        lista[i] = lista[0]
        lista[0] = temp

        heapify(lista, i, 0)


with open('title.ratings.tsv', 'r') as file:

    tsv_reader = csv.reader(file, delimiter = '\t')

    next(tsv_reader)    # Ignore column's name

    ratings_list = []

    # Counters for titles whose average rating is inside corresponding range
    space01 = 0
    space12 = 0
    space23 = 0
    space34 = 0
    space45 = 0
    space56 = 0
    space67 = 0
    space78 = 0
    space89 = 0
    space910 = 0

    # Put averageRatings column in ratings_list array
    while True:
        try:
            s = next(tsv_reader)
            ratings_list.append(float(s[1]))
        except StopIteration:
            break


    heap_sort(ratings_list)     # Use heap_sort to sort ratings_list


    # Now that ratings_list has been sorted, for each title rating that belongs to a range, increment the corresponding counter
    for el in range(len(ratings_list)):
        if ratings_list[el] >= 0.1 and ratings_list[el] <= 1.0:
            space01 += 1
        elif ratings_list[el] >= 1.1 and ratings_list[el] <= 2.0:
            space12 += 1
        elif ratings_list[el] >= 2.1 and ratings_list[el] <= 3.0:
            space23 += 1
        elif ratings_list[el] >= 3.1 and ratings_list[el] <= 4.0:
            space34 += 1
        elif ratings_list[el] >= 4.1 and ratings_list[el] <= 5.0:
            space45 += 1
        elif ratings_list[el] >= 5.1 and ratings_list[el] <= 6.0:
            space56 += 1
        elif ratings_list[el] >= 6.1 and ratings_list[el] <= 7.0:
            space67 += 1
        elif ratings_list[el] >= 7.1 and ratings_list[el] <= 8.0:
            space78 += 1
        elif ratings_list[el] >= 8.1 and ratings_list[el] <= 9.0:
            space89 += 1
        elif ratings_list[el] >= 9.1 and ratings_list[el] <= 10.0:
            space910 += 1

    # Print results
    print("0.1 - 1.0 :  " + str(space01) + '\n' +
    "1.1 - 2.0 :  " + str(space12) + '\n' +
    "2.1 - 3.0 :  " + str(space23) + '\n' +
    "3.1 - 4.0 :  " + str(space34) + '\n' +
    "4.1 - 5.0 :  " + str(space45) + '\n' +
    "5.1 - 6.0 :  " + str(space56) + '\n' +
    "6.1 - 7.0 :  " + str(space67) + '\n' +
    "7.1 - 8.0 :  " + str(space78) + '\n' +
    "8.1 - 9.0 :  " + str(space89) + '\n' +
    "9.1 - 10 :  " + str(space910) + '\n')
