"""
This module implements an AnimalShelter class that holds dogs and cats using a first-in, first-out approach.

Classes:
- Animal: Represents an animal with species and name attributes.
- Node: Represents a node in the linked list used by the AnimalShelter.
- AnimalShelter: Represents an animal shelter with enqueue and dequeue operations.

Usage:
1. Create an instance of the AnimalShelter class.
2. Enqueue animals using the enqueue method, providing an Animal object.
3. Dequeue animals based on preference (dog or cat) using the dequeue method.
   If the preference is not "dog" or "cat", None is returned.
4. The AnimalShelter class maintains the order of animals based on their arrival time.
"""

class Animal:
    def __init__(self, species, name):
        self.species = species
        self.name = name

    def __str__(self):
        return f"{self.species}: {self.name}"


class Node:
    def __init__(self, animal, timestamp):
        self.animal = animal
        self.timestamp = timestamp
        self.next = None


class AnimalShelter:
    def __init__(self):
        self.head = None
        self.tail = None
        self.timestamp = 0
    
    def enqueue(self, animal):
        """
        Enqueues an animal into the animal shelter.

        Args:
            animal (Animal): The animal object to be enqueued.

        Raises:
            ValueError: If the animal species is neither "dog" nor "cat".
        """
        if animal.species != "dog" and animal.species != "cat":
            raise ValueError("Invalid species. Animal must be either a dog or a cat.")
        
        new_node = Node(animal, self.timestamp)
        self.timestamp += 1

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    
    def dequeue(self, pref):
        """
        Dequeues an animal from the animal shelter based on preference.

        Args:
            pref (str): The preferred species ("dog" or "cat").

        Returns:
            Animal or None: The dequeued animal or None if no animal of the preferred species is found.
        """
        if pref != "dog" and pref != "cat":
            return None
        
        if not self.head:
            return None
        
        if self.head.animal.species == pref:
            dequeued_animal = self.head.animal
            self.head = self.head.next
            return dequeued_animal
        
        curr = self.head
        while curr.next:
            if curr.next.animal.species == pref:
                dequeued_animal = curr.next.animal
                curr.next = curr.next.next
                return dequeued_animal
            curr = curr.next
        
        return None


# Test the AnimalShelter class
shelter = AnimalShelter()
shelter.enqueue(Animal("dog", "Rex"))
shelter.enqueue(Animal("cat", "Whiskers"))
shelter.enqueue(Animal("dog", "Max"))
shelter.enqueue(Animal("cat", "Mittens"))


print(shelter.dequeue("dog"))  # Expected output: Dog: Rex
print(shelter.dequeue("cat"))  # Expected output: Cat: Whiskers

shelter.enqueue(Animal("dog", "Buddy"))
shelter.enqueue(Animal("cat", "Smokey"))

print(shelter.dequeue("camel"))  # Expected output: None

print(shelter.dequeue("dog"))  # Expected output: Dog: Max
print(shelter.dequeue("cat"))  # Expected output: Cat: Mittens
print(shelter.dequeue("dog"))  # Expected output: Dog: Buddy
print(shelter.dequeue("cat"))  # Expected output: Cat: Smokey

print(shelter.dequeue("dog"))  # Expected output: None
print(shelter.dequeue("cat"))  # Expected output: None
