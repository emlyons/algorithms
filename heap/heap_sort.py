from max_heap import maxHeap
from min_heap import minHeap

# runs in O(N log N)
def max_sort(array):
    max_heap = maxHeap()
    sorted_array = []
    size = len(array)
    for i in range(0, size):
        max_heap.insert(array[i])
    for i in range(0, size):
        sorted_array.append(max_heap.extractMax())
    return sorted_array

# runs in O(N log N)
def min_sort(array):
    min_heap = minHeap()
    sorted_array = []
    size = len(array)
    for i in range(0, size):
        min_heap.insert(array[i])
    for i in range(0, size):
        sorted_array.append(min_heap.extractMin())
    return sorted_array
