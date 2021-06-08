# Author: Zachariah Tatman
# Date: 6/8/21

'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
'''
import sys
import math


def largest_sum(arr):
  '''Returns the largest sum of non-adjacent numbers'''
  incl = arr[0]
  incl_sum = arr[0]
  excl_sum = 0

  # print(' i: 0')
  # print(f'\tCurr el: {arr[0]}')
  # print(f'\tIncl sum: {incl_sum}')
  # print(f'\tExcl sum: {excl_sum}')
  for i in range(1,len(arr)):
    incl_sum = excl_sum + arr[i]
    excl_sum = max(excl_sum, incl)
    incl = incl_sum
    # print(f'i: {i}')
    # print(f'\tCurr el: {arr[i]}')
    # print(f'\tIncl sum: {incl_sum}')
    # print(f'\tExcl sum: {excl_sum}')
  return max(excl_sum, incl_sum)
  


if __name__ == '__main__':
  with open(sys.argv[1], 'r') as file:
    cases = int(file.readline())
    for case in range(cases):
      try:
        arr = [int(x) for x in file.readline().split()]
        print(f'Max Sum: {largest_sum(arr)}')
      except ValueError as e:
        print(f'Error: {e}')
