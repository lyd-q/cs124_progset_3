import random
import numpy as np
import KK
import math

# HAVE TO ADD IN A AND MAKE IT ?NOT CA?LL ?KK AND INSTAD JUST ADD ?TOGETHEr

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

def repeated_random(n, iters):
    #generate the random solution:
    S = np.array([random.choice([1, -1]) for i in range(n)])
    for i in range(iters):
        S_prime = np.array([random.choice([1, -1]) for i in range(n)])
        if (KK.KK(S_prime) < KK.KK(S)):
            S = S_prime
    return S

def hill_climbing(n, iters):
    S = np.array([random.choice([1, -1]) for i in range(n)])
    for i in range(iters):
        S_prime = rand_neighbor(S)
        if (KK.KK(S_prime) < KK.KK(S)):
            S = S_prime
    return S
        
def simulated_annealing(n, iter):
    S = np.array([random.choice([1, -1]) for i in range(n)])
    S_doubleprime = S 
    for i in range(iter):
        #s' = random neighbor
        S_prime = rand_neighbor(S)
        if (KK.KK(S_prime) < KK.KK(S)):
            S = S_prime
        else:
            T_iter = 10**10*(0.8)**math.floor(iter/300)
            p = math.exp(-(KK.KK(S_prime) - KK.KK(S)/T_iter))
            if random.random() < p:
                S = S_prime
