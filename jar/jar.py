
class Jar:
    def __init__(self, capacity=12):
        if capacity > 0:
            self._capacity = capacity
        else:
            raise ValueError("Capacity can't be less than 0")
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        total = n + self._size
        if total > self._capacity:
            raise ValueError("Cookie Jar over capacity")
        else:
            self._size = n + self._size

    def withdraw(self, n):
        total = self._size - n
        if total < 0:
            raise ValueError("Cookie Jar Overdrawn")
        else:
            self._size = total

    #getter for the capacity
    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    #getter for the size
    @property
    def size(self):
        return self._size


# jar1 = Jar()
# jar2 = Jar(30)
# print(f'Jar1 capacity: ',jar1.capacity)
# print(f'Jar2 capacity: ',jar2.capacity)
# print(f'Jar1 size: ',jar1.size)
# print(f'Jar2 size: ',jar2.size)
# jar1.deposit(5)
# print(f'Jar1 size: ',jar1.size)
# jar1.deposit(5)
# print(jar1)
# jar1.withdraw(3)
# print(jar1)

# #test_jar