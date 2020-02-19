#!/usr/bin/python3
#
#   A script for comparing different column in a sheet
#
#

import csv
list1 = []
list2 = []
dupli = []

with open('csv_comp.csv', newline='') as csvfile:
    rows = csv.reader(csvfile)
    for row in rows:
        list1.append(row[0].lower())
        list2.append(row[2].lower())
    ## Test duplication
#    for j in list2:
#        if list2.count(j)>1:
#            dupli.append(j)
#    print(dupli)
## Find out the same values in 2 lists
    for i in list(set(list1) & set(list2)):
        print(i)
