import random
from heap import Heap
from max_heap import maxHeap
from min_heap import minHeap
from heap_sort import *

def populateHeap(heap, size):
    buffer = []
    for i in range(1, size + 1):
        buffer.append(i)

    for i in range(0, size):
        random_index = random.randint(0, len(buffer) - 1)
        heap.insert(buffer[random_index])
        buffer.pop(random_index)
    return heap

def verifyHeapInvariant(heap):
    for index in range(0, len(heap)):
        if index is not heap.getTrueParent(index):
            return False
    return True

def verifyExtractMax(max_heap):
    last_max = max_heap.getMax()
    for i in range(0, len(max_heap)):
        max = max_heap.extractMax()
        if max > last_max:
            return False
        last_max = max
    return True

def verifyExtractMin(min_heap):
    last_min = min_heap.getMin()
    for i in range(0, len(min_heap)):
        min = min_heap.extractMin()
        if min < last_min:
            return False
        last_min = min
    return True

def minSortRandomArray(size):
    random_array = []
    for i in range(0, size):
        random_array.append(random.randint(0, 100))
    sorted_array = min_sort(random_array)
    for i in range(1, size):
        if sorted_array[i - 1] > sorted_array[i]:
            return False
    return True

def maxSortRandomArray(size):
    random_array = []
    for i in range(0, size):
        random_array.append(random.randint(0, 100))
    sorted_array = max_sort(random_array)
    for i in range(1, size):
        if sorted_array[i - 1] < sorted_array[i]:
            return False
    return True




if __name__ == '__main__':
    status = True

    max_heap = maxHeap()
    populateHeap(max_heap, 1000)

    if not verifyHeapInvariant(max_heap):
        status = False
        print("Error: max heap invariant was violated")

    if not verifyExtractMax(max_heap):
        status = False
        print("Error: extract max failed to return max")

    min_heap = minHeap()
    populateHeap(min_heap, 1000)

    if not verifyHeapInvariant(min_heap):
        status = False
        print("Error: min heap invariant was violated")

    if not verifyExtractMin(min_heap):
        status = False
        print("Error: extract min failed to return min")

    if not minSortRandomArray(100):
        status = False
        print("Error: min heap sort has failed")

    if not maxSortRandomArray(100):
        status = False
        print("Error: max heap sort has failed")

    if status:
        print("all tests passed")
        
