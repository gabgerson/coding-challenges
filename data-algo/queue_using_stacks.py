class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.enqueue_stack = []
        self.dequeue_stack = []
        
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        #push element so enqueue stack
        self.enqueue_stack.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """

        if len(self.dequeue_stack) == 0:
          
            #loop through enqueue_stack in reverse and append them to dequeue_stack
            for item in self.enqueue_stack[::-1]:
                
                self.dequeue_stack.append(item)
            self.enqueue_stack = []
  
            #pop last element from dequeue_Stack
        return self.dequeue_stack.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """

        if len(self.dequeue_stack) == 0:
            for item in self.enqueue_stack[::-1]:
             
                self.dequeue_stack.append(item)
            self.enqueue_stack = []
        return self.dequeue_stack[-1]
    
    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if len(self.dequeue_stack) == 0 and len(self.enqueue_stack) == 0:
            return True
        else:
            return False
        