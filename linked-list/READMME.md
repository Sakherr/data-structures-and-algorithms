# Stack and a Queue Implementation
## Create a stack that has four methods: push, pop, peek, is_empty.

## Create a queue that has four methods: enqueue, dequeue, peek, is_empty


## Whiteboard Process
  > NO NEEDED
# Approach & Efficiency

# STACK
## push: The push operation has a time complexity of O(1) since it adds a new element to the top of the stack by updating the top pointer. The space complexity is also O(1) as it only requires additional memory for the new node.

## pop: The pop operation has a time complexity of O(1) since it removes the top element from the stack by updating the top pointer. The space complexity is O(1) as it does not require additional memory allocation.

## peek: The peek operation has a time complexity of O(1) since it returns the value of the top element without modifying the stack. The space complexity is O(1) as it does not require additional memory allocation.

# QUEUE

 ## enqueue: The enqueue operation has a time complexity of O(1) on average. It adds a new element to the back of the queue by traversing the linked list until the last node and appending the new node to it. The space complexity is also O(1) as it only requires additional memory for the new node.

## dequeue: The dequeue operation has a time complexity of O(1) since it removes the front element from the queue by updating the front pointer. The space complexity is O(1) as it does not require additional memory allocation.

## peek: The peek operation has a time complexity of O(1) since it returns the value of the front element without modifying the queue. The space complexity is O(1) as it does not require additional memory allocation.

## is_empty: The is_empty operation has a time complexity of O(1) since it only checks whether the front pointer is None or not. The space complexity is O(1) as it does not require additional memory allocation.

## is_empty: The is_empty operation has a time complexity of O(1) since it only checks whether the top pointer is None or not. The space complexity is O(1) as it does not require additional memory allocation.

# Solution
  >pytest