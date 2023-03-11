"""
Prints when the capacity changes
import sys

lst = []
prev_capacity = sys.getsizeof(lst)

print("Number of elements in my_list: " , len(lst))
print("Allocated memory for my_list: ", sys.getsizeof(lst))
print()

for i in range(64):
    lst.append(i)
    capacity = sys.getsizeof(lst)
    if capacity != prev_capacity:
        print(f"Capacity changed from {prev_capacity} bytes to {capacity} bytes at size {len(lst)}")
        prev_capacity = capacity
        
"""


"""
Prints the capacity for all entries
"""
import sys

lst = []
capacity = sys.getsizeof(lst)
print(f"Initial capacity: {capacity}")

for i in range(1, 64):
    lst.append(i)
    new_capacity = sys.getsizeof(lst)
    if new_capacity != capacity:
        print(f"Capacity changed from {capacity} to {new_capacity} at length {len(lst)}")
        capacity = new_capacity
    else:
        print(f"Capacity is {capacity} at length {len(lst)}")



