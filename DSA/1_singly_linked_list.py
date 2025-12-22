class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        pass

    # O(n) - linear runtime
    def __contains__(self, value):
        # point the last to the head and iterate it by shifting the last to the next until the last's next is not None
        # if the last's value is equal to the give value then return true, else false
        last = self.head
        while last.next is not None:
            if last.value == value:
                return True
            last = last.next
        return False

    # O(n) - linear time
    def __len__(self):
        # iterate through the LL by adding 1 to the counter at each step
        last = self.head
        counter = 0
        while last is not None:
            counter += 1
            last = last.next
        return counter
    
    # O(n) - linear time
    def append(self, value):
        # if head is none, that means there are no nodes in the LL, so we need to create a node and set the head to the new node.
        # if there are nodes, then i need to find the node that doesnt have a next node and create a new node and point that node to the new node.
        if self.head is None:
            self.head = Node(value)
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = Node(value)

    # O(1) - constant time
    def prepend(self, value):
        # create a new a node and point the new node's next to the node that has a head pointing to it already, and then point the head to the new node
        first_node = Node(value)
        first_node.next = self.head
        self.head = first_node

    # O(n) - linear time
    def insert(self, value, index):
        # if the index is 0 we can use the prepend function
        # if there is no head / or no nodes in the LL and an index is passed, we raise a value error
        # use last as the pointer to the head and iterate until the provided index
        # if the given index is after the last element of the LL (which is None), we raise a value error
        # if the index is within the LL then, we create the new node, point the new node to the last node's next value and point the next of the last node to the new node.
        if index == 0:
            self.prepend(value)
        else:
            if self.head is None:
                raise ValueError("Index out of bounds")
            else:
                last = self.head
                for i in range(index - 1): # because we want to find if the last element has a next value of None
                    if last.next is None:
                        raise ValueError("Index out of bounds")
                    last = last.next # keep iterating until the given index is the current node's previous / last node
                new_node = Node(value)
                new_node.next = last.next
                last.next = new_node

                    

        pass

    def delete(self, index):
        pass

    def pop(self, index):
        pass

    def get(self, index):
        pass

    
if __name__ == "__main__":
    pass

