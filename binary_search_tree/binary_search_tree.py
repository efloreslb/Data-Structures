import sys
sys.path.append('../queue_and_stack')
# from dll_queue import Queue
# from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return f'V: {self.value}, Left: {self.left}, Right: {self.right}'
        # return "hello"

    # Insert the given value into the tree
    def insert(self, value):
        # check if new value is less than curr node
        if value < self.value:
            # is there already a value at self.left
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        # the new value is greater than the curr node then go right
        else:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        #if root node is target value
        if target == self.value:
            print("True")
            return True
        
        # target is smaller, go left
        if target < self.value:
            if not self.left:
                print("False")
                return False
            else: 
                return self.left.contains(target)

        # target is greater, go right
        else:
            if not self.right:
                print("False")
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if not self:
            return None

        #return when there is no larger number, cant go right
        if not self.right:
            print(self.value)
            return self.value

        return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)

        if self.left:
            self.left.for_each(cb)

        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


bst = BinarySearchTree(5)
bst.insert(2)
bst.insert(3)
bst.insert(7)
bst.insert(6)
bst.insert(15)
bst.insert(1)
print(bst)
bst.get_max()

bst.contains(10)