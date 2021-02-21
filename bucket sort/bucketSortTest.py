import random
from bucketSort import bucketSort

def TEST_randomListAndSortedList(length, minValue, maxValue):
    unsorted = []
    sorted = []

    for i in range(0, length):
        unsorted.append(random.randint(minValue, maxValue))
    sorted = bucketSort(unsorted, minValue, maxValue)

    return (unsorted, sorted)

def TEST_elemCount():
    for listLength in range(1, 100):
        splitValue = random.randint(25, 75)
        for minValue in range(0, random.randint(0, splitValue)):
            for maxValue in range(random.randint(splitValue, 100), 100):

                (listA, listB) = TEST_randomListAndSortedList(listLength, minValue, maxValue)

                if len(listA) is not len(listB):
                    return False
                maxA = max(listA)
                maxB = max(listB)

                if maxA is not maxB:
                    return False

                countA = [0] * (maxA + 1)
                for i in range(0, len(listA)):
                    elem = listA[i]
                    countA[elem] += 1

                countB = [0] * (maxB + 1)
                for i in range(0, len(listB)):
                    elem = listB[i]
                    countB[elem] += 1

                for i in range(0, len(countA)):
                    if countA[i] is not countB[i]:
                        return False

        return True

def TEST_randomSorting():
    for listLength in range(1, 100):
        splitValue = random.randint(25, 75)
        for minValue in range(0, random.randint(0, splitValue)):
            for maxValue in range(random.randint(splitValue + 1, 100), 100):

                (unsorted, sorted) = TEST_randomListAndSortedList(listLength, minValue, maxValue)

                for i in range(1, listLength):
                    if sorted[i - 1] > sorted[i]:
                        return False

    return True

def TEST_edgeCases():
    listLength = 1
    (unsorted, sorted) = TEST_randomListAndSortedList(listLength, 1, 100)
    if len(unsorted) is not len(sorted):
        return False
    if len(sorted) is not listLength:
        return False
    for i in range(1, listLength):
        if sorted[i - 1] > sorted[i]:
            return False

    listLength = 0
    (unsorted, sorted) = TEST_randomListAndSortedList(listLength, 1, 100)
    if len(unsorted) is not len(sorted):
        return False
    if len(sorted) is not listLength:
        return False
    for i in range(1, listLength):
        if sorted[i - 1] > sorted[i]:
            return False

    listLength = 100
    (unsorted, sorted) = TEST_randomListAndSortedList(listLength, 1, 1)
    if len(unsorted) is not len(sorted):
        return False
    if len(sorted) is not listLength:
        return False
    for i in range(1, listLength):
        if sorted[i - 1] > sorted[i]:
            return False

    listLength = 100
    (unsorted, sorted) = TEST_randomListAndSortedList(listLength, 0, 0)
    if len(unsorted) is not len(sorted):
        return False
    if len(sorted) is not listLength:
        return False
    for i in range(1, listLength):
        if sorted[i - 1] > sorted[i]:
            return False

    listLength = 0
    (unsorted, sorted) = TEST_randomListAndSortedList(listLength, 0, 0)
    if len(unsorted) is not len(sorted):
        return False
    if len(sorted) is not listLength:
        return False
    for i in range(1, listLength):
        if sorted[i - 1] > sorted[i]:
            return False

    listLength = 1
    (unsorted, sorted) = TEST_randomListAndSortedList(listLength, 0, 0)
    if len(unsorted) is not len(sorted):
        return False
    if len(sorted) is not listLength:
        return False
    for i in range(1, listLength):
        if sorted[i - 1] > sorted[i]:
            return False

    return True


if __name__ == '__main__':
    success = True

    if not TEST_randomSorting():
        success = False
        print("random sorting test failed")

    if not TEST_elemCount():
        success = False
        print("sorted and unsorted had different elements")

    if not TEST_edgeCases():
        success = False
        print("edge case tests failed")


    if success:
        print("all tests passed")
