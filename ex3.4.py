import threading
import random
import time

class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None for i in range(size)]
        self.head = self.tail = -1
        self._lock = threading.Lock()

    def lock(self):
        self._lock.acquire()

    def unlock(self):
        self._lock.release()

    def enqueue(self, data):
        # Implement enqueue function
        while True:
            self.lock()
            if ((self.tail + 1) % self.size) != self.head:                  # Checks if queue is full (Use modulus for circular queue)
                if self.head == -1:                                         # Checks if queue is empty
                    self.head = 0                                           
                self.tail = (self.tail + 1) % self.size                     # Increment tail, modulus is used in case we exceed size to maintain circularity
                self.queue[self.tail] = data                                # Set the value into the queue
                self.unlock()               
                return
            else:
                self.unlock()
                time.sleep(1)                                               # Sleep 1 second, than try again
    
    def dequeue(self):
        # Implement dequeue function
        while True:
            self.lock()
            if self.head != -1:                                             # Proceeds if queue is not empty
                data = self.queue[self.head]                                # Get value to dequeue
                if self.head == self.tail:                                  # If pointers point to last remaining element, set to -1 to show empty queue as we are dequeueing it
                    self.head = self.tail = -1
                else:                                                       
                    self.head = (self.head + 1) % self.size                 # Increment head, modulus is used in case we exceed size to maintain circularity
                self.unlock()
                return data
            else:
                self.unlock()
                time.sleep(1)


def producer():
    while True:
        # Implement producer function
        random_number = random.randint(1, 10)
        time.sleep(random_number)
        q.enqueue(random_number)

def consumer():
    while True:
        # Implement consumer function
        random_number = random.randint(1, 10)
        time.sleep(random_number)
        dequeued = q.dequeue()
        print("Dequeued:", dequeued)


if __name__ == '__main__':
    q = CircularQueue(5)
    t1 = threading.Thread(target=producer)
    t2 = threading.Thread(target=consumer)
    t1.start()
    t2.start()
    t1.join()
    t2.join()