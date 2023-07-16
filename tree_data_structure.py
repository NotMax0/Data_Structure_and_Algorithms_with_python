# Binary Search trees are trees on which the parent at most have 2 children.

class Node:
    def __init__(self, data=None):
        self.data = data
        self.node_left = None
        self.node_right = None

    def insert(self, data):
        # Apply recursion to the nodes when are not empty to arrive
        # to the correct position on tree with respect to data
        # Best Case is O(log n) time worst case is O(n) time
        if self.data:
            if data < self.data:
                if self.node_left is None:
                    self.node_left = Node(data)
                else:
                    self.node_left.insert(data)
            elif data > self.data:
                if self.node_right is None:
                    self.node_right = Node(data)
                else:
                    self.node_right.insert(data)
        else:
            self.data = data

    def search(self, data):
        # Best Case is O(log n) time worst case is O(n) time
        print(self.data) # to show the search path.
        if self.data is None:
            return None
        if self.data == data:
            return self
        elif self.data > data:
            if self.node_left is None:
                return None
            else:
                return self.node_left.search(data)
        else:
            if self.node_right is None:
                return None
            else:
                return self.node_right.search(data)
    def remove(self, root, key):
        """
        1- if you are on leaf then set prev node's node_left/node_right to None
        2- if there's another node left or right connect that to the prev node (set prev node's node_left/node_right to
            the Existing node's left or right one).
        3- if you're on a node where it connects two edges (i.e. left and right) get either left.node_right..(the most
            right on left) or right.node_left..(the most left from right) and substitute instead of current
            that is (IF IT"LL BE SET TO CURRENT) current.node_left = prev.node_(left/right).node_left and
            current.node_right = prev.node_(left/right).node_right and prev.node_(left/right) = current.
        Special Cases::-
        - if root is none => return "tree is alread empty"
        :param data:
        :return:
        """
        if root is None:
            return root

        # Search for the node to remove
        if key < root.data:
            # set the returned new sub-root to be the left node of the sub-root....
            root.node_left = self.remove(root.node_left, key)
        elif key > root.data:
            # set the returned new sub-root to be the right node of the sub-root....
            root.node_right = self.remove(root.node_right, key)
        else:
            # Case 1: No child
            if root.node_left is None and root.node_right is None:
                root = None
            # Case 2: Only one child
            elif root.node_left is None:
                # temp = root.node_right
                root = root.node_right
                # temp = None
            elif root.node_right is None:
                # temp = root.node_left
                root = root.node_left
                # temp = None
            # Case 3: 2 children -> left & right
            # in this situation we took the min of right subtree, you can also take the max of the left subtree.
            else:
                temp = self.get_min(root.node_right)
                root.data = temp.data
                root.node_right = self.remove(root.node_right, temp.data)
        return root

    def get_min(self, root):
        current = root
        while current.node_left is not None:
            current = current.node_left
        return current

    def get_max(self, root):
        current = root
        while current.node_right is not None:
            current = current.node_right
        return current
    def PrintTree(self):
        # another print recurrsion
        if self.node_left:
            self.node_left.PrintTree()
        print(self.data),
        if self.node_right:
            self.node_right.PrintTree()

    def In_order_traversal(self, root):
    # Left -> Root -> Right
        res = []
        if root:
            res = self.In_order_traversal(root.node_left)
            res.append(root.data)
            res = res + self.In_order_traversal(root.node_right)
            print(res)
        return res
    def Pre_order_Traversal(self, root):
    # Root -> Left ->Right
        res = []
        if root:
            res.append(root.data)
            res = res + self.Pre_order_Traversal(root.node_left)
            res = res + self.Pre_order_Traversal(root.node_right)
        return res
    def Post_order_Traversal(self, root):
    # Left -> Right -> Root
        res = []
        if root:
            res = self.Post_order_Traversal(root.node_left)
            res = res + self.Post_order_Traversal(root.node_right)
            res.append(root.data)
        return res
    def level_order(self, root):
        if root is None:
            return
        Q = []
        Q.append(root)
        order = []
        while len(Q) > 0:
            current = Q.pop(0)
            order.append(current.data)
            if current.node_left != None:
                Q.append(current.node_left)
            if current.node_right != None:
                Q.append(current.node_right)
        return f"level -> {order}"
    def successor(self, root, node):
        if node.node_right:
            return self.get_min(node.node_right)
        else:
            successor = None
            current = root
            # set the successor to current only when moving current to
            # .node_left
            while current:
                if node.data < current.data:
                    successor = current
                    current = current.node_left
                elif node.data > current.data:
                    current = current.node_right
                else:
                    break
            return successor
    def predecessor(self, root, node):
        if node.node_left:
            return self.get_max(node.node_left)
        else:
            predecessor = None
            current = root
            # set the predecessor to current only when moving current to
            # .node_right
            while current:
                if node.data < current.data:
                    current = current.node_left
                elif node.data > current.data:
                    predecessor = current
                    current = current.node_right
                else:
                    break
            return predecessor
    def __repr__(self):
        return "<Node data: %s>" % self.data


root = Node(12)
root.insert(6)
root.insert(13)
root.insert(14)
root.insert(15)
root.insert(16)
root.insert(3)
# root.PrintTree()
print(root.In_order_traversal(root))
print(root.level_order(root))
print(root.search(3))
print(root.get_max(root))
print(root.get_min(root))

root.remove(root, 16)
root.remove(root, 6)
root.remove(root, 12)
print(root.level_order(root))

root1 = Node(50)
nums = [10, 13, 15, 20, 23, 24, 55, 56, 60, 65]
for num in nums:
    root1.insert(num)
print("\n")
print("\n", root1.In_order_traversal(root1))
node = root1.search(65)
print(root1.successor(root1, node))
print(root1.predecessor(root1, node))


