import json
import time
import matplotlib.pyplot as plt

with open("ex2data.json") as InFile:
    data = json.load(InFile)

with open("ex2tasks.json") as InFile:
    tasks = json.load(InFile)

def binary_search_with_config(x, first_mid):
    low = 0
    high = len(data) - 1

    if data[first_mid] == x:
        return first_mid
    elif data[first_mid] < x:
        low = first_mid + 1
    else:
        high = first_mid - 1

    while low <= high:
        mid = (low + high) // 2

        if data[mid] == x:
            return mid
        elif data[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    return -1

best_midpoints = {}
for value in tasks:
    init_mid = 0
    mid = []
    times = []
    while (init_mid < len(data)):
        start = time.perf_counter()
        binary_search_with_config(value, init_mid)
        end = time.perf_counter()
        mid.append(init_mid)
        times.append(end-start)
        init_mid += 500
    best_time = min(times)
    best_index = times.index(best_time)
    best_midpoint = mid[best_index]
    best_midpoints[value] = best_midpoint

print(best_midpoints)

plt.scatter(tasks, [best_midpoints[x] for x in tasks])
plt.title("Best Midpoints for Each Task")
plt.xlabel("Task Value")
plt.ylabel("Best Midpoint")
plt.show()
