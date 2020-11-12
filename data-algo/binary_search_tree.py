class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def __repr__(self):
        return f"{self.value}"

        
class BinarySeachTree:
    def __init__(self):
        self.root = None
    
  
    
    def insert(self, value):
        #check if tree has root if not set new node with value as root
        new_node = Node(value)

        if self.root == None:
            self.root = new_node
            return
        current = self.root
        #loop and check nodes if value is greater than currt
        #go to right
        #if smaller go to left i
        # if left or right is none set new_node to left or right

        while current.left != new_node and current.right != new_node:
            if new_node.value > current.value:
                if current.right == None:
                    current.right = new_node
                    return
                else:
                    current = current.right
            else:
                if current.left == None:
                    current.left = new_node
                    return 
                else:
                    current = current.left
    
    def lookup(self, value):
        current = self.root
        while current:
            if current.value == value:
                return True
            elif value > current.value:
                current = current.right
            elif value < current.value:
                current = current.left
        return False
        

    def remove(value):
        pass


    def print_tree(self):
        current = [self.root]
        while current:
            next_ = []
            for node in  current:
                print(node)
                if node.left:
                    next_.append(node.left)
                if node.right:
                    next_.append(node.right)
            current = next_
tree = BinarySeachTree()


tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)
tree.print_tree()
print(tree.lookup(170))
print(tree.lookup(70))
