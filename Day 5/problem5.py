# Author: Zach Tatman
# Date: 5/30/2021

'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Jane Street.

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
    
Implement car and cdr.
'''

# Closure used to retain state with inner function
def cons(a, b):
  # f = a function passed as a parameter
  def pair(f):
    # return return to pair result of function f
    return f(a, b)
  return pair

def car(pair):
  # function 'f'
  def first_el(a, b):
    return a
  # return callable object
  return pair(first_el)

def cdr(pair):
  # function 'f'
  def last_el(a, b):
    return b
  # return callable object
  return pair(last_el)



print(car(cons(3,4)))
print(cdr(cons(3,4)))
