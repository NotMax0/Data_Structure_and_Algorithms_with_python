class Node:
    data = None
    next_node = None
    def __init__(self, data):
        self.data = data
    def __repr__(self):
        return "<Node data: %s>" % self.data

class LinkedList:
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
    #Append new Node with data at the tail of the list takes O(n) time
        prev = None
        current = self.head
        while current:
            prev = current
            current = current.next_node
        current = Node(data)
        prev.next_node = current


    def add(self, data):
    #Adds new Node containing data at head of the list Takes O(1) time
        new_node = Node(data)
        new_node.next_node = self.head # Reference the Old head Node
        self.head = new_node # Set the Added node As the Head of the linked list
    def search(self, key):
        # Search for the first node containing that key data, returns the node
        # if not found None. Takes O(n) time.
        current = self.head
        while current:
            if current.data == key:
                return current
            else:
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
            new = Node(data)
            position = index
            current = self.head
            while position > 1:
                current = current.next_node
                position -= 1

            # Save the Nodes previous and next that we will insert between.
            prev_n = current
            next_n = current.next_node

            # insert between operation, by changing references.
            prev_n.next_node = new
            new.next_node = next_n
    def remove(self, key):
        current = self.head
        previous = None
        found = False
        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node
        return current

    def remove_index(self, index):
        if index == 0:
            current = self.head
            self.head = self.head.next_node
        # get the Equivalent index of the previous node in the list.
        if index > 0:
            position = index
            current = self.head
            while position > 1:
                current = current.next_node
                position -= 1

            # Save the Nodes previous and next that we will remove between.
            prev_n = current
            next_n = (current.next_node).next_node

            # remove between operation, by changing references.
            prev_n.next_node = next_n
        return current
    def node_at_index(self, index):
        if index == 0:
            return self.head
        else:
            current = self.head
            position = 0
            while position < index:
                current = current.next_node
                position += 1
            return current
            ## Same Code Here:
            # while index > 0:
            #     current = current.next_node
            #     index -= 1
            # return current
    def reverse(self):
        #reverse the linkedlist.
        previous = None
        current = self.head
        while current:
            next_node = current.next_node
            current.next_node = previous
            previous = current
            current = next_node
        self.head = previous

    def __repr__(self):
        # Return a String representation of the list. Takes O(n) time.
        nodes = []
        current = self.head
        while current:
            if current == self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)
            current = current.next_node
        return '-> '.join(nodes)

# list1 = LinkedList()
#
# list1.head = Node(10)
# node1 = Node(3)
# node2 = Node(5)
#
# list1.head.next_node = node1
# node1.next_node = node2
#
# print(list1.size())

l = LinkedList()
l.head = Node(1)
l.add(3)
l.add(2)
print(l.size())
# when return nodes directally
#print(l.__repr__()) # ['[Head: 2]', '[3]', '[Tail: 1]']
l.insert(4, 2)
print(l.remove_index(0))
print(l)
print(l.search(4))
l.reverse()
print(l)
l.append(2)
print(l)
print(l.node_at_index(3).next_node)
