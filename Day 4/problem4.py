# Author: Zach Tatman
# Date: 5/27/21

'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
'''

def solve(arr):
  assert len(arr) > 0
  assert all(type(int) for n in arr)

  arr.sort()
  min_pos = 1
  for n in arr:
    if n >= 0:
      min_pos = n + 1
      if min_pos not in arr:
          return min_pos
  return min_pos


if __name__ == '__main__':
  try:
    # Case 1: easy
    a1 = [3, 4, -1, 1]
    print(solve(a1))

    # Case 2: easy
    a2 = [1, 2, 0]
    print(solve(a2))

    # Case 3: All zeros
    a3 = [0, 0, 0, 0, 0, 0]
    print(solve(a3))

    # Case 4: All negatives
    a4 = [-23, -2, -1, -4, -2, -99]
    print(solve(a4))

    # Case 5: One zero
    a5 = [0]
    print(solve(a5))

    # Case 6: All negatives
    a6 = [-23, -2, -1, -4, -2, -99]
    print(solve(a6))

    # Case 7: Type error
    # a6 = [-23, '-2', 'hello', -4, -2, -99]
    # solve(a6) 
  except AssertionError as e:
    print(e)
