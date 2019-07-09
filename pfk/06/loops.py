#!/usr/bin/env python3
################################################################################
#   loops.py
#
#   chapter 6: loops
#
#   09.07.2019  Created by:  vo958
################################################################################

print('Loop for')

for i in range(0,5,1):
    print('This is %d line of text' %(i+1))
print('\n')
for i in range(5):
    print('This is again %d line of text' %(i+1))

print('\nLists and Range')
print(list(range(10,20,5)))

#iteration(repetition)

games = ['Minecraft', 'WOT', 'Thief', 'Soma']
print(len(games), games)

# 1 variant 
print('\n')
for g in range(len(games)):
    print(games[g])
    
# 2 variant
print('\n')
for game in games:
    print(game)
    
days_of_week = ('Mon', 'Tue', 'Wen', 'Thu', 'Fri', 'Sat', 'Sun')
print(days_of_week)

print('\n')
for day in days_of_week:  print(day) 

print('\nWHILE')
step = 0
while (step < 10):
    print(step)
    if (step < 5):
        step += 1
    else:
        step += 2

print('\nWhile true loop')
step = 0 
while True:
    print(step)
    step += 1
    if (step == 500):
        break
