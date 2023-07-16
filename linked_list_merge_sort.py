
from linked_list import LinkedList

def merge_sort(linked_list):
    """
    Sorts a linked list in ascending order
    - Recursively divide the linked list into sublists containing a single node
    - Repeatedly merge the sublists to produce sorted sublists until one remains

    :return a sorted linked list
    Runs in O(kn log n) time
    Space Complexity is O(n) space;
        since the new linked lists are created one at a time and the old ones are
        no longer needed once they have been merged, the total amount of space required
        at any given time is proportional to the size of the original list.
    """
    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head is None:
        return linked_list

    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(linked_list):
    """
    Divide the unsorted list at midpoint into sublists
    Takes O(k log n) time; whereas k is the node_at_index traversal runtime of O(k) method which is n/2
    """
    if linked_list == None or linked_list.head == None:
        left_half = linked_list
        right_half = None
        return left_half, right_half
    else:
        size = linked_list.size()
        mid = size//2

        mid_node = linked_list.node_at_index(mid-1)

        left_half = linked_list
        right_half = LinkedList()
        right_half.head = mid_node.next_node
        mid_node.next_node = None

        return left_half, right_half
def merge(left, right):
    """
    Merges two linked lists, sorting by data in nodes
    Returns a new merged list.
    Runs in O(n) time.
    """
    # Create a new linked list that contains nodes from
    # merging left and right
    merged = LinkedList()

    # Add a fake head that is discarded later
    merged.add(0)

    # Set current to the head of the linked list
    current = merged.head

    # Obtain head nodes for left and right linked lists.
    left_head = left.head
    right_head = right.head

    # Iterate over left and right until we reach the tail node
    # of either
    while left_head or right_head:
        # If the head node of left is None, we're past the tail
        # Add the node from right to merged linked list
        if left_head == None:
            current.next_node = right_head
            # Call next on right to set loop condition to False
            right_head = right_head.next_node
        elif right_head == None:
            current.next_node = left_head
            # Call next on left to set loop condition to False
            left_head = left_head.next_node
        else:
            # Not at either tail Nodes
            # Obtain node data to perform comparison operations
            left_data = left_head.data
            right_data = right_head.data
            # If data on left is less than right, set current to left node
            if left_data < right_data:
                current.next_node = left_head
                # Move left head to next node
                left_head = left_head.next_node
            # If data on left is greater than right, set current to right node
            else:
                current.next_node = right_head
                # Move right head to next node
                right_head = right_head.next_node
        # Move current to the next node
        current = current.next_node

    # Discard fake head and set first merged node as head
    head = merged.head.next_node
    merged.head = head

    return merged

l = LinkedList()
l.add(4)
l.add(3)
l.add(2)
l.add(1)
print('\n', l)
# left, right = split(l)
# print(left, right)
index = l.node_at_index(2)
print(index)
left, right = split(l)
print(left, right)

l2 = LinkedList()
l2.add(10), l2.add(2), l2.add(44), l2.add(15), l2.add(200)
print(l2)
sorted_linked_list = merge_sort(l2)
print(sorted_linked_list)

# Try
# def split(linked_list):
    ## the add method pre-pend from the head of the linked list.
    # current = linked_list.head
    # mid = linked_list.size() //2
    # left = LinkedList()
    # right = LinkedList()
    # for i in range(mid):
    #     left.add(current.data)
    #     current = current.next_node
    # for i in range(mid, linked_list.size()):
    #     right.add(current.data)
    #     current = current.next_node
    #
    # return left, right
