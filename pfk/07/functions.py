#!/usr/bin/env python3
################################################################################
#   functions.py
#
#   chapter 7: Functions
#
#   09.07.2019  Created by:  vo958
################################################################################

def show_name(name='user'):
    print('hello %s' % name)

show_name('vova')

show_name()

def full_name(first_name, last_name):
    print('hello %s %s' % (first_name, last_name))
    
full_name('Vova', 'Kruglyakov')

f_name = 'zhenya'
l_name = 'telukov'

full_name(f_name, l_name)

def add(var1, var2):
    return(var1+var2)
    
total = add(10, 20)

print(total)

x = 100
y = 50
print('%d and %d out of functions code' % (x,y))

def sum1(x,y):
    x *= 10
    y *= 12
    print('%d and %d in functions code' % (x,y))
    return(x+y)

print(sum1(x,y))
print('%d and %d out of functions code' % (x,y))