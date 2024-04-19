import algorithms
import numpy as np
import time

setlist = [[0]]*50
resultlist = [[0]*50]*7
timelist = [[0]*50]*7
#generate set of random numbers
for i in range(50):
    setlist[i] = np.random.randint(1, 10**12, 100)

for i in range(50):

    start_time = time.time()
    resultlist[0][i] = algorithms.KK(setlist[i])
    end_time = time.time()
    timelist[0][i] = end_time - start_time

    start_time = time.time()
    resultlist[1][i] =  algorithms.repeated_random(setlist[i], 25000)
    end_time = time.time()
    timelist[1][i] = end_time - start_time

    start_time = time.time()
    resultlist[2][i] = algorithms.hill_climbing(setlist[i], 25000)
    end_time = time.time()
    timelist[2][i] = end_time - start_time

    start_time = time.time()
    resultlist[3][i] =  algorithms.simulated_annealing(setlist[i], 25000)
    end_time = time.time()
    timelist[3][i] = end_time - start_time

    start_time = time.time()
    resultlist[4][i] =  algorithms.repeated_random_pp(setlist[i], 25000)
    end_time = time.time()
    timelist[4][i] = end_time - start_time

    start_time = time.time()
    resultlist[5][i] =  algorithms.hill_climbing_pp(setlist[i], 25000)
    end_time = time.time()
    timelist[5][i] = end_time - start_time
    
    start_time = time.time()
    resultlist[6][i] =  algorithms.simulated_annealing_pp(setlist[i], 25000)
    end_time = time.time()
    timelist[6][i] = end_time - start_time

    print(i)
print(setlist)
    
