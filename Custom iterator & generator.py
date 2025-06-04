class SuperIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end
    def __iter__(self):
        return self
    def __next__(self):
        if self.current < self.end:
            value = self.current ** 2
            self.current += 1
            return value
        else:
            raise StopIteration
class SuperGenerator:
    def square_generator(start, end):
        for num in range(start, end + 1):
            yield num ** 2

print("Using SuperIterator:")
for a in SuperIterator(1, 10):
    print(a)

print("\nUsing SuperGenerator:")
for b in SuperGenerator.square_generator(1, 10):
    print(b)