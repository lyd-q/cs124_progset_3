# import random
# import numpy as np
# import KK
# import math

# #generates a random neighbor
# def rand_neighbor(S):
#     n = len(S)
#     i = random.randint(0, n-1)
#     j = random.randint(0, n-1)

#     #make sure they're not the same
#     while (i == j):
#         j = random.randint(0, n-1)
    
#     #generate a random neighbor
#     S_prime = np.copy(S) 
#     S_prime[i] = S_prime[i]*(-1)

#     if random.choice([1, -1]) == 1:
#         S_prime[j] = S_prime[j]*(-1)
    
#     return S_prime

# def T(iter):
#     return 10**10*(0.8)**math.floor(iter/300)

# #should take in A as a argument
# def repeated_random(A, iters):
#     #generate the random solution:
#     n = len(A)
#     S = np.array([random.choice([1, -1]) for i in range(n)])
#     for i in range(iters):
#         S_prime = np.array([random.choice([1, -1]) for i in range(n)])
#         print(S_prime)
#         if (np.dot(A, S_prime) < np.dot(A, S)):
#             S = S_prime
#     return np.dot(A, S)

# def hill_climbing(A, iters):
#     n = len(A)
#     S = np.array([random.choice([1, -1]) for i in range(n)])
#     print(S)
#     for i in range(iters):
#         S_prime = rand_neighbor(S)
#         print(S)
#         print(S_prime)
#         print(abs(np.dot(A, S_prime)))
#         print(abs(np.dot(A, S)))
#         if (abs(np.dot(A, S_prime)) < abs(np.dot(A, S))):
#             S = S_prime
#             print("change")
#     return int(abs(np.dot(A, S)))
        
# def simulated_annealing(A, iter):
#     n = len(A)
#     S = np.array([random.choice([1, -1]) for i in range(n)])
#     S_doubleprime = S 
#     for i in range(iter):
#         #s' = random neighbor
#         S_prime = rand_neighbor(S)
#         if (np.dot(A, S_prime) < np.dot(A, S)):
#             S = S_prime
#         else:
#             p = math.exp(-(abs(np.dot(A, S_prime)) - abs(np.dot(A, S)))/T(i))
#             if random.random() < p:
#                 S = S_prime
#         if (np.dot(A, S) < np.dot(A, S_doubleprime)):
#             S_doubleprime = S
#     return abs(np.dot(S_doubleprime, A))


# #okay yippee! now for the preparitioned versions

# def rand_neighbor_pp(P):
#     n = len(P)
#     i = random.randint(0, n-1)
#     j = random.randint(0, n-1)

#     #make sure they're not the same
#     while (P[i] == j):
#         j = random.randint(0, n-1)

#     #set p_i to j'
#     P_prime = np.copy(P)
#     P_prime[i] = j

#     return P_prime

# def get_A_prime(A, P):
#     n = len(A)
#     A_prime = [0] * n 
#     for j in range(n):
#         A_prime[P[j]] = A_prime[P[j]] + A[j]
#     return np.array(A_prime)


# def repeated_random_pp(A, iters):
#     #start with random P
#     n = len(A)
#     P = np.array([random.randrange(0,n-1) for i in range(n)])
#     newA = get_A_prime(A, P)
#     for i in range(iters):
#         newA = get_A_prime(A, P)
#         P_prime = np.array([random.randrange(0,n-1) for i in range(n)])
#         newA_prime = get_A_prime(A, P_prime)
#         if KK.KK(newA_prime) < KK.KK(newA):
#             P = P_prime
#     return int(KK.KK(newA))

# def hill_climbing_pp(A, iters):
#     n = len(A)
#     P = np.array([random.randrange(1,n) for i in range(n)])
#     for i in range(iters):
#         P_prime = rand_neighbor_pp(P)
#         if KK.KK(P_prime) < KK.KK(P):
#             P = P_prime
#     return KK.KK(P)

# def  simulated_annealing_pp(A, iters):
#     n = len(A)
#     P = np.array([random.randrange(1,n) for i in range(n)])
#     P_doubleprime = P 
#     for i in range(iters):
#         P_prime = rand_neighbor_pp(P)
#         if KK.KK(P_prime) < KK.KK(P):
#             P = P_prime
#         else:
#             p = math.exp(-((np.dot(A, P_prime) - np.dot(A, P_prime))/T(i)))
#             if random.random() < p:
#                 P = P_prime
#         if KK.KK(P_prime) < KK.KK(P_doubleprime):
#             P_doubleprime = P
#     return  KK.KK(P_doubleprime)

import random
import numpy as np
import math
import heapq
import sys


def KK(A):
    #make it negative to use minheap commands
    listA = list(-1 * A)
    heapq.heapify(listA)
    for i in range(0, len(A)):
        max1 = -1 * heapq.heappop(listA)
        max2 = -1 * heapq.heappop(listA)
        diff = -1 * abs(max1 - max2)
        heapq.heappush(listA, diff)
        heapq.heappush(listA, 0)
    return int((-1) * listA[0])

#generates a random neighbor
def rand_neighbor(S):
    n = len(S)
    i = random.randint(0, n-1)
    j = random.randint(0, n-1)

    #make sure they're not the same
    while (i == j):
        j = random.randint(0, n-1)
    
    #generate a random neighbor
    S_prime = np.copy(S) 
    S_prime[i] = S_prime[i]*(-1)

    if random.choice([1, -1]) == 1:
        S_prime[j] = S_prime[j]*(-1)
    
    return S_prime

def T(iter):
    return 10**10*(0.8)**math.floor(iter/300)

#should take in A as a argument
def repeated_random(A, iters):
    #generate the random solution:
    n = len(A)
    S = np.array([random.choice([1, -1]) for i in range(n)])
    for i in range(iters):
        S_prime = np.array([random.choice([1, -1]) for i in range(n)])
        if (abs(np.dot(A, S_prime)) < abs(np.dot(A, S))):
            S = S_prime
    return int(abs(np.dot(A, S)))

def hill_climbing(A, iters):
    n = len(A)
    S = np.array([random.choice([1, -1]) for i in range(n)])
    for i in range(iters):
        S_prime = rand_neighbor(S)
        if (abs(np.dot(A, S_prime)) < abs(np.dot(A, S))):
            S = S_prime
    return int(abs(np.dot(A, S)))
        
def simulated_annealing(A, iter):
    n = len(A)
    S = np.array([random.choice([1, -1]) for i in range(n)])
    S_doubleprime = S 
    for i in range(iter):
        #s' = random neighbor
        S_prime = rand_neighbor(S)
        if (abs(np.dot(A, S_prime)) < abs(np.dot(A, S))):
            S = S_prime
        else:
            p = math.exp(-(abs(np.dot(A, S_prime)) - abs(np.dot(A, S)))/T(i))
            if random.random() < p:
                S = S_prime
        if (abs(np.dot(A, S)) < abs(np.dot(A, S_doubleprime))):
            S_doubleprime = S
    return int(abs(np.dot(S_doubleprime, A)))


#okay yippee! now for the preparitioned versions

def rand_neighbor_pp(P):
    n = len(P)
    i = random.randint(0, n-1)
    j = random.randint(0, n-1)

    #make sure they're not the same
    while (P[i] == j):
        j = random.randint(0, n-1)

    #set p_i to j'
    P_prime = np.copy(P)
    P_prime[i] = j

    return P_prime

def get_A_prime(A, P):
    n = len(A)
    A_prime = [0] * n 
    for j in range(n):
        A_prime[P[j]] = A_prime[P[j]] + A[j]
    return np.array(A_prime)


def repeated_random_pp(A, iters):
    #start with random P
    n = len(A)
    P = np.array([random.randrange(0,n-1) for i in range(n)])
    #store residue 
    currentA = get_A_prime(A, P)
    residue = KK(currentA)
    for i in range(iters):
        P_prime = np.array([random.randrange(0, n-1) for i in range(n)])
        newA_prime = get_A_prime(A, P_prime)
        # residue = KK(newA)
        cand_res = KK(newA_prime)
        if cand_res < residue:
            P = P_prime
            currentA = newA_prime
            residue = cand_res
    return residue

def hill_climbing_pp(A, iters):
    n = len(A)
    P = np.array([random.randrange(1,n) for i in range(n)])
    currentA = get_A_prime(A, P)
    residue = KK(currentA)
    for i in range(iters):
        P_prime = rand_neighbor_pp(P)
        newA_prime = get_A_prime(A, P_prime)
        cand_res = KK(newA_prime)
        if cand_res < residue:
            P = P_prime
            currentA = newA_prime
            residue = cand_res
    return residue

def  simulated_annealing_pp(A, iters):
    n = len(A)
    P = np.array([random.randrange(1,n) for i in range(n)])
    currentA = get_A_prime(A, P)
    residue = KK(currentA)


    P_doubleprime = P 
    newA_double = get_A_prime(A, P_doubleprime)
    double_res = KK(newA_double)

    for i in range(iters):
        P_prime = rand_neighbor_pp(P)
        newA_prime = get_A_prime(A, P_prime)
        cand_res = KK(newA_prime)
        if cand_res < residue:
            P = P_prime
            currentA = newA_prime
            residue = cand_res
        else:
            p = math.exp(-(( cand_res - residue)/T(i)))
            if random.random() < p:
                P = P_prime
                currentA = newA_prime
                residue = cand_res
        
        if cand_res < double_res:
            P_doubleprime = P
            double_res = residue
            newA_double = currentA

    return double_res

x = np.array([10, 8, 7, 6, 5])
# print(KK.KK(x))
# print(repeated_random(x, 1))

# print(hill_climbing(x, 10))
print(simulated_annealing(x, 10000))
# print(repeated_random_pp(x, 100))
#print(hill_climbing_pp(x, 10))
# print(simulated_annealing_pp(x, 25000))

# # print(rand_neighbor([1, 1, 1, 1, 1, 1]))
# P = np.array([0, 1, 1, 3, 4])
# y = get_A_prime(x, P)
# print(y)
# print(KK.KK(y))