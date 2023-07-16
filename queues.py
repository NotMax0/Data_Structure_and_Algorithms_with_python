class Queue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.queue = []
    def enqueue(self,data):
        if self.is_full():
            return "Queue is full"
        self.queue.append(data)
    def dequeue(self):
        self.queue.pop(0)
    def is_empty(self):
        return len(self.queue) == 0
    def is_full(self):
        return (len(self.queue) == self.max_size)
    def __repr__(self):
        return "Queue %s " % self.queue

# single_queue = Queue(2)
# single_queue.enqueue(4)
# single_queue.enqueue(5)
# single_queue.dequeue()
# single_queue.enqueue(9)
# print(single_queue)

# My Implementation of Circular Queues
class CircularQueue:
    """
    in Circular Queues the head points to the first index item in queue
    and Tail points to the slot after the last index item in queue.
    """
    def __init__(self, max_size):
        self.max_size = max_size
        self.queue = [None] * max_size
        self.head = 0
        self.tail = 0
    def enqueue(self, data):
        if self.is_full():
            return "Queue is full"
        self.queue[self.tail] = data
        self.tail = (self.tail + 1) % self.max_size

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        data = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_size
        return data

    def is_empty(self):
        return self.head == self.tail and self.queue[self.head] is None
    def is_full(self):
        return self.head == self.tail and self.queue[self.head] is not None

    def get_head(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue[self.head]
    def get_tail(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue[self.tail]

    def size(self):
        if self.tail == self.head and self.queue[self.head] is not None:
            return self.max_size
        elif self.tail >= self.head:
            return self.tail - self.head
        else:
            return self.max_size - self.head + self.tail

    def clear(self):
        self.queue = [None] * self.max_size
        self.head = 0
        self.tail = 0
    def __repr__(self):
        return "Queue: %s" % self.queue


circle_queue = CircularQueue(5)
circle_queue.enqueue(1)
circle_queue.enqueue(2)
circle_queue.enqueue(3)
circle_queue.enqueue(1)
circle_queue.dequeue()
circle_queue.dequeue()
circle_queue.dequeue()
circle_queue.enqueue(3)
circle_queue.enqueue(1)

print(circle_queue.size())
print(circle_queue.is_full())
print(circle_queue)


class ArrayQueueType:
    """
    AddQueue and DeleteQueue both take O(1) time
    """
    def __init__(self, max_length):
        self.front = 0
        self.max_length = max_length
        self.rear = max_length - 1
        self.length = 0
        self.arr = [0] * max_length
    def is_empty(self):
        return (self.length == 0)
    def is_full(self):
        return (self.length == self.max_length)
    def addQueue(self, element):
        if (self.is_full()):
            return "Queue full can't Enqueue ...!"
        self.rear = (self.rear + 1) % self.max_length
        self.arr[self.rear] = element
        self.length += 1
    def deleteQueue(self):
        if (self.is_empty()):
            return "Queue is already Empty ...!"
        deleted = self.arr[self.front]
        self.arr[self.front] = 0
        self.front = (self.front + 1) % self.max_length
        self.length -= 1
        return deleted
    def frontQueue(self):
        assert(self.is_empty())
        return self.arr[self.front]
    def rearQueue(self):
        assert(self.is_empty())
        return self.arr[self.rear]
    def search(self, elem):
        return self.arr.index(elem)
    def __repr__(self):
        return "Queue: %s" % self.arr

q1 = ArrayQueueType(4)
q1.addQueue(3)
q1.addQueue(1)
q1.addQueue(2)
q1.addQueue(4)
q1.deleteQueue()
q1.deleteQueue()
q1.addQueue(5)
q1.addQueue(6)
q1.deleteQueue()
q1.addQueue("Karren")
print(q1.is_full())
print(q1)
print(q1.search(6))
