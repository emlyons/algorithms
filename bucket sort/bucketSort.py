# runs in O(N) time
# all values must be unsigned and minValue <= maxValue
def bucketSort(toSort, minValue, maxValue):
    buckets = [0] * (maxValue + 1 - minValue)
    sorted = []

    # fill buckets - O(N)
    for i in range(0, len(toSort)):
        elem = toSort[i]
        elem_index = elem - minValue
        buckets[elem_index] = buckets[elem_index] + 1

    # read from buckets into sorted array - O(N)
    for elem_index in range(0, len(buckets)):
        for elem_count in range(0, buckets[elem_index]):
            elem = elem_index + minValue
            sorted.append(elem)

    return sorted
