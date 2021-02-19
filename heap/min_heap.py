import random
from heap import Heap


class minHeap(Heap):
    def __init__(self):
        super().__init__()

    def __len__(self):
        return len(self.Heap)

    def getTrueParent(self, parent_index):
        less_index = parent_index

        left_child_index = self.getLeftChild(parent_index)
        if self.isNode(left_child_index):  # does left child exist?
            if self.Heap[left_child_index] < self.Heap[less_index]:  # is left child less than parent?
                less_index = left_child_index

        right_child_index = self.getRightChild(parent_index)
        if self.isNode(right_child_index):  # does right child exist?
            if self.Heap[right_child_index] < self.Heap[
                less_index]:  # is left child less than parent and left child?
                less_index = right_child_index

        return less_index

    # runs in O(Log N)
    def Heapify(self, index):
        # is index a valid parent node?
        if not self.isNode(index):
            return
        if self.isLeaf(index):
            return

        true_parent_index = self.getTrueParent(index)
        if true_parent_index is not index:  # is parent greater than both children?
            self.swap(index, true_parent_index)  # swap parent with a child of lesser value (smallest child)
            self.Heapify(true_parent_index)  # Heapify the sub tree rooted at the new location of the previous root

    # runs in O(Log N)
    def insert(self, value):
        self.Heap.append(value)  # add value to end of Heap array
        index = self.lastIndex()
        while (self.getParent(index) is not None) & (
                self.Heap[index] < self.Heap[self.getParent(index)]):  # is new value less than its parent?
            self.swap(self.getParent(index), index)
            index = self.getParent(index)

    # runs in O(1)
    def getMin(self):
        return self.root()

    # runs in O(Log N)
    def extractMin(self):
        min = self.root()
        if (self.lastIndex() is not None) and (self.lastIndex() != self.rootIndex()):
            self.swap(self.rootIndex(), self.lastIndex())
            self.Heap.pop(self.lastIndex())
            self.Heapify(self.rootIndex())
        return min

