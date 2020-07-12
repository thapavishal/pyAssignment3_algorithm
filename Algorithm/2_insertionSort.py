def insertionSort(list1):
    for index in range(1, len(list1)):
        current_item = list1[index]
        pos = index
        while current_item < list1[pos-1] and pos > 0:
            list1[pos] = list1[pos-1]
            pos = pos-1
            list1[pos] = current_item


list1 = [2, 3, 4, 5, 1]
insertionSort(list1)
print(list1)
