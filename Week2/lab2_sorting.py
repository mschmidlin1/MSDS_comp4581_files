
import random




def mergeSort(L):
    pass

def insertionSort(L):
    sorted_list = []
    for i in L:
        if sorted_list.__len__() == 0:
            sorted_list.append(i)
            continue
        inserted=False
        for j in sorted_list:
            if i<=j:
                sorted_list.insert(sorted_list.index(j), i)
                inserted=True
                break
        if inserted==False:
            sorted_list.append(i)
    return sorted_list

    ## Insertion code from the video. Mine is faster even though this code is cleaner.

    # for i in range(1, len(L)):
    #     key = L[i]
    #     j = i-1
    #     while j>=0 and L[j]>key:
    #         L[j+1] = L[j]
    #         j = j-1
    #     L[j+1] = key
    # return L

def bubbleSort(L):
    pass
