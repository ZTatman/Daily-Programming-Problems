# Author: Zach Tatman
# Date: 5/30/2021

'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev fields, it holds a field named both, which is an XOR of the next node and the previous node. Implement an XOR linked list; it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python), you can assume you have access to get_pointer and dereference_pointer functions that converts between nodes and memory addresses.
'''

class Node:
  def __init__(self, data=None):
    self.both = 0
    self.data = data

class LinkedList:
  def __init__(self):
    self.head = None

  def add(self, data):
    new_node = Node(data)
    if self.head is None:
       self.head = new_node
    else:
      temp = self.head
      while (temp.next):
        temp = temp.next
      temp.next = new_node

  def display(self):
    node = self.head
    nodes = []
    while node is not None:
        nodes.append(str(node.data))
        node = node.next
    nodes.append("None")
    print(" -> ".join(nodes))

  # def xor(a=0, b=0):


  # def addresses(self):
  #   node = self.head
  #   nodes = []
  #   while node is not None:
  #     nodes.append(str(id(node)))
  #     node = node.next
  #   nodes.append('None')
  #   print(" -> ".join(nodes))

  # def get(self, index):
  #   temp = self.head

if __name__ == '__main__':
  ll = LinkedList()
  ll.add(1)
  ll.add(2)
  ll.add(3)
  ll.display()
  ll.addresses()