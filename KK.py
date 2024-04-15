#KK
#input array A
#build heap
#remove max, remove max again (to get 2 largest)
#insert difference, insert 0
import heapq
import math
import numpy as np

# class MaxHeap:
#     def __init__(self):
#         self.heap = []

#     def push(self, elem):
#         heapq.heappush(self, -1 * elem)

#     def pop(self, elem):
#         return (-1) * (heapq.heappop(self, elem))


def KK (A):
    #make it negative to use minheap commands
    listA = list(-1 * A)
    heapq.heapify(listA)
    for i in range(0, len(A)):
        max1 = -1 * heapq.heappop(listA)
        max2 = -1 * heapq.heappop(listA)
        diff = -1 * abs(max1 - max2)
        heapq.heappush(listA, diff)
        heapq.heappush(listA, 0)
    #return (-1) * heapq.heappeek(listA)
    return (-1) * listA[0]

# x = np.array([10, 15, 0, 6, 5])
# print(x)
# print(KK(x))