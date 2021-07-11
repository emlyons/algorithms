


if __name__ == '__main__':
    from random import randint
    import avl

    maxSize = 100

    testTree = avl.AVLTree()



    elements = []
    insertOrder = []
    for i in range(maxSize):
        elements.append(i)

    while len(elements) > 0:
        index = randint(0, len(elements) - 1)
        toAdd = elements[index]
        testTree.insert(toAdd)
        insertOrder.append(toAdd)
        elements.remove(toAdd)

    (success, orderedWalk, avlStatus) = testTree.testInvariants()


    rangeList = testTree.list(2,90)
    count = testTree.count(2,90)

    if (count != len(rangeList)):
        count = testTree.count(2, 90)

    while len(orderedWalk) > 0 and success:
        index = randint(0, len(orderedWalk) - 1)
        toAdd = orderedWalk[index]
        node = testTree.search(toAdd)
        testTree.delete(node)
        orderedWalk.remove(toAdd)
        (success, orderedWalk_too, avlStatus) = testTree.testInvariants()

    if not success:
        (success, orderedWalk_too, avlStatus) = testTree.testInvariants()


    print("tests passed!")





