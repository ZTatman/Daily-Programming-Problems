# Author: Zachariah Tatman
# Date: 6/4/2021

'''

'''
import sys

class Node:
  '''Node class'''
  def __init__(self, data):
    self.data = data
    self.right = None
    self.left = None

# class Tree: 
#   '''Tree class'''
#   def __init__(self):
#     self.root = None

#   def add(self, val):
#     if self.root is None:
#       self.root = Node(val)
#     else:
#       self.add_(self.root, val)

  # def add_(self, root, val):
  #   if root.data < val:
  #     if root.left is not None:
  #       self.add_(root.left, val)
  #     else:
  #       root.left = Node(val)
  #   else:
  #     if root.right is not None:
  #       self.add_(root.right, val)
  #     else:
  #       root.right = Node(val)

  # def display(self):
  #   if self.root:
  #     self.display_(self.root)

  # def display_(self, node):
  #     if node is not None:
  #         self.display_(node.left)
  #         print(str(node.data) + ' ')
  #         self.display_(node.right)

def unival_count(root):
  count = [0]
  unival_count_(root, count)
  return count

def unival_count_(root, count):

  if root is None:
    return True
  
  # Traverse tree in postorder: L,R,M
  left = unival_count_(root.left, count)
  right = unival_count_(root.right, count)

  # If one subtree is false, return false
  if left == False or right == False:
    return False

  if root.left and root.left.data is not root.data:
    return False
  
  if root.right and root.right.data is not root.data:
    return False

  count[0] += 1
  return True

  
if __name__ == '__main__':
  # Tree
  root = Node(0)
  root.left = Node(1)
  root.right = Node(0)
  root.right.left = Node(1)
  root.right.right = Node(0)
  root.right.left.left = Node(1)
  root.right.left.right = Node(1)
  # Unival subtrees count
  print(unival_count(root)[0])
