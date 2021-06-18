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

def lev_dict(query, words):
  '''Returns a dict of word values with key levenshtein distances'''
  lev = {}

  for word in words:
    dist = lev_dist(query, word)

    if dist not in lev:
      lev[dist] = []
      lev[dist].append(word)
    else:
      lev[dist].append(word)
  return lev

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
    # print(f'i: {i}')
    for j in range(1, len(t)+1):
      # print(f'\tj: {j}')
      # print(f'\t\tComparing string \'{s[i-1]}\' to string \'{t[j-1]}\'')
      # print(f'\t\tdist[{i-1}][{j-1}]: {dist_matr[i-1][j-1]}')
      # print(f'\t\tdist[{i}][{j-1}]: {dist_matr[i][j-1]}')
      # print(f'\t\tdist[{i-1}][{j}]: {dist_matr[i-1][j]}')

      # First string is empty
      if (len(s) == 0):
        dist_matr[i][j] = i
      
      # Second string is empty
      elif (len(t) == 0):
        dist_matr[i][j] = j

      # Letters being compared are the same
      if (s[i-1] == t[j-1]):

        # Letter being compared same as last letter compared (i.e., second 'l' in hello)
        if (t[j-1] == t[j-2]):
          dist_matr[i][j] = min(dist_matr[i-1][j-1], dist_matr[i][j-1], dist_matr[i-1][j]) + 1
          # print(f'\t\tDD dist[{i}][{j}]: {dist_matr[i][j]}')
        else:
          dist_matr[i][j] = min(dist_matr[i-1][j-1], dist_matr[i][j-1], dist_matr[i-1][j])
          # print(f'\t\t!! dist[{i}][{j}]: {dist_matr[i][j]}')

      # Letters being compared are not the same
      else:
        dist_matr[i][j] = min(dist_matr[i-1][j-1], dist_matr[i][j-1], dist_matr[i-1][j]) + 1
      #   print(f'\t\t?? dist[{i}][{j}]: {dist_matr[i][j]}')
      # print(f'\t\t-> {dist_matr}')

  # Levenshtein Distance
  return dist_matr[len(s)][len(t)]

def find_closest(query, d):
  words = d[min(list(d.keys()))]

  def bin_search(query, d, lo, hi):
    if hi >= lo:
      
      mid = lo + (hi - lo) // 2 
      # print('Mid: {}'.format(words[mid]))
      if query <= words[mid]:
        # print('Closest words: {}'.format(words[:mid+1]))
        return words[:mid+1]

      elif query < words[mid]:
        return bin_search(query, words, lo, mid)

      else:
        return bin_search(query, words, mid+1, hi)
    else:
      return False   
  return bin_search(query, words, 0, len(words)-1)
    



if __name__ == '__main__':
  # read file
  with open(sys.argv[1]) as f:
    num_cases = int(f.readline())
    for case in range(num_cases):
      query = f.readline().strip()
      words = sorted([word.lower().strip() for word in f.readline().split(',')])
      search_dict = lev_dict(query, words)
      print(find_closest(query, search_dict))