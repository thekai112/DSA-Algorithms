def bubbleSort(Alist):
    for k in range(len(Alist)):
        for j in range(len(Alist) - 1):
            if Alist[j] > Alist[j + 1]:
                Alist[j], Alist[j + 1] = Alist[j + 1], Alist[j]
                print(f"\nThe List @ {k} th Iteration Is: {Alist}")

    print(f"\nThe Total Number Of Iterations Used Is {k - 1}")
    return Alist


Blist = []
print("Enter The Number Of Elements You Want To Enter: ")
n = int(input())
print("Enter The Elements: ")
for i in range(n):
    Blist.append(int(input()))

print(f"\nThe List after Sorting @ bubble is:  {bubbleSort(Blist)}")
