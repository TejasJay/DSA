# O(log n) or O(log h) -> if the tree is designed well as a balanced binary tree (h is the height of the tree) 
# O(n) -> if the tree is designed poorly (might turn into a linked list)

class Node:
    def __init__(self, key):
        self.left = None # left child node of the root node
        self.right = None # right child node of the root node
        self.parent = None # refrence to the parent
        self.key = key # the key of the node
        self.value = None # each node can have a value like (key : value)

    def __repr__(self): # to print the node
        return f"({self.key}, {self.value})"


class BinarySearchTree:
    def __init__(self):
        self.root = None # the root node of the full tree

    def __contains__(self, key): # to check if it exists
        current_node = self.root # start from the root
        while current_node is not None: # if it doesnt reach the end
            if key < current_node.key:
                current_node = current_node.left # we need to go to the left
            elif key > current_node.key:
                current_node = current_node.right # we need to go to the right
            else: # key == current node
                return True 
        return False

    # O(n) - because we need to iterate over all the elements / nodes
    def __iter__(self): # this is a dunder method to iterate over the tree
        yield from self._in_order_traversal(self.root)

    # O(n) - because we need to iterate over all the elements / nodes
    def __repr__(self): # to print the tree
        return str(list(self._in_order_traversal(self.root)))

    def insert(self, key, value):
        if self.root is None: # if the tree is empty
            self.root = Node(key)
            self.root.value = value
        else: # if the tree isnt empty
            current_node = self.root
            while True:
                if key < current_node.key: # if key is less we check left
                    if current_node.left is None: # if the left node is empty we create it
                        current_node.left = Node(key)
                        current_node.left.value = value
                        current_node.left.parent = current_node
                        break
                    else: # if it isnt empty and key is still < current_node, we continue moving left
                        current_node = current_node.left
                elif key > current_node.key: # if key is greater we check right
                    if current_node.right is None: # if the right node is empty we create it
                        current_node.right = Node(key)
                        current_node.right.value = value
                        current_node.right.parent = current_node
                        break
                    else: # if it isnt empty and key is still > current_node, we continue moving right
                        current_node = current_node.right
                else: # the current node is already the key we are looking for, so we update the value
                    current_node.value = value
                    break

        
    def search(self, key): # to retreive the full Node
        current_node = self.root # we start the search from the root
        while True:
            if current_node is None or current_node.key == key: # returns the node when it is found, else returns None
                return current_node
            elif key < current_node.key: # check if the key is smaller than the current node and traverse left until we find it, if we don't then return None
                if current_node.left is None:
                    return None
                else:
                    current_node = current_node.left
            else: # check if the key is larger than the current node and traverse right until we find it, if we don't then return None
                if current_node.right is None:
                    return None
                else:
                    current_node = current_node.right

    def delete(self, key):
        node = self.search(key)
        if node is None:
            raise KeyError('Node with this key doesnt exist')
        self._delete(node)

    def traverse(self, order): # to traverse the tree using different order types
        if order == 'inorder':
            yield from self._in_order_traversal(self.root)
        elif order == 'preorder':
            yield from self._pre_order_traversal(self.root)
        elif order == 'postorder':
            yield from self._post_order_traversal(self.root)
        else:
            raise ValueError('Unknown order')

    # Below are the helper private functions required by the main functions

    def _delete(self, node): # used by delete to search and find the Node to delete
        # Node is a leaf node
        if node.left is None and node.right is None:
            if node.parent is None: # if we want to delete the root node itself
                self.root = None
            else: # we need to check if we need to delete the right or left node from the parent node persepective
                if node.parent.right == node:
                    node.parent.right = None
                else:
                    node.parent.left = None
                node.parent = None # we do this to remove the reference of the deleted node to its parent
        # Node has one child node
        elif node.left is None or node.right is None:
            child_node = node.left if node.left is not None else node.right # to find is the single child is a left or right node
            if node.parent is None: # check if the node we want to delete is the root node
                child_node.parent = None # because the root node has no parent (child node is now the root node)
                self.root = child_node # since we deleted the root node we need to make its child as the root node
            else: # if the node we want to delete is not the root,
                if node.parent.right == node: # 
                    node.parent.right = child_node
                else:
                    node.parent.left = child_node
                child_node.parent = node.parent
            node.parent = node.left = node.right = None
        # Node has two child nodes
        else:
            successor = self._successor(node) # we replace the node with the successor node's key and value
            node.key = successor.key
            node.value = successor.value
            self._delete(successor) # because we replace the node with the successor node we need to delete the successor, else there will be 2 nodes with the same key and value

    def _successor(self, node): # The smallest child key of all the children present for a parent, but still larger than the parent key itself.
        if node is None:
            raise ValueError('Cannot find successor of None')
        if node.right is None: # There is no successor
            return None 
        else: # To find the successor we check right and move there and we traverse all the way down the left to get the last node element (easier to visualize with a diagram)
            current_node = node.right
            while node.left is not None:
                current_node = current_node.left
            return current_node
            

    def _predecessor(self, node): # The largest child key of all the children present for a parent, but still lesser than the parent key itself.
        if node is None:
            raise ValueError('Cannot find predecessor of None')
        if node.left is None: # There is no predecessor
            return None 
        else: # To find the predecessor we check left and move there and we traverse all the way down the right to get the last node element (easier to visualize with a diagram)
            current_node = node.left
            while node.right is not None:
                current_node = current_node.right
            return current_node

    def _in_order_traversal(self, node): # used by traverse as its parameter value, (left -> root -> right) this should print the node keys in ascending order
        if node is not None:
            yield from self._in_order_traversal(node.left) # recursive call to yield the left subtree
            yield (node.key, node.value) # yield the root node
            yield from self._in_order_traversal(node.right) # recursive call to yield the right subtree


    def _pre_order_traversal(self, node): # used by traverse as its parameter value, (root -> left -> right)
        if node is not None:
            yield (node.key, node.value) # yield the root node
            yield from self._pre_order_traversal(node.left) # recursive call to yield the left subtree
            yield from self._pre_order_traversal(node.right) # recursive call to yield the right subtree

    def _post_order_traversal(self, node): # used by traverse as its parameter value, (left -> right -> root)
        if node is not None:
            yield from self._post_order_traversal(node.left) # recursive call to yield the left subtree
            yield from self._post_order_traversal(node.right) # recursive call to yield the right subtree
            yield (node.key, node.value) # yield the root node
            

if __name__ == "__main__":
    bst = BinarySearchTree()

    bst.insert(10, 'hello')
    bst.insert(5, 'hello')
    bst.insert(22, 'hello')
    bst.insert(2, 'hello')
    bst.insert(9, 'hello')
    bst.insert(12, 'hello')
    bst.insert(30, 'hello')
    bst.insert(11, 'hello')
    bst.insert(15, 'hello')
    bst.insert(30, 'hello')
    bst.insert(23, 'hello')
    bst.insert(35, 'hello')

    bst.delete(9)

    for i in bst.traverse('preorder'):
        print(i)

    print(bst)

    print(bst.search(30))