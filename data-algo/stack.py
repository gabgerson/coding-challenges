class Node:

    def __init__(self,value):
        self.value = value
        self.next = None

class Stack:

    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0
    
    def peek(self):
        #show top item
        return self.top.value

    def push(self, value):
        
        #if nothing is in the stack item being pushed is bottom and top
        new_node = Node(value)
        if self.bottom == None:
            self.top = new_node
            self.bottom = new_node
        
        else:
            
            #current top's next is new_node
            self.top.next = new_node
            #add node to top of stack
            self.top = new_node

    def _pop(self):
        pass

my_stack = Stack()

