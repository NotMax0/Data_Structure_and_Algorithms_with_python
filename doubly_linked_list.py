class Node:
    data = None
    prev_node = None
    next_node = None
    def __init__(self, data):
        self.data = data
    def __repr__(self):
        return "<Node data: %s>" % self.data

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    def is_empty(self):
        return self.head == None
    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next_node
        return count
    def append(self, data):
        #add nodes of data at the tail requires O(1) to add and O(n) to access
        current = self.head
        new_node = Node(data)
        while current.next_node:
            current = current.next_node
        current.next_node = new_node
        new_node.prev_node = current
        new_node.next_node = None
    def add(self, data):
    # add new node containing data at the head of the list takes O(1) time
        new_node = Node(data)
        self.head.prev_node = new_node
        new_node.next_node = self.head
        self.head = new_node
    def search(self, key):
    # Search for the first node containing that key data, returns the node
    # if not found None. Takes O(n) time.
        current = self.head
        while current:
            if (current.data == key):
                return current
            current = current.next_node
        return None
    def insert(self, data, index):
    # Inserts a new Node containing data at index position
    # Insertion Takes O(1) time but finding the node at the
    # insertion point takes O(n) time. Overall O(n) linear time.
        if index == 0:
            self.add(data)
        # get the Equivalent index of the previous node in the list.
        if index > 0:
            current = self.head
            new_node = Node(data)
            while index > 1:
                current = current.next_node
                index -= 1
            current.next_node.prev_node = new_node
            new_node.next_node = current.next_node
            current.next_node = new_node
            new_node.prev_node = current
    def remove(self, key):
        current = self.head
        while current:
            if current.data == key:
                if current is self.head:
                    self.head = current.next_node
                    if current.next_node:
                        current.next_node.prev_node = None
                else:
                    current.prev_node.next_node = current.next_node
                    if current.next_node:
                        current.next_node.prev_node = current.prev_node
                current.next_node = None
                current.prev_node = None
                return current
            current = current.next_node
        return None
    def remove_at_index(self, index):
        current = self.head
        if index == 0:
            self.head = current.next_node
            if current.next_node:
                current.next_node.prev_node = None
        while index > 0:
            current = current.next_node
            index -= 1
        current.prev_node.next_node = current.next_node
        if current.next_node:
            current.next_node.prev_node = current.prev_node
        current.next_node = None
        current.prev_node = None
        return current
    def node_at_index(self, index):
        current = self.head
        while index > 0:
            current = current.next_node
            index -= 1
        return current
    def reverse(self):
        current = self.head
        while current:
            if current is self.head:
                current.prev_node = current.next_node
                current.next_node = None
            elif current.next_node is None:
                current.next_node = current.prev_node
                current.prev_node = None
                self.head = current
            else:
                next = current.prev_node
                current.prev_node = current.next_node
                current.next_node = next
            current = current.prev_node
    def __repr__(self):
        node = []
        current = self.head
        while current:
            if current == self.head:
                node.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                node.append("[Tail: %s]" % current.data)
            else:
                node.append("[%s]" %current.data)
            current = current.next_node
        return ' <-> '.join(node)



# dl = DoublyLinkedList()
# dl.head = Node(1)
# node2 = Node(2)
# node3 = Node(3)
#
# dl.head.prev_node = None
# dl.head.next_node = node2
#
# node2.prev_node = dl.head
# node2.next_node = node3
#
# node3.prev_node = node2
# node3.next_node = None

dl = DoublyLinkedList()
dl.head = Node(2)
dl.add(1)
dl.add(3)
dl.add(5)
# dl.insert(2, 1)
# dl.remove(3)
#
# print(dl.remove_at_index(1))
# print(dl.search(0))
# print(dl.node_at_index(2))
# dl.add(6)
print(dl)
dl.reverse()
# dl.append(0)
# dl.append(3)
print(dl)
