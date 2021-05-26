# Daily-Programming-Problems

My solutions to daily programming problems mailed to me by https://www.dailycodingproblem.com/  
I chose to do these problems using Python to practice but you can choose to do them in any programming language you want.

## Daily Coding Problem: Problem #1 [Easy]
Good morning! Here's your coding interview problem for today.

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given `[10, 15, 3, 7]` and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?

## Daily Coding Problem: Problem #2 [Hard]
Good morning! Here's your coding interview problem for today.

This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was `[1, 2, 3, 4, 5]`, the expected output would be `[120, 60, 40, 30, 24]`. If our input was `[3, 2, 1]`, the expected output would be `[2, 3, 6]`.

Follow-up: what if you can't use division?

## Daily Coding Problem: Problem #3 [Medium]
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given the root to a binary tree, implement `serialize(root)`, which serializes the tree into a string, and `deserialize(s)`, which deserializes the string back into the tree.

For example, given the following Node class

`class Node:`
    <br>
     &nbsp;`def __init__(self, val, left=None, right=None):`
     <br>
      &nbsp;&nbsp;&nbsp;`self.val = val`
     <br>
      &nbsp;&nbsp;&nbsp;`self.left = left`
     <br>
      &nbsp;&nbsp;&nbsp;`self.right = right`
     <br>
<br>
The following test should pass:

`node = Node('root', Node('left', Node('left.left')), Node('right'))`
<br>
`assert deserialize(serialize(node)).left.left.val == 'left.left'`
