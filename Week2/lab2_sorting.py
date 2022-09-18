
import random
import copy
from time import time
import random
from tabulate import tabulate

def merge(left, right):
    sorted_list = []

    while len(left)>0 and len(right)>0:

        if left[0]<right[0]:
            e = left.pop(0)
            sorted_list.append(e)

        else:
            e = right.pop(0)
            sorted_list.append(e)

        
    if len(left)>0:
        while len(left)>0:
            e = left.pop(0)
            sorted_list.append(e)

    
    else:
        while len(right)>0:
            e = right.pop(0)
            sorted_list.append(e)

    
    if len(right)>0 or len(left)>0:
        raise ValueError

    return sorted_list

def mergeSort(L):
    if len(L) < 2:
        return L[:]
    else:
        mid = len(L)//2
        left = mergeSort(L[:mid])
        right = mergeSort(L[mid:])
        return merge(left, right)

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
    A = copy.copy(L)
    for j in range(len(A)):
        for i in range(len(A)-1):
            if A[i]>A[i+1]:
                a = A[i]
                b = A[i+1]
                A[i] = b
                A[i+1] = a

    return A

def main():

    results = {}
    results["N"] = [i for i in range(100, 1100, 100)]
    results["Merge"] = []
    results["Insert"] = []
    results["Bubble"] = []

    for n in results["N"]:
        L = [i for i in range(n)]
        random.shuffle(L)
        t1 = time()
        mergeSort(L)
        t2 = time()
        insertionSort(L)
        t3 = time()
        bubbleSort(L)
        t4 = time()

        results["Merge"].append((t2-t1)*1000)
        results["Insert"].append((t3-t2)*1000)
        results["Bubble"].append((t4-t3)*1000)

    print(tabulate(results, headers=results.keys(), tablefmt='fancy_grid'))



if __name__ == "__main__":
    main()