# Author: Zach Tatman
# Date: 5/24/21

'''
Good morning! Here's your coding interview problem for today.

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
'''

def solve(numbers, lo, hi, k):
  '''Binary Search can be used to determine if any two numbers
     in a sorted list of numbers are able to add up to K.'''

  if hi > lo:
    
    mid = lo + (hi - lo) // 2 

    if numbers[mid] + numbers[mid+1] == k:
      print('True: {} + {} = {}\n'.format(numbers[mid], numbers[mid+1], k))
      return True

    elif numbers[mid] + numbers[mid+1] < k:
      return solve(numbers, mid+1, hi, k)

    else:
      return solve(numbers, lo, mid, k)
  else:
    print('False: No two numbers add up to {}\n'.format(k))
    return False


with open('problem1Input.in', 'r') as file:
  numcases = int(file.readline())
  for case in range(numcases):
    k = int(file.readline())
    numbers = list(file.readline().split())
    numbers = [int(s) for s in numbers]
    numbers.sort()
    print('Case: {}\nNumbers: {}\nK: {}'.format(case+1, numbers, k))
    solve(numbers, 0, len(numbers) - 1, k)