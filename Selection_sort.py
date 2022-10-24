def selectionsort(lst):
    for i in range(len(lst)):
        min_index = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]
        print(f"\nThe List @ {i} th Iteration Is: {lst}")
    print(f"\nThe Total Number Of Iterations Used Is {i + 1}")
    return lst


Sl = []
print("Enter The Number Of Elements You Want To Enter: ")
n = int(input())
print("Enter The Elements: ")
for i in range(n):
    Sl.append(int(input()))

print(f"\nThe List after Sorting @ bubble is:  {selectionsort(Sl)}")
