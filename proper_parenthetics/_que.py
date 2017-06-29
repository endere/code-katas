import sys


class Node(object):
    """Creates a Node."""
    def __init__(self, value, next_up=None):
        self.value = value
        self.next = next_up
        self.behind = None


class Queue(object):
    """Creates a Queue from value or list."""
    def __init__(self, optional_values=[]):
        self.head = None
        self.tail = None
        self.length = 0
        self.is_empty = True
        for x in optional_values:
            self.enqueue(x)

    def enqueue(self, value):
        """Adds node to end of queue."""
        self.tail = Node(value, self.tail)
        if self.length == 0:
            self.head = self.tail
        if self.tail.next is not None:
            self.tail.next.behind = self.tail
        if self.is_empty is True:
            self.is_empty = False
        self.length += 1

    def dequeue(self):
        """Removes node from head of queue."""
        if self.head is None:
            return "Queue is empty."
        head = self.head
        if self.head == self.tail:
            self.tail = None
            self.head = None
        else:
            self.head.behind.next = None
            self.head = self.head.behind
        self.length -= 1
        if self.length == 0:
            self.is_empty = True
        return head

    def peek(self):
        """Return value of head."""
        if self.head is None:
            return "Queue is empty."
        return self.head.value

    def size(self):
        """Returns length of queue."""
        return self.length

    def __len__(self):
        """Returns length of queue."""
        return self.size()
