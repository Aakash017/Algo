"""
Animal Shelter
"""


class AnimalShelter:
    def __init__(self):
        self.stack = []

    def __str__(self):
        return self.stack

    def enqueue(self, animal):
        self.stack.append(animal)

    def dequeany(self):
        return self.stack.pop(0)

    def dequeuedog(self):
        i = 0
        while i < len(self.stack):
            if self.stack[i] == "dog":
                return self.stack.pop(i), i
            i+=1

    def dequeuecat(self):
        i = 0
        while i < len(self.stack):
            if self.stack[i] == "cat":
                return self.stack.pop(i), i
            i+=1

shelter=AnimalShelter()
shelter.enqueue("dog")
shelter.enqueue("cat")
shelter.enqueue("cat")
shelter.enqueue("dog")
shelter.enqueue("cat")
shelter.enqueue("cat")
shelter.enqueue("dog")
shelter.enqueue("dog")
print(shelter.dequeany())
print(shelter.dequeuedog())
print(shelter.dequeuecat())
print(shelter.dequeuecat())

