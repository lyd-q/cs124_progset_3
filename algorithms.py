import random
import numpy as np
import KK
import math

#generates a random neighbor
def rand_neighbor(S):
    n = len(S)
    i = random.randint(1, n)
    j = random.randint(1, n)

    #make sure they're not the same
    while (i == j):
        j = random.randint(1, n)
    
    #generate a random neighbor
    S_prime = S
    S_prime[i] = S_prime[i]*(-1)

    if random.choice(1, -1) == 1:
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
        if (np.dot(A, S_prime) < np.dot(A, S)):
            S = S_prime
    return S

def hill_climbing(A, iters):
    n = len(A)
    S = np.array([random.choice([1, -1]) for i in range(n)])
    for i in range(iters):
        S_prime = rand_neighbor(S)
        if (np.dot(A, S_prime) < np.dot(A, S)):
            S = S_prime
    return S
        
def simulated_annealing(A, iter):
    n = len(A)
    S = np.array([random.choice([1, -1]) for i in range(n)])
    S_doubleprime = S 
    for i in range(iter):
        #s' = random neighbor
        S_prime = rand_neighbor(S)
        if (np.dot(A, S_prime) < np.dot(A, S)):
            S = S_prime
        else:
            p = math.exp(-((np.dot(A, S_prime) - np.dot(A, S_prime))/T(i)))
            if random.random() < p:
                S = S_prime
        if (np.dot(A, S) < np.dot(A, S_doubleprime)):
            S_doubleprime = S
    return S_doubleprime


#okay yippee! now for the preparitioned versions

def rand_neighbor_pp(P):
    n = len(P)
    i = random.randint(1, n)
    j = random.randint(1, n)

    #make sure they're not the same
    while (P[i] == j):
        j = random.randint(1, n)

    #set p_i to j
    P[i] = j
    return P

def repeated_random_pp(A, iters):

    #start with random P
    n = len(A)
    P = np.array([random.randrange(1,n) for i in range(n)])
    for i in range(iters):
        P_prime = np.array([random.randrange(1,n) for i in range(n)])
        if KK.KK(P_prime) < KK.KK(P):
            P = P_prime
    return P

def hill_climbing_pp(A, iters):
    n = len(A)
    P = np.array([random.randrange(1,n) for i in range(n)])
    for i in range(iters):
        P_prime = rand_neighbor_pp(P)
        if KK.KK(P_prime) < KK.KK(P):
            P = P_prime
    return P

def  simulated_annealing_pp(A, iters):
    n = len(A)
    P = np.array([random.randrange(1,n) for i in range(n)])
    P_doubleprime = P 
    for i in range(iters):
        P_prime = rand_neighbor_pp(P)
        if KK.KK(P_prime) < KK.KK(P):
            P = P_prime
        else:
            p = math.exp(-((np.dot(A, P_prime) - np.dot(A, P_prime))/T(i)))
            if random.random() < p:
                P = P_prime
        if KK.KK(P_prime) < KK.KK(P_doubleprime):
            P_doubleprime = P
    return P_doubleprime
