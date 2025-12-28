# Last In First Out Principle (LIFO)
# The element added the last to the stack will be the first one to be processed or removed
# push - adding a element to the top of the stack
# pop - taking out the top element from the stack for processing
# peek - taking a look at the top element without any processing

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None # The element below the top element

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    # O(1) - constant time
    def __len__(self):
        return self.size

    # O(n) - linear time
    def __repr__(self):
        items = []
        current_item = self.top
        while current_item is not None:
            items.append(str(current_item.value)) # append the first element
            current_item = current_item.next # move current pointer to the next element until we reach the last
        return ','.join(items)

    # O(1) - constant time
    def push(self, value):
        new_node = Node(value) # create a new element
        new_node.next = self.top # If there is already an element in the stack then point it to the newly created node as its next element
        self.top = new_node # Then point the top to the new node
        self.size += 1 # keeping track of the size of the stack

    # O(1) - constant time
    def pop(self):
        if self.top is None: # if the stack is empty
            raise ValueError("Stack is empty")
        pop_value = self.top.value # the element to be returned
        self.top = self.top.next # we set the current top to the next element of the top element
        self.size -= 1 # decrease the size as we are removing 1 element
        return pop_value # return the removed value to display

    # O(1) - constant time
    def peek(self):
        if self.top is None: # if the stack is empty
            raise ValueError("Stack is empty")
        return self.top.value # return the top element

    # O(1) - constant time
    def is_empty(self):
        return self.top is None


if __name__ == "__main__":
    stack = Stack()

    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)
    stack.push(50)
    stack.push(60)
    stack.push(70)

    print(stack.pop())

    stack.push(1000)

    print(stack.peek())

    print(stack)

    print(stack.is_empty())


