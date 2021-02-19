class Heap:
    def __init__(self):
        self.Heap = []

    def __len__(self):
        return len(self.Heap)

    def isNode(self, index):
        if index is None:
            return False
        if index < self.rootIndex():
            return False
        if index > self.lastIndex():
            return False
        return True

    def root(self):
        if len(self.Heap) > 0:
            return self.Heap[0]
        return None

    def rootIndex(self):
        if len(self.Heap) > 0:
            return 0
        return None

    def lastIndex(self):
        length = len(self.Heap)
        if length > 0:
            return length - 1
        return None

    def getParent(self, index):
        parentIndex = int((index - 1) / 2)
        if self.isNode(parentIndex):
            return parentIndex
        return None

    def getLeftChild(self, index):
        leftChildIndex = 2 * index + 1
        if self.isNode(leftChildIndex):
            return leftChildIndex
        return None

    def getRightChild(self, index):
        rightChildIndex = 2 * index + 2
        if self.isNode(rightChildIndex):
            return rightChildIndex
        return None

    def isLeaf(self, index):
        if not self.isNode(index):
            return False
        if self.isNode(self.getLeftChild(index)):
            return False
        return True

    def getTrueParent(self, parent_index):
        return parent_index

    def swap(self, parent_index, child_index):
        parent = self.Heap[parent_index]
        self.Heap[parent_index] = self.Heap[child_index]
        self.Heap[child_index] = parent

    def Heapify(self, index):
        return

    def insert(self, value):
        self.Heap.append(value)  # add value to end of Heap array
        
