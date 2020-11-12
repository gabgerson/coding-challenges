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
        if self.root == None:
            return False
        current = self.root
        while current:
            if current.value == value:
                return True , current
            elif value > current.value:
                current = current.right
            elif value < current.value:
                current = current.left
        return False
        

    def remove(self,value):
        if self.root == None:
            return False

        current_node = self.root

        parent_node = None

        while current_node:
            if value < current_node.value:
                parent_node = current_node
                current_node = current_node.left
            elif value > current_node.value:
                parent_node = current_node
                current_node = current_node.right

            elif current_node.value == value:
                if current_node.right == None:
                    if parent_node == None:
                        self.root = current_node.left
                        return
                    else:
                        if current_node.value < parent_node.value:
                            parent_node.left = current_node.left
                            return
                        elif current_node.value > parent_node.value:
                            perent_node.right = current_node.left
                            return
                elif current_node.left == None:
                    if parent_node == None:
                        self.root = current_node.right
                        return
                    else:
                        if current_node.value < parent_node.value:
                            parent_node.left = current_node.right
                            return
                        elif current_node.value > parent_node.value:
                            parent_node.right = current_node.right
                            return
                elif current_node.left == None and current.right == None:
                    if parent_node == None:
                        current_node = None
                        return
                    if parent_node.value > current_node.value:
                        parent_node.left = None
                        return
                    else:
                        parent_node.right = None
                        return
                elif current_node.left != None and current_node.right != None:
                    remove_node = current_node.right
                    remove_node_parent = current_node.right
                    while remove_node.left != None:
                        remove_node_parent = remove_node
                    current_node.value = remove_node.value
                    if remove_node == remove_node_parent:
                        current_node.right = remove_node.right
                        return
                    if remove_node.right == None:
                        remove_node_parent.left = None
                        return
                    else:
                        remove_node_parent.left = remove_node.right
                        return
        return False
        


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
tree.remove(20)
tree.print_tree()
print(tree.lookup(170))
print(tree.lookup(20))
