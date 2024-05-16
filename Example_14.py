# Supporting Iteration With Iterators and Iterable:

# Creating Iterators:
class Range:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.end:
            raise StopIteration
        current_value = self.start
        self.start += 1
        return current_value


my_range = Range(1, 6)
print("Iterator:")
while True:
    try:
        num = next(my_range)
        print(num)
    except StopIteration:
        break


# Building Iterables:
class Range:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return iter(self.data)


a = Range([1, 2, 3, 4, 5])
print("Iterable:")

for item in a:
    print(item)
