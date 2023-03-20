# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 18:34:20 2023

@author: Hannah
"""

from ArrayDeque import ArrayDequeMaxlen

AQM = ArrayDequeMaxlen(100)

# adding last
print('\nAdding last')
for i in range(100):
    AQM.append(i)
    print(i, AQM._data)

print('\nDelete 80', AQM.remove(80), AQM._data, AQM._front)

# adding first
print('\nAdding first')
for i in range(20, 10, -1):
    AQM.appendleft(i)
    print(i, AQM._data)

print(AQM._front)

# performing the removals

print('\nPerforming the removals')
while not AQM.is_empty():
    AQM.pop()
    print('removing last', AQM.pop(), AQM._data)