# There are two types of heap - Min heap & Max heap
# heap is in the form of a tree, 
# where min heap has its root node smaller than its children on both left and right sides
# where max heap has its root node larger than its children on both left and right sides

# consider our min heap is structured in an array like 
# [5, 20, 30, 25, 40, 50, 36, 32] -> nodes in the heap
# [0, 1,  2,  3,  4,  5,  6,  7] -> index of the heap nodes

# left child = 2 * index + 1
# right child = 2 * index + 2
# parent = (index - 1) // 2 , if index != 0

# time complexity - O(h) is always O(log n) because a heap is always balanced

class MinHeap:
    def __init__(self):
        self.heap = []

    def __len__(self):
        return len(self.heap)

    def __repr__(self):
        return str(self.heap)
    
    # O(log n)
    def insert(self, key, value):
        self.heap.append([key, value])
        self._sift_up(len(self.heap) - 1) # we sift up the index of the new element added to the heap, that needs its position to be sifted up to maintain the heap structure. This is the last element so (lenght - 1) is the proper index. 

    # O(1)
    def peek_min(self): # look at the min key, value
        if not self.heap: # if heap is empty
            raise IndexError('Empty heap')
        return self.heap[0] # because the min heap has the min element always on the top, ie the first element / index

    # O(log n)
    def extract_min(self): # remove the min key, value
        if not self.heap: # if heap is empty
            raise IndexError('Empty heap')
        min_element = self.heap[0]
        last_element = self.heap.pop() # because we want to remove the last element of the heap
        if self.heap: # if there are elements in the heap after poping
            self.heap[0] = last_element # we take the last element of the heap and put it in the first position
            self._sift_down(0) # when we place the last element in the first position of the heap the heap might not have a proper structure, so we need to move this element down by bring the other element forward.
        return min_element

    # O(n)
    def heapify(self, elements): # process of converting a list of elements into proper heap structure
        # we navigate from right to left (bottom to top) to sift down and maintain the heap properties
        self.heap = list(elements)
        for i in reversed(range(self._parent(len(self.heap) - 1) + 1)): # we want to move to the last element's parent's position for proper sift down comparisions 
            self._sift_down(i)

    # O(n)
    def meld(self, other_heap): # combine one heap with another
        combined_heap = self.heap + other_heap.heap
        self.heapify(combined_heap) # calling the above method to adjust both the heaps in correct heap structure
        other_heap = [] # in the end since the heaps are combined we adjust the other_heap back to empty list

    # helper methods

    # O(1)
    def _parent(self, index): # returns the parent of the index
        return (index - 1) // 2 if index != 0 else None # if index == 0, its the root / child node

    # O(1)
    def _left(self, index): # returns the left child of the index
        left = 2 * index + 1
        return left if left < len(self.heap) else None

    # O(1)
    def _right(self, index): # returns the right child of the index
        right = 2 * index + 2
        return right if right < len(self.heap) else None

    # O(log n)
    def _sift_up(self, index): # also called swim operation, this is used to move nodes up by comparing to its parent to maintain the heap structure when an new node is added, ie if the parent is larger than current index element then the current index element needs to move up.
        parent_index = self._parent(index) # get the parent's index of the current element
        while parent_index is not None and self.heap[index][0] < self.heap[parent_index][0]: # while Im not reaching the top of the heap and self.head[index][0] < self.heap[parent_index][0] is used because we are comparing the current element's key to the parent's key 
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index] # we replace the positions of the parent and current element
            index = parent_index # now the current index is at the parent's index because we swapped the positions
            parent_index = self._parent(index) # Now we fetch the new parent's index to the current index's position. we do this until the while condition is met.

    # O(log n)
    def _sift_down(self, index): # also called snik operation, this is used to move largest nodes or elements down to maintain the heap structure, usually done after we have swapped the new element to the top of the heap 
        while True:
            smallest = index # lets assume that the current element is the smallest
            left = self._left(index) # Now we want to compare to check if the left child is smaller than the current element. we get the left child element.
            right = self._right(index) # Now we want to compare to check if the right child is smaller than the current element. we get the right child element.
            if left is not None and self.heap[left][0] < self.heap[smallest][0]: # if the is a left child is present and if the left child's key is smaller than the current elements key, then we swap the positions.
                smallest = left # we swap the left child with the current element
            if right is not None and self.heap[right][0] < self.heap[smallest][0]: # if the is a right child is present and if the right child's key is smaller than the current elements key, then we swap the positions.
                smallest = right # we swap the right child with the current element
            if smallest == index: # this means the current element is already the smallest
                break
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index] # we swap the positions after determining if the largest and smallest elements
            index = smallest # we update the new index to be the smallest and repeat the process

if __name__ == "__main__":
    min_heap = MinHeap()
    min_heap.heapify([
        [10, '10'], [9, '9'], [8, '8'], [7, '7'], [6, '6'],
        [5, '5'], [4, '4'], [3, '3'], [2, '2'], [1, '1']
    ])
    print(min_heap)

    import heapq
    myList = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    heapq.heapify(myList)
    print(myList)

    print(min_heap.extract_min())
    print(min_heap.extract_min())
    print(min_heap.extract_min())

    print(heapq.heappop(myList))
    print(heapq.heappop(myList))
    print(heapq.heappop(myList))

    min_heap.insert(2, '2')
    print(min_heap)

    heapq.heappush(myList, 2)
    print(myList)

    min_heap2 = MinHeap()
    min_heap2.heapify([[5, '5'], [7, '7'], [2, '2']])
    min_heap.meld(min_heap2)
    print(min_heap)

