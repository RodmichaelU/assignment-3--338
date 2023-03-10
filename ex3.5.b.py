import time
import random
import heapq
import matplotlib.pyplot as plt

class Node:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority
        self.next = None
        
class PriorityQueueLinkedList:
    def __init__(self):
        self.head = None
        
    def push(self, data, priority):
        new_node = Node(data, priority)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            
    def pop(self):
        if not self.head:
            return None
        min_node = self.head
        min_node_prev = None
        current = self.head
        while current.next:
            if current.next.priority < min_node.priority:
                min_node = current.next
                min_node_prev = current
            current = current.next
        if min_node_prev:
            min_node_prev.next = min_node.next
        else:
            self.head = min_node.next
        return min_node.data

class PriorityQueueHeap:
    def __init__(self):
        self.elements = []
        
    def push(self, data, priority):
        heapq.heappush(self.elements, (priority, data))
        
    def pop(self):
        if not self.elements:
            return None
        return heapq.heappop(self.elements)[1]
    
def run_experiment(size, num_tests):
    data = [random.randint(0, 1000) for _ in range(size)]
    pq_ll = PriorityQueueLinkedList()
    pq_heap = PriorityQueueHeap()

    ll_times = []
    heap_times = []

    for _ in range(num_tests):
        start_time = time.time()
        for i in data:
            pq_ll.push(i, i)
        while pq_ll.head:
            pq_ll.pop()
        end_time = time.time()
        ll_times.append(end_time - start_time)

        start_time = time.time()
        for i in data:
            pq_heap.push(i, i)
        while pq_heap.elements:
            pq_heap.pop()
        end_time = time.time()
        heap_times.append(end_time - start_time)

    return ll_times, heap_times

ll_times, heap_times = run_experiment(1000, 100)

fig, axs = plt.subplots(2, figsize=(8, 8))
fig.suptitle('Execution Time Distribution')

axs[0].hist(ll_times, alpha=0.5)
axs[0].set_title('Linked List')
axs[0].set_xlabel('Execution Time (seconds)')
axs[0].set_ylabel('Frequency')

axs[1].hist(heap_times, alpha=0.5)
axs[1].set_title('Heap')
axs[1].set_xlabel('Execution Time (seconds)')
axs[1].set_ylabel('Frequency')

plt.show()

print(f"Linked List avg: {sum(ll_times)/len(ll_times)}")
print(f"Heap avg: {sum(heap_times)/len(heap_times)}")
