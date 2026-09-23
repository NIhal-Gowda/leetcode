class MyQueue(object):

    def __init__(self):
        # s1 handles incoming elements (push)
        self.s1 = []
        # s2 handles outgoing elements (pop/peek)
        self.s2 = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        # Always push onto the input stack
        self.s1.append(x)

    def pop(self):
        """
        :rtype: int
        """
        # Ensure s2 has elements to pop from
        self.peek()
        return self.s2.pop()

    def peek(self):
        """
        :rtype: int
        """
        # If the output stack is empty, transfer everything from s1 to s2
        # This reverses the order from LIFO to FIFO!
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    def empty(self):
        """
        :rtype: bool
        """
        # The queue is empty only if BOTH stacks are empty
        return not self.s1 and not self.s2
