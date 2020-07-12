def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result = left[i:]
    result = right[j:]
    return result


def mergesort(list1):
    if (len(list1) <= 1):
        return list1

    mid = int(len(list1)/2)
    left = mergesort(list1[:mid])
    right = mergesort(list1[mid:])

    return merge(left, right)


data = [1, 2, 3, 4, 5, 6, 8, 99, 21, 4, -1, 0]
print(mergesort(data))

"""
# method
def merge(leftlist, rightlist):
    leftlistIndex = 0
    rightlistIndex = 0

    leftlistLength = len(leftlist)
    rightlistLength = len(rightlist)

    originallength = leftlistLength + rightlistLength

    sorted_list = []

    for _ in range(0, len(originallength)):
        if leftlistIndex < leftlistLength and rightlistIndex < rightlistLength:

            if leftlist[leftlistIndex] <= rightlist[rightlistLength]:
                sorted_list.append(leftlist[leftlistIndex])
                leftlistIndex = leftlistIndex + 1

            else:
                sorted_list.append(rightlist[rightlistIndex])
                rightlistIndex = rightlistIndex + 1

    return sorted_list


def mergesort(list1):
    if len(list1) > 1:
        return list1
    else:
        mid = len(list1)/2

        leftlist = list1[:mid]
        rightlist = list1[mid:]

        return merge(leftlist, rightlist)
"""
