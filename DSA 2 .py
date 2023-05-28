class KeyValueNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class ChainingDictionaryWithReplacement:
    def __init__(self, size):
        self.size = size
        self.hash_table = [None] * size

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        node = self.hash_table[index]

        while node is not None:
            if node.key == key:
                node.value = value
                return
            node = node.next

        new_node = KeyValueNode(key, value)
        new_node.next = self.hash_table[index]
        self.hash_table[index] = new_node

    def find(self, key):
        index = self.hash_function(key)
        node = self.hash_table[index]

        while node is not None:
            if node.key == key:
                return node.value
            node = node.next

        return None

    def delete(self, key):
        index = self.hash_function(key)
        node = self.hash_table[index]
        prev_node = None

        while node is not None:
            if node.key == key:
                if prev_node is None:
                    self.hash_table[index] = node.next
                else:
                    prev_node.next = node.next
                return
            prev_node = node
            node = node.next

    def display(self):
        for index in range(self.size):
            node = self.hash_table[index]
            while node is not None:
                print(f"Key: {node.key}, Value: {node.value}")
                node = node.next


class ChainingDictionaryWithoutReplacement:
    def __init__(self, size):
        self.size = size
        self.hash_table = [None] * size

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)

        if self.hash_table[index] is None:
            self.hash_table[index] = KeyValueNode(key, value)
        else:
            current_node = self.hash_table[index]
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = KeyValueNode(key, value)

    def find(self, key):
        index = self.hash_function(key)
        node = self.hash_table[index]

        while node is not None:
            if node.key == key:
                return node.value
            node = node.next

        return None

    def delete(self, key):
        index = self.hash_function(key)
        node = self.hash_table[index]
        prev_node = None

        while node is not None:
            if node.key == key:
                if prev_node is None:
                    self.hash_table[index] = node.next
                else:
                    prev_node.next = node.next
                return
            prev_node = node
            node = node.next

    def display(self):
        for index in range(self.size):
            node = self.hash_table[index]
            while node is not None:
                print(f"Key: {node.key}, Value: {node.value}")
                node = node.next


# Testing the ChainingDictionary classes
print("Chaining with Replacement:")
dictionary_with_replacement = ChainingDictionaryWithReplacement(10)

dictionary_with_replacement.insert("apple", 5)
dictionary_with_replacement.insert("banana", 7)
dictionary_with_replacement.insert("cherry", 10)
dictionary_with_replacement.insert("date", 12)
dictionary_with_replacement.insert("banana", 8)  # Replacing value for existing key

dictionary_with_replacement.display()

print("\nSearching for banana....")
print("\nValue for key 'banana':", dictionary_with_replacement.find("banana"))

print("\nDeleting cherry....")
dictionary_with_replacement.delete("cherry")
dictionary_with_replacement.display()


print("---------------------------------------------------")

print("\nChaining without Replacement:")
dictionary_without_replacement = ChainingDictionaryWithoutReplacement(10)

dictionary_without_replacement.insert("apple", 5)
dictionary_without_replacement.insert("banana", 7)
dictionary_without_replacement.insert("cherry", 10)
dictionary_without_replacement.insert("date", 12)

dictionary_without_replacement.display()

print("\nSearching for banana....")
print("\nValue for key 'banana':", dictionary_without_replacement.find("banana"))

print("\nDeleting cherry....")
dictionary_without_replacement.delete("cherry")
dictionary_without_replacement.display()
