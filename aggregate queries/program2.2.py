# Spyridonos Vasileios
# AM : 2820

import csv
import collections

with open('title.basics.tsv', 'r') as file1, open('title.ratings.tsv', 'r') as file2:

    tsv_reader1 = csv.reader(file1, delimiter = '\t')
    tsv_reader2 = csv.reader(file2, delimiter = '\t')


    next(tsv_reader1)    # Ignore column names
    next(tsv_reader2)

    s1 = next(tsv_reader1)
    s2 = next(tsv_reader2)

    start_years = {}   # {xronia: [athroisma vathmologiwn, plithos titlwn me vathmologia, mesos oros vathmologiwn]}

    while True:
        try:
            if(s1[0] == s2[0]):                                                                     # an ta tconst einai idia
                year = s1[5]                                                                        # year = startYear
                exists = start_years.get(year, -1)
                if(exists == -1):                                                                   # an to year den yparxei sto start_years
                    start_years[year] = [float(s2[1]), 1, float(s2[1])]                             # s2[1] = averageRating
                else:                                                                               # an to year yparxei sto start_years
                    start_years[year][0] += float(s2[1])                                            # athroisma vathmologiwn += averageRating tou titlou
                    start_years[year][1] += 1                                                       # plithos titlwn auti ti xronia += 1
                    start_years[year][2] = float(start_years[year][0])/start_years[year][1]         # mesos oros vathmologiwn = athroisma/plithos
                s2 = next(tsv_reader2)                                                              # proxwraw to deikti tou deuterou arxeiou

            else:                                                                                   # an ta tconst einai diaforetika
                if(s1[0] > s2[0]):                                                                  # an to tconst tou prwtou arxeiou einai megalytero aptou deuterou
                    s2 = next(tsv_reader2)                                                          # proxwraw to deikti tou deuterou arxeiou
                else:                                                                               # an to tconst tou deuterou arxeiou einai megalytero aptou prwtou
                    s1 = next(tsv_reader1)                                                          # proxwraw to deikti tou prwtou arxeiou

        except StopIteration:
            break

    ordered = collections.OrderedDict(sorted(start_years.items()))                                  # ordered = leksiko taksinomimeno me vasi tis xronies
    for k, v in ordered.items():
        print("year: " + k + " average rating: " + "{0:.1f}".format(v[2]))
    print("Finished!")
