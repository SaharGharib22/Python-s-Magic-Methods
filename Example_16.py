# Implementing Custom Sequences and Mappings:

class Sequences:
    def __init__(self, items):
        self.items = items

    def __getitem__(self, index):
        return self.items[index]

    def __len__(self):
        return len(self.items)

    def __contains__(self, item):
        return item in self.items

    def __reversed__(self):
        return Sequences(list(reversed(self.items)))


a = Sequences([10, 20, 30, 40])

print(a[1])
print(len(a))
print(30 in a)
print(50 in a)

reversed_sequences = reversed(a)
print(list(reversed_sequences))
