# Author: Zach Tatman
# Date: 06/02/2021


'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
'''
import sys 
import string

def decode(msg):
  count = 0

  # Base case
  if len(msg) == 0:
    return 1
  if len(msg) == 1:
    return 1
  
  # Look at 1 letter first 
  if msg[len(msg) - 1] >= '1':
    # print(f'new_msg: {msg[:-1]}')
    count = decode(msg[:-1])
  # Look at 2 letters next
  if (msg[len(msg) - 2] == '1' 
  or (msg[len(msg) - 2] == '2' 
  and msg[len(msg) - 1] < '7')):
    count += decode(msg[:-2])
  
  return count

if __name__ == '__main__':

  # Mapping 
  # map = {n:c for n, c in enumerate(string.ascii_lowercase, start=1)}

  # Read file
  with open(sys.argv[1], 'r') as file:
    num_cases = int(file.readline())
    
    # Read each case
    for case in range(num_cases):
      msg = file.readline().split()
      msg = ''.join(msg)
      print(decode(msg))
