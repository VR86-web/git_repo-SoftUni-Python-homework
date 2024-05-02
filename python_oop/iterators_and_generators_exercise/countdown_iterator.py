class countdown_iterator:

    def __init__(self, count):
        self.count = count
        self.start_idx = self.count + 1
        self.end_idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.start_idx == self.end_idx:
            raise StopIteration

        self.start_idx -= 1

        return self.start_idx


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")

