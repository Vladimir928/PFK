#!/usr/bin/env python3
################################################################################
#   strings.py
#
#   chapter 3 : strings
#
#   07.07.2019  Created by:  vo958
################################################################################

question = 'How are you?'
print(question)
print(question[0:3])
print(question[5])
print(question[:5])
print(question[5:])
print(question[-3:-1])
print(question[-3:])
print('\n')


three_single_quote_str = '''he said, "are't can't souldn't wouldn't"''' 
print(three_single_quote_str)

# Escaping
print('\nEscaping\n')
single_quote_str = 'he said, "are\'t can\'t souldn\'t wouldn\'t"'
print(single_quote_str)

double_qoute_str = "he said, \"are't can't souldn't wouldn't"
print(double_qoute_str)

# multiple strings
print('\n')
text = '''This is the text with
          multiple lines.
this is the last time'''
print(text)

# Embeding values in strings 
print('\n')
age = 17
print('I am %d years old' % age)
name = 'vova'
print('My name is %s. I am %d years old' % (name, age))

# Multiplying strings 
print('\n')
print('2'*5, ' '*10, 'stop'*2)


for i in range(0,10):
    print(' '*i, '\\')
    
for i in range(9,-1,-1):
    print(' '*i, '/')

