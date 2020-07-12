# quick sort
# choose one pivot point and compare all the values in the list with the pivot value
# take the pivot from the list and start compairing
# the smaller value are placed on the left side and greater are placed on the right of the pivot


def quick_sort(list1):
    length = len(list1)
    if length <= 1:
        return list1
    else:
        pivot = list1.pop()

    items_greater_thanpivot = []
    items_smaller_thanpivot = []

    for item in list1:
        if item > pivot:
            items_greater_thanpivot.append(item)

        else:
            items_smaller_thanpivot.append(item)

    return quick_sort(items_smaller_thanpivot) + [pivot] + quick_sort(items_greater_thanpivot)


print(quick_sort([2, 3, 44, 5, 78, 1, 99, 6]))
