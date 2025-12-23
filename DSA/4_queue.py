# First In First Out (FIFO)
# enqueue - adding an element at the last or rear end of the queue
# dequeue - taking out the element from the front of the queue
# peek - looking at the element that is about to leave the queue


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None # first element of the Queue
        self.rear = None # last element of the Queue
        self.size = 0 # To keep track of the size of the Queue

    # O(1) - constant time
    def __len__(self):
        return self.size

    # O(n) - linear time
    def __repr__(self):
        items = []
        current_item = self.front
        while current_item is not None:
            items.append(str(current_item.value))
            current_item = current_item.next
        return ','.join(items)

    # O(1) - constant time
    def enqueue(self, value):
        new_node = Node(value)
        if self.rear is None: # if the queue is empty then both the front and rear will point to the new node
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node # the next element of the rear element is the new node
            self.rear = new_node # now we point the rear to the new node
        self.size += 1 

    # O(1) - constant time
    def dequeue(self):
        if self.front is None: # check if the Queue is already empty
            raise IndexError("Queue is empty")
        dequeue_value = self.front.value # the value to be dequeued or removed
        self.front = self.front.next # move to front pointer to the next element
        if self.front is None: # if there was only one element in the Queue after moving, then the front would point to None
            self.rear = None # we need to adjust so that the rear would also point to None, else it would be pointing to the previous element
        self.size += 1
        return dequeue_value

    # O(1) - constant time
    def peek(self):
        if self.front is None: # check if the Queue is already empty
            raise IndexError("Queue is empty")
        return self.front.value

    # O(1) - constant time
    def is_empty(self):
        return self.front is None # if front is None it returns True, else False



if __name__ == "__main__":
    queue = Queue()

    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.enqueue(40)
    queue.enqueue(50)
    queue.enqueue(60)
    queue.enqueue(70)
    queue.enqueue(80)

    print(queue)

    queue.dequeue()
    queue.dequeue()

    print(queue)

    print(queue.is_empty())

    print(queue.peek())

    print(queue)

    print(len(queue))

    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()

    print(len(queue))
    print(queue)




