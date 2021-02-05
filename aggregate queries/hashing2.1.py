# Description: If the titles' average ratings are inside specific ranges (0-1, 1.1-2, 2.1-3, ..., 9.1-10), for each range, find the number of titles whose average rating is inside that range. This version uses hashing.

import csv

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


    hash_list = [None] * 10     # hash_list will be the result of hashing. Initialize it with None elements


    # Create and apply hush function for ratings_list array
    for i in range(0, len(ratings_list)):
        x = ratings_list[i] - 0.1   # Ranges begin with a digit + 0.1
        y = int(x//1)               # Hash by the range that each rating belongs to


        if hash_list[y] is None:                    # If list inside index 'y' is empty
            hash_list[y] = list([ratings_list[i]])  # Create a new list
        else:
            hash_list[y].append(ratings_list[i])    # If list isn't empty, append the element


    # For each title rating that belongs to a range, increment the corresponding counter
    for lists in hash_list:
        for rating in lists:
            if rating >= 0.1 and rating <= 1.0:
                space01 += 1
            elif rating >= 1.1 and rating <= 2.0:
                space12 += 1
            elif rating >= 2.1 and rating <= 3.0:
                space23 += 1
            elif rating >= 3.1 and rating <= 4.0:
                space34 += 1
            elif rating >= 4.1 and rating <= 5.0:
                space45 += 1
            elif rating >= 5.1 and rating <= 6.0:
                space56 += 1
            elif rating >= 6.1 and rating <= 7.0:
                space67 += 1
            elif rating >= 7.1 and rating <= 8.0:
                space78 += 1
            elif rating >= 8.1 and rating <= 9.0:
                space89 += 1
            elif rating >= 9.1 and rating <= 10.0:
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
