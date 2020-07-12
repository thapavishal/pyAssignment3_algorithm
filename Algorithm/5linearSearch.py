def search(list1, key):
    for i in range(len(list1)):
        if key == list1[i]:
            print("Key element is found at index:", i)
            break

    else:
        print("element is not found")


list1 = [12, 34, 2, 3, 7, 1, 9, 7]
print("The given list is: ", list1)
key = int(input("enter the element you want to search from the list: "))
search(list1, key)
