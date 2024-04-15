import algorithms
import KK
import numpy as np

setlist = [[0]]*50
resultlist = [[0]*50]*7
#generate set of random numbers
for i in range(50):
    setlist[i] = np.random.randint(1, 10**12, 100)

for i in range(50):
    resultlist[0][i] = KK.KK(setlist[i])
    resultlist[1][i] =  algorithms.repeated_random(setlist[i], 25000)
    resultlist[2][i] = algorithms.hill_climbing(setlist[i], 25000)
    resultlist[3][i] =  algorithms.simulated_annealing(setlist[i], 25000)
    resultlist[4][i] =  algorithms.repeated_random_pp(setlist[i], 25000)
    resultlist[5][i] =  algorithms.hill_climbing_pp(setlist[i], 25000)
    resultlist[6][i] =  algorithms.simulated_annealing_pp(setlist[i], 25000)
    print(i)

print(setlist)
    
