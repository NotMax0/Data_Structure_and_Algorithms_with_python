def merge_sort(list):
    """
    sort a list in ascending order: Returns a new list
    Divide: Find the midpoint of the list and divide into sublists
    Conquer: Recursively sort the sublists created in previous step
    Combine: Merge the sorted sublists created in prevous step

    Takes O(n log n) time; in reality it takes O(kn log n) time
    merge sort takes Space Complexity of O(n) space.
    """
    # this is the Stopping Condition
    if len(list) <= 1:
        return list

    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(list):
    """
    Divide the unsorted list at midpoint into sublists
    Returns two sublists - lift and right

    Takes Overall O(log n) runtime; but reality is O(k log n) runtime because there is a slice operation for each split
    wehre k represent the slice size.
    """
    mid = len(list)//2
    left = list[:mid]
    right = list[mid:]
    return left, right

def merge(left , right):
    """
    Merges two lists (arrays), sorting them in the process.
    :return: a new merged list

    Runs in Overall O(n) time
    """
    l = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i+=1
        else:
            l.append(right[j])
            j+=1
    while i < len(left):
        l.append(left[i])
        i+=1
    while j < len(right):
        l.append(right[j])
        j+=1
    return l

def verify_sorted(list):
    n = len(list)
    if n == 0 or n == 1:
        return True
    return list[0] < list[1] and verify_sorted(list[1:])

# sorted = merge([3, 1], [0]) #You can't have [3, 1] because the arrays
# must split and sorted with single elements.[3] and [1] here
sorted = merge([2, 4, 8], [2, 6, 7])
print(sorted)

alist = [54, 62, 93, 17, 77, 31, 44, 55, 20]
l = merge_sort(alist)
print(l)
print(verify_sorted(l))
