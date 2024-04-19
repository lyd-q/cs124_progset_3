import algorithms
import numpy as np
import time
import matplotlib.pyplot as plt

var = 10
setlist = [[0]]*var
resultlist = [[0]*var for _ in range(7)]
timelist = [[0]*var for _ in range(7)]
#generate set of random numbers
for i in range(var):
    setlist[i] = np.random.randint(1, 10**12, 100)

for i in range(var):

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
#print(setlist)

for i in range(7):
    plt.hist(resultlist[i])
    plt.xlabel('Residual')
    plt.ylabel('Frequency')
    plt.title(f'Residual: Algorithm {i}')
    plt.show()

    plt.hist(timelist[i])
    plt.xlabel('Time')
    plt.ylabel('Frequency')
    plt.title(f'Time: Algorithm {i}')
    plt.show()

    print("Min:")
    print("resultlist,", i, ":", np.min(resultlist[i]))
    print("timelist,", i, ":",np.min(timelist[i]))
    print("")

    print("Means:")
    print("resultlist,", i, ":", np.mean(resultlist[i]))
    print("timelist,", i, ":",np.mean(timelist[i]))
    print("")

    print("Max:")
    print("resultlist,", i, ":", np.max(resultlist[i]))
    print("timelist,", i, ":",np.max(timelist[i]))
    print("")

    print("Lists:")
    print("resultlist,", i, ":", (resultlist[i]))
    print("timelist,", i, ":",(timelist[i]))
    print("")

#printing instead

# print("Min:")
# print("resultlist,", i, ":", np.min(resultlist[0]))
# print("timelist,", i, ":",np.min(timelist[0]))
# print("")

# print("Means:")
# print("resultlist,", i, ":", np.mean(resultlist[0]))
# print("timelist,", i, ":",np.mean(timelist[0]))
# print("")

# print("Max:")
# print("resultlist,", i, ":", np.max(resultlist[0]))
# print("timelist,", i, ":",np.max(timelist[0]))
# print("")

# print("Lists:")
# print("resultlist,", i, ":", (resultlist[0]))
# print("timelist,", i, ":",(timelist[0]))
# print("")

# print("Min:")
# print("resultlist,", i, ":", np.min(resultlist[1]))
# print("timelist,", i, ":",np.min(timelist[1]))
# print("")

# print("Means:")
# print("resultlist,", i, ":", np.mean(resultlist[1]))
# print("timelist,", i, ":",np.mean(timelist[1]))
# print("")

# print("Max:")
# print("resultlist,", i, ":", np.max(resultlist[1]))
# print("timelist,", i, ":",np.max(timelist[1]))
# print("")