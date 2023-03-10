import random
import time
import matplotlib.pyplot as plt

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    
    return -1

def binary_search_recursion(array, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if array[mid] == target:
        return mid
    elif array[mid] < target:
        return binary_search_recursion(array, target, mid + 1, high)
    else:
        return binary_search_recursion(array, target, low, mid - 1)

def measure_time(func, *args):
    start = time.time()
    result = func(*args)
    end = time.time()
    return end - start

def main():
    # Generate a sorted array of 1000 elements
    size = 1000
    array = sorted(random.sample(range(size * 10), size))

    # Select a random target element from the array
    target = random.choice(array)

    # Measure the execution time of the iterative implementation
    measurements_iterative = []
    measurements_recursive = []
    for i in range(100):
        measurements_iterative.append(measure_time(linear_search, array, target))
        measurements_recursive.append(measure_time(binary_search_recursion, array, target, 0, size - 1))

    # Print the minimum and average execution times for both implementations
    print(f"Search with linear iteration: min={min(measurements_iterative)}, avg={sum(measurements_iterative)/len(measurements_iterative)}")
    print(f"Binary search with recursion: min={min(measurements_recursive)}, avg={sum(measurements_recursive)/len(measurements_recursive)}")

    # Plot a histogram of the execution time distribution for both implementations
    plt.hist(measurements_iterative, alpha=0.5, label='Linear')
    plt.hist(measurements_recursive, alpha=0.5, label='Binary')
    plt.legend(loc='upper right')
    plt.title('Execution time distribution')
    plt.xlabel('Execution time (s)')
    plt.ylabel('Frequency')
    plt.show()

if __name__ == '__main__':
    main()
