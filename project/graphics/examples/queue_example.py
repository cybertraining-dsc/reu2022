import queue
import random

'''
    Implementation of the built-in python queue as an example of the way the
    data structure works. 
'''

# this queue is a FIFO queue
fq = queue.Queue()

for x in range(0, 10):
    fq.put(x)

while not fq.empty():
    print(fq.get())


# this queue is a LIFO queue

lq = queue.LifoQueue()

for x in range(0, 10):
    lq.put(x)

while not lq.empty():
    print(lq.get())

# this queue is a Priority queue

pq = queue.PriorityQueue()

for x in range(0, 10):
    value = int(random.random() * 100)
    print('number being inserted into the priority queue', value)
    pq.put(value)

print()

while not pq.empty():
    print('number being removed from the pq', pq.get())




