class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.start_idx = - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start_idx == self.count - 1:
            raise StopIteration

        self.start_idx += 1

        return self.start_idx * self.step


numbers = take_skip(10, 5)
for number in numbers:
    print(number)
