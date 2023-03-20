# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 18:34:01 2023

@author: Hannah
"""
class Empty(Exception):
    pass

class ArrayDequeMaxlen:
    def __init__(self, maxlen):
        self._data = [None] * maxlen
        self._size = 0
        self._front = 0
        self._maxlen = maxlen

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._data[self._front]

    def last(self):
        if self.is_empty():
            raise Empty('Deque is empty')
        back = (self._front + self._size - 1) % self._maxlen
        return self._data[back]

    def append(self, e):
        if self._size == self._maxlen:
            raise Exception('Deque is full')
        back = (self._front + self._size) % self._maxlen
        self._data[back] = e
        self._size += 1

    def appendleft(self, e):
        if self._size == self._maxlen:
            raise Exception('Deque is full')
        self._front = (self._front - 1) % self._maxlen
        self._data[self._front] = e
        self._size += 1

    def remove(self, e):
        if self.is_empty():
            raise Empty('Deque is empty')
        index = -1
        for i in range(self._size):
            if self._data[(self._front + i) % self._maxlen] == e:
                index = i
                break
        if index == -1:
            raise ValueError('Element not found')
        for i in range(index, self._size-1):
            self._data[(self._front + i) % self._maxlen] = self._data[(self._front + i + 1) % self._maxlen]
        self._data[(self._front + self._size - 1) % self._maxlen] = None
        self._size -= 1
        return e

    def delete_first(self):
        if self.is_empty():
            raise Empty('Deque is empty')
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % self._maxlen
        self._size -= 1
        return answer

    def delete_last(self):
        if self.is_empty():
            raise Empty('Deque is empty')
        back = (self._front + self._size - 1) % self._maxlen
        answer = self._data[back]
        self._data[back] = None
        self._size -= 1
        return answer
    
    def pop(self):
        return self.delete_last()

    def popleft(self):
        return self.delete_first()

    def add_first(self, e):
        self.appendleft(e)

    def add_last(self, e):
        self.append(e)



   
    


