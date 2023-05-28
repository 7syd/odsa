class HashingDemo:
    def __init__(self, size):
        self.size = size
        self.HashTable = [0] * self.size
        self.num_of_elements = 0
        self.comparisons = 0

    def isTableFull(self):
        return self.num_of_elements == self.size

    def HashFun(self, element):
        return element % self.size

    def insertElement_Linear(self, element):
        if self.isTableFull():
            print("Hash Table Full")
            return False

        position = self.HashFun(element)

        if self.HashTable[position] == 0:
            self.HashTable[position] = element
            print(f"Telephone Number {element} at position {position}")
            self.num_of_elements += 1
        else:
            print(f"Collision has occurred for Telephone number {element} at index {position}")
            position = self.linearProbing(element, position)
            self.HashTable[position] = element
            self.num_of_elements += 1
        return True

    def linearProbing(self, element, position):
        while self.HashTable[position] != 0:
            position = (position + 1) % self.size
        return position

    def insertElement_Quadratic(self, element):
        if self.isTableFull():
            print("Hash Table Full")
            return False

        position = self.HashFun(element)
        if self.HashTable[position] == 0:
            self.HashTable[position] = element
            print(f"Telephone Number {element} at position {position}")
            self.num_of_elements += 1
        else:
            print(f"Collision has occurred for Telephone number {element} at index {position}")
            occupiedStatus, position = self.quadraticProbing(element, position)
            if occupiedStatus:
                self.HashTable[position] = element
                self.num_of_elements += 1
        return True

    def quadraticProbing(self, element, position):
        limit = 50
        i = 1
        while i <= limit:
            newPosition = (position + (i ** 2)) % self.size
            if self.HashTable[newPosition] == 0:
                return True, newPosition
            i += 1
        return False, position

    def search(self, element):
        position = self.HashFun(element)
        self.comparisons += 1

        if self.HashTable[position] == element:
            return position

        temp = position - 1
        while position < self.size:
            if self.HashTable[position] != element:
                position += 1
                self.comparisons += 1
            else:
                return position

        position = temp
        while position >= 0:
            if self.HashTable[position] != element:
                position -= 1
                self.comparisons += 1
            else:
                return position

        print("Element not found")
        return False

    def display(self):
        print("\n")
        print("---------------------------")
        print("\n Position \t Telephone Number\n")
        print("---------------------------")
        for i in range(self.size):
            print(f"\t{i} ====> {self.HashTable[i]}")


hash_object1 = HashingDemo(8)
print("\n Inserting The Telephone Numbers in the Hash Table....\n")
print("\n Collision Resolution using Linear Probing\n")
hash_object1.insertElement_Linear(1111111112)
hash_object1.insertElement_Linear(3333333331)
hash_object1.insertElement_Linear(4444444417)
hash_object1.insertElement_Linear(5555555590)
hash_object1.insertElement_Linear(6666666621)
hash_object1.insertElement_Linear(7777777788)
hash_object1.insertElement_Linear(8888888840)
hash_object1.insertElement_Linear(9999999977)

hash_object1.display()
print()

print("The position of number 3333333331 is:", hash_object1.search(3333333331))
print("The position of number 6666666621 is:", hash_object1.search(6666666621))
print("The position of number 9999999977 is:", hash_object1.search(9999999977))
print("\n-----------------------------------------------------------------")
print("Total number of comparisons done for searching =", hash_object1.comparisons)
print("\n-----------------------------------------------------------------")
print("\n\n\n*********************************************************************\n")

hash_object2 = HashingDemo(8)
print("\n Inserting The Telephone Numbers in the Hash Table....\n")
print("\n Collision Resolution using Quadratic Probing\n")
hash_object2.insertElement_Quadratic(1111111112)
hash_object2.insertElement_Quadratic(3333333331)
hash_object2.insertElement_Quadratic(4444444417)
hash_object2.insertElement_Quadratic(5555555590)
hash_object2.insertElement_Quadratic(6666666621)
hash_object2.insertElement_Quadratic(7777777788)
hash_object2.insertElement_Quadratic(8888888840)
hash_object2.insertElement_Quadratic(9999999977)

hash_object2.display()
print()

print("The position of number 3333333331 is:", hash_object2.search(3333333331))
print("The position of number 6666666621 is:", hash_object2.search(6666666621))
print("The position of number 9999999977 is:", hash_object2.search(9999999977))
print("\n-----------------------------------------------------------------")
print("Total number of comparisons done for searching =", hash_object2.comparisons)
print("\n-----------------------------------------------------------------")
print("\n\n\n*********************************************************************\n")
