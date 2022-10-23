def LinearNRSearch(alist, i):
    found = False
    for j in range(len(alist)):
        if alist[j] == i:
            found = True
            break
    return print(f"Element {i} found at index {j}") if found else print(f"Element {i} not found")


def LinearRS(alist, k):
    if len(alist) == 0:
        return False
    else:
        return LinearRS(alist[1:], k) or alist[0] == k


array = []
print("Enter the number of elements in the array: ")
n = int(input())
print("Enter the elements of the array: ")
for i in range(n):
    print(f"Enter The {i + 1}th element: ")
    array.append(int(input()))

print("How do you want to search the array?")
print("1. Recursive Search")
print("2. Non Recursive Search")
choice = int(input())
if choice == 1:
    print("Enter the element to be searched: ")
    item = int(input())
    print(f"Element found @ index {LinearRS(array, item)}")

elif choice == 2:
    print("Enter the element to be searched: ")
    item = int(input())
    LinearNRSearch(array, item)

else:
    print("Invalid Choice")
