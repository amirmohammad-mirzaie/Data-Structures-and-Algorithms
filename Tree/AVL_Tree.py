'''
    File name: avl.py
    Author: Amir Mohammad Mirzaie
    email: amirm57@gmail.com
    Date created: April/16/2020
    Python Version: 3.7
'''

class Node(object):
    def __init__(self, value):
        self.avalue = value
        self.left = None
        self.right = None
        self.height = 0


class AVL_Tree(object):
    def __init__(self, root_value):
        self.root = Node(root_value)

    # method to insert values to the tree
    def insert(self, value):
        self.root = self.go_inside(value, self.root)

    # helper method for insert method above.
    # by using this, we'll be able to create the AVL tree
    def go_inside(self, value, node):
        # if there is no node, currently, we create one and return it
        if not node:
            return Node(value)
        # if it already exists, we return it
        if node.avalue == value:
            return node

        # else if the value is greater than the current node's value, go to right
        elif value > node.avalue:
            node.right = self.go_inside(value, node.right)


        # else the value is less than or equal to the current node's value, go to left
        else:
            node.left = self.go_inside(value, node.left)

        # update the node regarding it's children
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

        difference = self.get_difference_condition(node)

        # 1st situation in which the node is doubly left heavy
        if difference > 1 and value < node.left.avalue:
            print('case 1')
            return self.rotate_right(node)

        # 2nd situation in which the node is left right heavy
        if difference > 1 and value > node.left.avalue:
            print('case 2')
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        # 3rt situation in which the node is doubly right heavy
        if difference < -1 and value > node.right.avalue:
            print('case 3')
            return self.rotate_left(node)

        # 4th situation in which the node is right left heavy
        if difference < -1 and value < node.right.avalue:
            print('case 4')
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        return node

    # calculate the height of a node
    def get_height(self, node):
        if node is None:
            return -1
        else:
            return node.height

    # calculate the difference of the left child's height and the right child's height
    def get_difference_condition(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    # rotate node rightwise
    def rotate_right(self, node):
        y = node.left
        y_right = y.right

        y.right = node
        node.left = y_right
        node.height = 1 + max(self.get_height(node.right), self.get_height(node.left))
        y.height = 1 + max(self.get_height(y.right), self.get_height(y.left))
        return y

    # rotate node leftwise
    def rotate_left(self, node):
        y = node.right
        y_left = y.left

        y.left = node
        node.right = y_left
        node.height = 1 + max(self.get_height(node.right), self.get_height(node.left))
        y.height = 1 + max(self.get_height(y.right), self.get_height(y.left))
        return y

    # TODO: write methods for removing an element from the tree


tree = AVL_Tree(40)
tree.insert(20)
tree.insert(10)
tree.insert(30)
tree.insert(50)
tree.insert(5)
tree.insert(15)
tree.insert(17)
tree.insert(14)
tree.insert(16)
tree.insert(18)
tree.insert(19)
