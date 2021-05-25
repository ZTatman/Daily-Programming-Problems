# Author: Zach Tatman
# Date: 5/25/21

'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
'''


def solve_no_div(numbers):
  ''' This solution uses brute force method
      and avoids using division'''

  result = []

  for i, n in enumerate(numbers):
    product = 1
    # print('{}:'.format(i))
    new_numbers = numbers[:]
    new_numbers.remove(numbers[i])
    for j, m in enumerate(new_numbers):
      product *= new_numbers[j]
      # print('\t{}'.format(product))
    result.append(product)
  # print(result)
  return result


with open('problem2Input.in') as file:
  num_cases = int(file.readline())
  for case in range(num_cases):
    nums = file.readline().split()
    nums = [int(n) for n in nums]
    print('Case {}:\n{}\n'.format(case+1, solve_no_div(nums)))