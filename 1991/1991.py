from sys import stdin
from enum import Enum

"https://www.acmicpc.net/problem/1991 트리 순회 <Silver I>"

Direction = Enum("Direction", "left right")

class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, direction, sub_tree):
        if direction == Direction.left:
            self.left = sub_tree
        elif direction == Direction.right:
            self.right = sub_tree

    def preorder(self, func):
        func(self.data)
        if self.left != None:
            self.left.preorder(func)
        if self.right != None:
            self.right.preorder(func)

    def inorder(self, func):
        if self.left != None:
            self.left.inorder(func)
        func(self.data)
        if self.right != None:
            self.right.inorder(func)

    def postorder(self, func):
        if self.left != None:
            self.left.postorder(func)
        if self.right != None:
            self.right.postorder(func)
        func(self.data)

trees = {}
alphabet = map(lambda x: chr(65 + x), range(26))
trees.update([(a, Tree(a)) for a in alphabet])
trees['.'] = None

num_of_sub_tree = int(stdin.readline())
for _ in range(num_of_sub_tree):
    main, left, right = stdin.readline().split()
    main_tree = trees[main]

    left_tree = trees[left]
    main_tree.insert(Direction.left, left_tree)

    right_tree = trees[right]
    main_tree.insert(Direction.right, right_tree)

print_elem = lambda x: print(x, end='')
root_tree = trees['A']
root_tree.preorder(print_elem)
print()
root_tree.inorder(print_elem)
print()
root_tree.postorder(print_elem)
print()
