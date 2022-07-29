# Python

## Queue

---

![](images/learning.png) **Learning Objectives**

* Learn how to use the build in Python queue

---

A queue is a data structure. Essentially, it is a list that has order,
meaning that the queue has an object to be removed first and an 
object to be removed last.

There are three types of queues: FIFO (first in first out), 
LIFO (last in first out), and Priority Queue (order is based
on the data's individual priority score). 

```python
import queue
```

Then, the data structures can be built as follows:

### FIFO Queue

A FIFO queue is the most basic type of queue. Simply put, 
the values that go into the data structure first are the values
that comes out of the data structure first. 

FIFO queues are easy to implement:

```python
# this queue is a FIFO queue
fq = queue.Queue()

for x in range(0, 10):
    fq.put(x)

while not fq.empty():
    print(fq.get())
```

This code can be accessed on [GitHub](https://github.com/cybertraining-dsc/reu2022/tree/main/project/graphics/examples/queue_example.py)

### LIFO Queue

A LIFO queue is another very basic type of queue. Simply put,
it is a queue that operates the last item inserted being the
first item that is removed. 

LIFO queues are simple to implement:

```python
# this queue is a LIFO queue

lq = queue.LifoQueue()

for x in range(0, 10):
    lq.put(x)
```

This code can be accesed on [GitHub](https://github.com/cybertraining-dsc/reu2022/tree/main/project/graphics/examples/queue_example.py)

### Priority Queue

Finally, priority queues are a more complex queue type. Priority
queues work by inserting elements with a sorted priority. For 
example, if an 8 is inserted before a 2, the 2 will be removed 
first. 

Priority queues are easily implemented:

```python
# this queue is a Priority queue

pq = queue.PriorityQueue()

for x in range(0, 10):
    value = int(random.random() * 100)
    print('number being inserted into the priority queue', value)
    pq.put(value)

print()

while not pq.empty():
    print('number being removed from the pq', pq.get())
```

This code can be accessed on [GitHub](https://github.com/cybertraining-dsc/reu2022/tree/main/project/graphics/examples/queue_example.py)

All specifics on queues can be researched at the below links:

* [Python Queues](<https://pymotw.com/3/queue/index.html>)
* [Priority Queues in Python](<https://www.geeksforgeeks.org/priority-queue-in-python/>)
* [Queue Documentations](<https://docs.python.org/3/library/queue.html>)