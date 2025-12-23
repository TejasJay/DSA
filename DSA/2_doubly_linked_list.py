class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # O(n) - linear runtime
    # This is same as singly linked list
    def __repr__(self):
        # there the LL is empty then return an empty list
        # if there are elements then first set the last to point the head
        # now until the last's next is not 0 we iterate bu moving the last reference to its next node
        # concat all the nodes's values to dusplay
        if self.head is None:
            return "[]"
        else:
            last = self.head
            return_str = f"[ {last.value}"
            while last.next:
                last = last.next
                return_str += f" <-> {last.value}"
            return_str += " ]"
            return return_str

    # O(n) - linear runtime
    # This is same as singly linked list
    def __contains__(self, value):
        # point the curr to the head and iterate it by shifting the curr to the next until the last's next is not None
        # if the curr's value is equal to the give value then return true, else false
        curr = self.head
        while curr is not None:
            if curr.value == value:
                return True
            curr = curr.next
        return False

    # O(n) - linear time
    # This is same as singly linked list
    def __len__(self):
        # iterate through the LL by adding 1 to the counter at each step
        last = self.head
        counter = 0
        while last is not None:
            counter += 1
            last = last.next
        return counter
    
    # O(1) - Constant time
    def append(self, value):
        # if head is none, that means there are no nodes in the LL, so we need to create a node and set the head to the new node.
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head # both head and tail points to the same node
        else:
            # crete a new node, 
            # point it to the last node
            # point the last's next to the new node, instead of None
            # point the tail to the new node
            last_node = Node(value)
            last_node.previous = self.tail
            self.tail.next = last_node
            self.tail = last_node
            

    # O(1) - constant time
    def prepend(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            # crete a new node, 
            # point it's next to the first node
            # point the first's prev to the new node
            # point the head to the new node
            first_node = Node(value)
            first_node.next = self.head
            self.head.previous = first_node
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
                new_node.next = last.next # point the new node's next to the last's next
                new_node.previous = last # we make this change to also point the new node's previous node
                if last.next is not None:
                    last.next.previous = new_node # we cut the connection to point the last's node to the new node
                last.next = new_node

    # O(n) - linear time            
    def delete(self, value):
        # if we try to delete a value from the LL that isnt present we dont do anything
        # if the value is the current head then we assign the head to the last's next
        # if value is somewhere in between, we look ahead if current's next / last's next's next value = given value, if yes then we point the last's next to it.
        last = self.head
        if last is not None:
            if last.value == value:
                self.head = last.next
            else:
                while last.next:
                    if last.next.value == value:
                        if last.next.next is not None:
                            last.next.next.previous = last
                        last.next = last.next.next
                        break
                    last = last.next

    # O(n) - Linear time             
    def pop(self, index):
        # if there is no head / or no nodes in the LL and an index is passed, we raise a value error
        # if the given index is after the last element of the LL (which is None), we raise a value error
        if self.head is None:
            raise ValueError("Index out of bounds")
        else:
            last = self.head
            for i in range(index - 1):
                if last.next is None:
                    raise ValueError("Index out of bounds")
                last = last.next
            if last.next is None:
                raise ValueError("Index out of bounds")
            else:
                if last.next.next is not None:
                    last.next.next.previous = last
                last.next = last.next.next

    # O(n) - Linear time
    # This is same as singly linked list 
    def get(self, index):
        # same principles as the others but this time we return the value when we reach the index
        if self.head is None:
            raise ValueError("Index out of bounds")
        else:
            last = self.head
            for i in range(index):
                if last.next is None:
                    raise ValueError("Index out of bounds")
                last = last.next
            return last.value

    
if __name__ == "__main__":
    ll = DoublyLinkedList()

    ll.append(10)
    ll.append(5)
    ll.append(18)
    ll.append(22)
    ll.append(29)

    ll.prepend(100)

    ll.insert(200, 1)
    ll.insert(50, 1)
    ll.insert(2, 1)
    ll.insert(2000, 1)
    ll.insert(300, 1)

    ll.delete(18)

    ll.pop(1)

    print(ll.get(1))
    print(29 in ll)
    print(800 in ll)
    print(29 in ll)
    print(2000 in ll)

    print(ll)


