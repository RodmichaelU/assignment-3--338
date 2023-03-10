import sys

lst = []
prev_capacity = sys.getsizeof(lst)

for i in range(64):
    lst.append(i)
    capacity = sys.getsizeof(lst)
    if capacity != prev_capacity:
        print(f"Capacity changed from {prev_capacity} bytes to {capacity} bytes at size {len(lst)}")
        prev_capacity = capacity
