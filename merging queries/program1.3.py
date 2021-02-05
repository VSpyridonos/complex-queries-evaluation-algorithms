# Description: Find the title names that don't have a rating

import csv

with open('title.ratings', 'r') as file1, open('title.basics', 'r') as file2, open('output1.3.txt', 'w') as output:

    tsv_reader1 = csv.reader(file1, delimiter = '\t')
    tsv_reader2 = csv.reader(file2, delimiter = '\t')
    tsvwriter = csv.writer(output, delimiter = ',')

    next(tsv_reader1)    # For ignoring column names
    next(tsv_reader2)

    s1 = next(tsv_reader1)
    s2 = next(tsv_reader2)

    counter1 = 0                                        # element counter for the first file
    counter2 = 0                                        # element counter for the second file

    while True:
        try:
            if(s1[0] == s2[0]):                         # if tconst fields are the same
                s2 = next(tsv_reader2)                  # move second file's line pointer
                counter2+=1                             # increment second file's element counter
            else:                                       # if tconst fields are different
                if(s1[0] > s2[0]):                      # if the first file's tconst field is bigger than the second file's one
                    if(counter1 == counter2):           # if the two counters are equal (if title doesn't have a rating)
                        var = s2[2] + '\t' + '\n'       # save primaryTitle field in var
                        output.write(var)               # write result in output file
                        counter1+=1                     # increment first file's element counter
                    s2 = next(tsv_reader2)              # move second file's line pointer
                    counter2+=1                         # increment second file's element counter
                else:                                   # if tconst fields are different
                    s1 = next(tsv_reader1)              # move first file's line pointer
                    counter1+=1                         # # increment first file's element counter

        except StopIteration:
            break

    print("Finished!")
