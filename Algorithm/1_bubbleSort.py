# in acsending order
list1 = [10, 15, 4, 23, 0]
print("unsorted List", list1)

for j in range(len(list1)-1):
    for i in range(len(list1)-1):
        # to compare the adjacent values
        if list1[i] > list1[i+1]:
            list1[i], list1[i+1] = list1[i+1], list1[i]

print("Sorted List", list1)

# in descending order
list1 = [10, 15, 4, 23, 0]
print("unsorted List", list1)

for j in range(len(list1)-1):
    for i in range(len(list1)-1):
        # to compare the adjacent values
        if list1[i] < list1[i+1]:
            list1[i], list1[i+1] = list1[i+1], list1[i]

print("Sorted List second:", list1)

# display all the steps
list1 = [10, 15, 4, 23, 0]
print("unsorted List", list1)

for j in range(len(list1)-1):
    for i in range(len(list1)-1-j):
        # to compare the adjacent values
        if list1[i] < list1[i+1]:
            list1[i], list1[i+1] = list1[i+1], list1[i]
            print(list1)
        else:
            print(list1)
    print()


print("Sorted List second:", list1)
