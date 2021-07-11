# binary tree
class AVLTree:
    def __init__(self):
        """ tree fields """
        self.root = None




    # insert element into BST structure
    # runs in O(log n) time
    def insert(self, key):
        newNode = avlNode(key)

        if self.root == None:                               # empty tree
            self.root = newNode
        else:
            run = True
            searchNode = self.root

            while run:
                if newNode.key <= searchNode.key:           # go left
                    if searchNode.left == None:             # insert node
                        searchNode.left = newNode
                        newNode.parent = searchNode
                        self.rebalance(searchNode)
                        run = False
                    else:
                        searchNode = searchNode.left        # search left

                elif newNode.key > searchNode.key:          # go right
                    if searchNode.right == None:            # insert node
                        searchNode.right = newNode
                        newNode.parent = searchNode
                        self.rebalance(searchNode)
                        run = False
                    else:
                        searchNode = searchNode.right       # search right



    # delete node from avl
    # runs in O(log n) time
    def delete(self, node):
        parent = node.parent

        if node.left != None and node.right != None:                        # node has left and right child
            successorNode = self.successor(node)
            self.delete(successorNode)
            self.replaceWithNode(node, successorNode)
            self.rebalance(successorNode)

        elif node.left != None:                                             # node has only left child
            left = node.left
            self.replaceWithNode(node, left)
            self.rebalance(left.parent)

        elif node.right != None:                                            # node has only right child
            right = node.right
            self.replaceWithNode(node, right)
            self.rebalance(right.parent)

        else:                                                               # node has no child
            self.replaceWithNone(node)
            self.rebalance(parent)




    # search avl tree and return first node with matching key
    # runs in O(log n) time
    def search(self, key):
        if self.root == None:                                   # empty tree
            return None
        else:
            searchNode = self.root
            while True:
                if key == searchNode.key:                       # key matched
                    return searchNode

                elif key < searchNode.key:                      # go left
                    if searchNode.left == None:                 # key not found
                        return None
                    else:
                        searchNode = searchNode.left            # search left

                elif key > searchNode.key:                      # go right
                    if searchNode.right == None:                # key not found
                        return None
                    else:
                        searchNode = searchNode.right           # search right



    # rebalance
    # traverses the AVL tree upward from requested node until reaching the parent
    # maintains the AVL invariant
    # runs in O(log n) time
    def rebalance(self, node):

        while node != None:

            self.updateAugmentedFields(node)

            # right heavy
            if not node.left and node.right:
                if node.right.height > 0:
                    if node.right.left and not node.right.right:
                        self.caseDoubleRotate(node, node.right, node.right.left, True)
                    elif node.right.left and node.right.right:
                        if node.right.left.height > node.right.right.height:
                            self.caseDoubleRotate(node, node.right, node.right.left, True)
                    node = self.caseSingleRotate(node, node.right, True)

            # left heavy
            elif not node.right and node.left:
                if node.left.height > 0:
                    if node.left.right and not node.left.left:
                        self.caseDoubleRotate(node, node.left, node.left.right, False)
                    elif node.left.right and node.left.left:
                        if node.left.right.height > node.left.left.height:
                            self.caseDoubleRotate(node, node.left, node.left.right, False)
                    node = self.caseSingleRotate(node, node.left, False)

            elif node.right and node.left:
                # right heavy
                if node.right.height > node.left.height + 1:
                    if node.right.left and not node.right.right:
                        self.caseDoubleRotate(node, node.right, node.right.left, True)
                    elif node.right.left and node.right.right:
                        if node.right.left.height > node.right.right.height:
                            self.caseDoubleRotate(node, node.right, node.right.left, True)
                    node = self.caseSingleRotate(node, node.right, True)

                # left heavy
                elif node.left.height > node.right.height + 1:
                    if node.left.right and not node.left.left:
                        self.caseDoubleRotate(node, node.left, node.left.right, False)
                    elif node.left.right and node.left.left:
                        if node.left.right.height > node.left.left.height:
                            self.caseDoubleRotate(node, node.left, node.left.right, False)
                    node = self.caseSingleRotate(node, node.left, False)

            node = node.parent


    # performs the first rotation of a two rotation balance case and maintains augmented fields of nodes involved
    # assumes A is parent of B
    # C is left child of B for right rotation
    # C is right child of B for left rotation
    # direction: (True = left) (False = right)
    # runs in O(1) time
    def caseDoubleRotate(self, A, B, C, direction):
        if direction is True:
            self.rotateRight(C)
            self.updateAugmentedFields(B)
            self.updateAugmentedFields(C)
            self.updateAugmentedFields(A)
        else:
            self.rotateLeft(C)
            self.updateAugmentedFields(B)
            self.updateAugmentedFields(C)
            self.updateAugmentedFields(A)



    # performs a single rotation and maintains augments fields of nodes involved
    # assumes A is parent of B
    # direction: (True = left) (False = right)
    # runs in O(1) time
    def caseSingleRotate(self, A, B, direction):
        if direction is True:
            self.rotateLeft(B)
            self.updateAugmentedFields(A)
            self.updateAugmentedFields(B)
            return B
        else:
            self.rotateRight(B)
            self.updateAugmentedFields(A)
            self.updateAugmentedFields(B)
            return B


    # updates all the augmented fields associated with node
    # assumes all augments fields are only dependent on sub trees of node
    # runs in O(1) time
    def updateAugmentedFields(self, node):
        self.updateHeight(node)
        self.updateSubTreeSize(node)


    # updates the subTreeHeight field of the requested node
    # depends only on sub trees of node
    # runs in O(1) time
    def updateSubTreeSize(self, node):
        node.subTreeSize = 1
        if node.left != None:
            node.subTreeSize += node.left.subTreeSize
        if node.right != None:
            node.subTreeSize += node.right.subTreeSize


    # updates the height field for a given node
    # depends only on sub trees of node
    # runs in O(1) time
    def updateHeight(self, node):
        node.height = 0
        if node.left != None:
            node.height = 1 + node.left.height
        if node.right != None:
            node.height = max(node.height, 1 + node.right.height)



    # rotate left
    # assumes B is the left child of node A
    # runs in O(1) time
    def rotateLeft(self, B):
        A = B.parent

        B.parent = A.parent  # point B parent to A.parent
        if A.parent != None:
            if B.parent.left == A:      # point A.parent to B
                B.parent.left = B
            else:
                B.parent.right = B
        else:
            self.root = B

        A.right = B.left            # point A right to B.left
        if A.right != None:
            A.right.parent = A      # point B left.parent to A

        B.left = A                      # point B left to A
        A.parent = B                    # point A parent to B




    # rotate right
    # assumes B is the right child of node A
    # runs in O(1) time
    def rotateRight(self, B):
        A = B.parent

        B.parent = A.parent
        if A.parent != None:
            if B.parent.left == A:
                B.parent.left = B
            else:
                B.parent.right = B
        else:
            self.root = B

        A.left = B.right
        if A.left != None:
            A.left.parent = A

        B.right = A
        A.parent = B




    # replaces a node with another
    # removes all connections with the replaced node to the tree
    # assumes in_node has no connected nodes at call
    # runs in O(1) time
    def replaceWithNode(self, out_node, in_node):

        # connect replacement node to parent
        if not out_node.parent:                                     # root node is being replaced
            in_node.parent = None
            self.root = in_node

        elif out_node.parent.left == out_node:                      # left child to parent
            out_node.parent.left = in_node
            in_node.parent = out_node.parent

        else:                                                       # right child to parent
            out_node.parent.right = in_node
            in_node.parent = out_node.parent

        # connect replacement node to children
        if out_node.left and out_node.left != in_node:      # left children
            in_node.left = out_node.left
            in_node.left.parent = in_node

        if out_node.right and out_node.right != in_node:    # right children
            in_node.right = out_node.right
            in_node.right.parent = in_node

        # disconnect replaced node
        out_node.parent = None
        out_node.left = None
        out_node.right = None



    # replace a node in bst with a None type
    # WARNING: any children of the node will be lost
    # runs in O(1) time
    def replaceWithNone(self, node):
        if node.parent == None:                                 # root node is being replaced
            self.root = None

        elif node.parent.left == node:                          # left child to parent
            node.parent.left = None

        else:                                                   # right child to parent
            node.parent.right = None

        # disconnect replaced node
        node.parent = None
        node.left = None
        node.right = None



    # find and return successor of node
    # runs in O(log n)
    def successor(self, node):
        if node.right == None:
            # only using child successors in this implementation
            #while node.parent != None:
            #    if node.parent.right == node:
            #        return node.parent
            #else:
            #    node = node.parent
            return None
        else:
            return self.min(node.right)


    # find and return the minimum node in the tree
    # runs in O(log n) time
    def min(self, node):
        while node.left != None:
            node = node.left
        return node


    # find and return the maximum node in the tree
    # runs in O(log n) time
    def max(self, node):
        while node.right != None:
            node = node.right
        return node


    # returns the number of values in the avl tree within the requested range (inclusive)
    # runs in O(log n)
    def count(self, l, h):
        lca = self.lca(l, h)
        lowRank, foundLow = self.countTraverseLeft(lca, l, 0)
        highRank, foundHigh = self.countTraverseLeft(lca, h, 0)
        return highRank - lowRank + foundLow


    # counts the number of elements the avl that are less than or equal to the bound
    # runs in O(log n)
    def countTraverseLeft(self, node, bound, count):
        found = 0
        while bound < node.key:
            if not node.left:
                return (count, found)
            node = node.left
        count += 1

        if node.left:
            count += node.left.subTreeSize
        if node.key == bound:
            found = 1
            return (count, found)

        if node.right:
            (count, found) = self.countTraverseRight(node.right, bound, count)
        return (count, found)


    # counts the number of elements in the avl tree that are greater than or equal to the bound
    # runs in O(log n)
    def countTraverseRight(self, node, bound, count):
        found = 0
        while bound >= node.key:
            count += 1
            if node.left:
                count += node.left.subTreeSize
            if bound == node.key:
                found = 1
                return (count, found)
            if not node.right:
                return (count, found)
            node = node.right

        if node.left:
            (count, found) = self.countTraverseLeft(node.left, bound, count)
        return (count, found)




    # returns a list containing all nodes in the avl tree within the requested range
    # runs in O(n) time
    def list(self, l, h):
        lca = self.lca(l, h)
        result = []
        self.nodeList(lca, l, h, result)
        return result


    # generates the list
    # runs in O(n) time
    def nodeList(self, node, l, h, result):
        if node:
            if l <= node.key and node.key <= h:
                result.append(node.key)
            if node.key >= l:
                self.nodeList(node.left, l, h, result)
            if node.key <= h:
                self.nodeList(node.right, l, h, result)


    # returns the lowest common ancestor of the requested range
    # runs in O(log n) time
    def lca(self, l, h):
        node = self.root
        while node and not (l <= node.key and h >= node.key):
            if l < node.key:
                node = node.left
            else:
                node = node.right
        return node





    def isNodeAVL(self, node):
        if node.left and node.right:
            if abs(node.left.height - node.right.height) > 1:
                return False

        elif node.left and not node.right:
            if node.left.height > 0:
                return False

        elif not node.left and node.right:
            if node.right.height > 0:
                return False

        else:
            if node.height != 0:
                return False

        return True



    # test method for checking the BST invariant and AVL invariant
    def testInvariants(self):
        orderedWalk = []
        avlStatus = []
        flag = True
        orderedWalk, avlStatus = self.inOrderTraversal(self.root, orderedWalk, avlStatus)
        for i in range(len(orderedWalk) - 1):
            if orderedWalk[i] > orderedWalk[i+1]:
                flag = False
        if avlStatus.__contains__(0):
            flag = False
        return (flag, orderedWalk, avlStatus)




    # returns a list containing a topological walk of the bst
    # runs in O(n) time
    def inOrderTraversal(self, node, list, avlStatus):
        if node:
            if node.left != None:
                list, avlStatus = self.inOrderTraversal(node.left, list, avlStatus)

            list.append(node.key)

            if self.isNodeAVL(node):
                avlStatus.append(1)
            else:
                avlStatus.append(0)

            if node.right != None:
                list, avlStatus = self.inOrderTraversal(node.right, list, avlStatus)

        return (list, avlStatus)







class avlNode:
    def __init__(self, key):
        self.key = key
        self.height = 0
        self.subTreeSize = 1
        self.parent = None
        self.left = None
        self.right = None