#KK
#input array A
#build heap
#remove max, remove max again (to get 2 largest)
#insert difference, insert 0
import heapq
import math

# class MaxHeap:
#     def __init__(self):
#         self.heap = []

#     def push(self, elem):
#         heapq.heappush(self, -1 * elem)

#     def pop(self, elem):
#         return (-1) * (heapq.heappop(self, elem))


def KK (A):
    #make it negative to use minheap commands
    heapq.heapify(-1 * A)
    for i in range(0, len(A)):
        max1 = -1 * heapq.heappop(A)
        max2 = -1 * heapq.heappop(A)
        diff = -1 * math.abs(max1 - max2)
        heapq.heappush(A, diff)
        heapq.heappush(A, 0)
    return (-1) * heapq.heappeek(A)

