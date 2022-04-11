from sys import stdin

class Tree:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()

        print(self.value, end=' ');

def predict_tree(preorder, inorder):
    if len(preorder) == 0 or len(inorder) == 0:
        return None

    center = 0
    while preorder[0] != inorder[center]:
        center += 1

    tree = Tree(inorder[center])

    if center != 0:
        tree.left = predict_tree(preorder[1:center+1], inorder[0:center])

    if center != len(preorder):
        tree.right = predict_tree(preorder[center+1:], inorder[center+1:])

    return tree

test_case = int(stdin.readline())
for _ in range(test_case):
    num_of_node = int(stdin.readline())
    preorder = list(map(int, stdin.readline().split()))
    inorder = list(map(int, stdin.readline().split()))

    result = predict_tree(preorder, inorder)
    result.postorder()
    print()

