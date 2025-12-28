class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # O(n) - linear runtime
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
                return_str += f" -> {last.value}"
            return_str += " ]"
            return return_str

    # O(n) - linear runtime
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
                last.next = last.next.next

    # O(n) - Linear time 
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
    ll = LinkedList()

    ll.append(10)
    ll.append(5)
    ll.append(18)
    ll.append(22)
    ll.append(29)
    ll.prepend(100)

    ll.insert(200, 1)

    ll.delete(18)

    ll.pop(1)

    print(ll.get(1))
    print(29 in ll)
    print(800 in ll)
    print(29 in ll)
    print(ll)


