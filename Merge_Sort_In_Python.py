def MergeSort(A):
    if len(A) > 1:
        mid = len(A) // 2
        L1 = A[:mid]
        L2 = A[mid:]
        print("L1:", L1)
        print("L2:", L2)
        MergeSort(L1)
        MergeSort(L2)

        i = j = k = 0

        while i < len(L1) and j < len(L2):
            if L1[i] < L2[j]:
                A[k] = L1[i]
                i += 1
            else:
                A[k] = L2[j]
                j += 1
            k += 1

        while i < len(L1):
            A[k] = L1[i]
            i += 1
            k += 1

        while j < len(L2):
            A[k] = L2[j]
            j += 1
            k += 1
        print(f"The List @ {i}th Iteration Is: {A}")
    return A


MergeSort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
