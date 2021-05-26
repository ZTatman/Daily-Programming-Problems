# Author: Zach Tatman
# Date: 5/26/21

'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
'''


# Create a binary tree class
class Node: 
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def preorder(root):
  if root:
    print(root.val)
  
    preorder(root.left)

    preorder(root.right)
  else:
    return

def insert(root, val):
  if not root:
    return Node(val)
  else: 
    if root.val is val:
      return root
    elif val < root.val:
      root.left = insert(root.left, val)
    elif val > root.val:
      root.right = insert(root.right, val)  
  return root 

def serialize(root):
  nodes = []

  def helper(root, nodes):
    if root:
      # print(f'Appending... {root.val}')
      nodes.append(str(root.val))
      helper(root.left, nodes)
      helper(root.right, nodes)
    else:
      # print(f'Appending... \'n\'')
      nodes.append('n')
    serialized = ','.join(nodes)
    # print(f'Serialized: {serialized}')
    return serialized
  return helper(root, nodes)

def deserialize(tree):
  tree = tree.split(',') 
  root = Node(int(tree[0])) 
  tree.remove(tree[0])
  for val in tree:
    if val == 'n':
      continue
    else:
      # print(f'Deserializing... {val}')
      root = insert(root, int(val))
  return root

# Instantiate tree
root = Node(4)
root = insert(root, 23)
root = insert(root, 1)
root = insert(root, 90)
root = insert(root, 76)
root = insert(root, 30)
assert serialize(root) == serialize(deserialize(serialize(root)))