# Author: Zachariah Tatman
# Date: 6/13/21

'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Twitter.

Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
'''

import sys

# def closest_word(word):
#   return word[::]

# def lev_list(word, words):
#   '''Returns list of levenshtein distances of words'''

def lev_dist(s, t):
  ''' Calculates levenshtein distance between str s and str t. (Dynamic Programming approach using memoization with distance matrix) '''

  # Empty 2D matrix with extra row/col for indeces
  dist_matr = [[0]*(len(t)+1) for i in range(len(s)+1)]

  # Fill column indeces of matrix
  for i in range(1, len(t)+1):
    dist_matr[0][i] = i
  
  # Fill column indeces of matrix
  for i in range(1, len(s)+1):
    dist_matr[i][0] = i
  
  # Find min dist between each in two words
  for i in range(1, len(s)+1):
    print(f'i: {i}')
    for j in range(1, len(t)+1):
      print(f'\tj: {j}')
      print(f'\t\tComparing string \'{s[i-1]}\' to string \'{t[j-1]}\'')
      print(f'\t\tdist[{i-1}][{j-1}]: {dist_matr[i-1][j-1]}')
      print(f'\t\tdist[{i}][{j-1}]: {dist_matr[i][j-1]}')
      print(f'\t\tdist[{i-1}][{j}]: {dist_matr[i-1][j]}')
      if (s[i-1] == t[j-1]):
        # if (len(s[:i]) == len(t[:j])):
        #   print(f'\t\t{s[:i]} and {t[:j]}')
        dist_matr[i][j] = min(dist_matr[i-1][j-1], dist_matr[i][j-1], dist_matr[i-1][j])
        print(f'\t\t!! dist[{i}][{j}]: {dist_matr[i][j]}')
        # else:
        #   dist_matr[i][j] = min(dist_matr[i-1][j-1], dist_matr[i][j-1], dist_matr[i-1][j]) + 1
        #   print(f'\t\t?? dist[{i}][{j}]: {dist_matr[i][j]}')
      else:
        dist_matr[i][j] = min(dist_matr[i-1][j-1], dist_matr[i][j-1], dist_matr[i-1][j]) + 1
        print(f'\t\t?? dist[{i}][{j}]: {dist_matr[i][j]}')
      print(f'\t\t{dist_matr}')

  # Levenshtein Distance
  return dist_matr[len(s)][len(t)]

if __name__ == '__main__':
  # read file
  with open(sys.argv[1]) as f:
    num_cases = int(f.readline())
    for case in range(num_cases):
      query = f.readline().strip()
      words = [word.lower() for word in f.readline().split(',')]
      print(lev_dist('sittmg', 'setting'))