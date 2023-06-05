class Node:
    """
    Implementation of a node in a linked list.
    """
    def __init__(self, data, next_=None):
        self.data = data
        self.next = next_

class Queue:
    """
    Implementation of a queue data structure.
    """
    def __init__(self):
        """
        Initializes an empty queue.
        """
        self.front = None
        self.rear = None

    def enqueue(self, data):
        """
        Adds an element to the back of the queue.

        Args:
            data: The element to be added to the queue.
        """
        new_node = Node(data)
        if self.front:
            self.rear.next = new_node
            self.rear = new_node
        else:
            self.front = new_node
            self.rear = new_node

    def dequeue(self):
        """
        Removes and returns the element at the front of the queue.

        Returns:
            The element at the front of the queue.

        Raises:
            AttributeError: If the queue is empty.
        """
        if self.front:
            temp = self.front
            if self.front.next is None:
                self.front = None
                self.rear = None
            else:
                self.front = self.front.next
            temp.next = None
            return temp.data
        else:
            raise AttributeError('The queue is Empty')


class AnimalShelter:
    """
    Represents an animal shelter that holds cats and dogs.
    """
    def __init__(self, name):
        """
        Initializes a new animal shelter with separate queues for cats and dogs.

        Args:
            name (str): The name of the animal shelter.
        """
        self.name = name
        self.cats = Queue()
        self.dogs = Queue()

    def enqueue(self, animal):
        """
        Enqueues an animal into the appropriate queue based on its type.

        Args:
            animal: The animal object to be enqueued.
        """
        if animal.type == 'cat':
            self.cats.enqueue(animal)
        elif animal.type == 'dog':
            self.dogs.enqueue(animal)
        
    def dequeue(self, pref=None):
        """
        Dequeues the first cat or dog in the respective queue based on the preference.

        Args:
            pref (str): The preferred type of animal to dequeue. Default is None.

        Returns:
            The dequeued animal or None if no animal of the preferred type is found.
        """
        if pref == 'cat':
            return self.cats.dequeue()
        elif pref == 'dog':
            return self.dogs.dequeue()


class Cat:
    """
    Represents a cat.
    """
    def __init__(self, name):
        """
        Initializes a new cat with the given name.

        Args:
            name (str): The name of the cat.
        """
        self.name = name
        self.type = 'cat'

class Dog:
    """
    Represents a dog.
    """
    def __init__(self, name):
        """
        Initializes a new dog with the given name.

        Args:
            name (str): The name of the dog.
        """
        self.name = name
        self.type = 'dog'
# Create a new animal shelter
shelter = AnimalShelter("My Shelter")

# Enqueue some cats and dogs
shelter.enqueue(Cat("Whiskers"))
shelter.enqueue(Dog("Buddy"))
shelter.enqueue(Cat("Tom"))
shelter.enqueue(Dog("Max"))

# Dequeue a cat
cat = shelter.dequeue("cat")
print(cat.name)  # Prints "Whiskers"

# Dequeue a dog
dog = shelter.dequeue("dog")
print(dog.name)  # Prints "Buddy"

# Dequeue a cat
cat = shelter.dequeue("cat")
print(cat.name)  # Prints "Tom"

# Dequeue a dog
dog = shelter.dequeue("dog")
print(dog.name)  # Prints "Max"

# Try to dequeue an animal from an empty queue
try:
    shelter.dequeue("cat")
except AttributeError as e:
    print(e)  # Prints "The queue is Empty"

# Enqueue a cat and a dog
shelter.enqueue(Cat("Mittens"))
shelter.enqueue(Dog("Rocky"))

# Dequeue a dog
dog = shelter.dequeue("dog")
print(dog.name)  # Prints "Rocky"

# Dequeue a cat
cat = shelter.dequeue("cat")
print(cat.name)  # Prints "Mittens"

# Try to dequeue a dog when only cats are available
dog = shelter.dequeue("dog")
print(dog)  # Prints "None"

# Try to dequeue a cat when only dogs are available
cat = shelter.dequeue("cat")
print(cat)  # Prints "None"
