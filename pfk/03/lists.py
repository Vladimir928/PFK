#!/usr/bin/env python3
################################################################################
#   lists.py
#
#  chapter 3: Lists 
#
#   08.07.2019  Created by:  vo958
################################################################################

numbs = [1, -2, 3, 4, 10, -200, 350]
print(numbs)
print(type(numbs))
print(numbs[1])
print(numbs[2:4])
print(numbs[-1])
print(numbs[-3:-1])

greetings = ['hello', 'привет', 'hi', 'morning']
print('\ngreetings')
print(greetings)

mix = numbs + greetings 
print('\nConcatenation: Sum of arrays')
print(mix)
print(type(mix))
numbs = numbs + [101,102,103]
print(numbs)

new = [numbs, greetings]
print('\nArray of arrays')
print(new)
print(new[0])
print(new[0][3])
print(new[-1][-1])

print('\nChanging item')
numbs[3] = 444
print(numbs)

print('\nAdding items to list')
numbs.append(777)
print(numbs)

print('\nRemoving items from list')
del(numbs[6])
print(numbs)

print('\nAdding array as item')
more_numbers = [111, 112, 113]
numbs.append(more_numbers)
print(numbs)
print(numbs[-1])
print(numbs[-1][0])

print('\nList arithmetics')
list_1 = [1,2,3]
list_2 = ['vova', 'zhenya']
list_3 = list_1 + list_2 
print(list_3)
print(list_2*3)
list_4 = [1]*10
print(list_4)

print('\nList initialization v1')
for i in range(0,10): list_5 = [0]*i
print(list_5)

print('\nList initialization v2')
list_6 = [i for i in range(0,10)]
print(list_6)