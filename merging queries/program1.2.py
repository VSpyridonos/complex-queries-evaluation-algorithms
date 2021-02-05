# Description: For each title that is the first episode of a series, find the name of the title, the series' id and the season's number

import csv

with open('title.basics', 'r') as file1, open('title.episode', 'r') as file2, open('output1.2.txt', 'w') as output:

    tsv_reader1 = csv.reader(file1, delimiter = '\t')
    tsv_reader2 = csv.reader(file2, delimiter = '\t')
    tsvwriter = csv.writer(output, delimiter = ',')

    next(tsv_reader1)    # For ignoring column names
    next(tsv_reader2)

    s1 = next(tsv_reader1)
    s2 = next(tsv_reader2)

    while True:
        try:
            if(s1[0] == s2[0]):                                         # if tconst fields are the same
                if(s2[3] == '1'):                                       # if episodeNumber equals 1
                    var = s1[2] + '\t' + s2[1] + '\t' + s2[2] + '\n'    # save primaryTitle, parentTconst, seasonNumber in var
                    output.write(var)                                   # write result in output file
                s2 = next(tsv_reader2)                                  # move second file's line pointer
            else:                                                       # if tconst fields are different
                if(s1[0] > s2[0]):                                      # if the first file's tconst field is bigger than the second file's one
                    s2 = next(tsv_reader2)                              # move second file's line pointer
                else:                                                   # if the second file's tconst field is bigger than the first file's one
                    s1 = next(tsv_reader1)                              # move first file's line pointer
        except StopIteration:
            break

    print("Finished!")
