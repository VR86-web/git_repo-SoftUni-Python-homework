class custom_range:

    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
        self.start_index = self.start - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start_index >= self.end:
            raise StopIteration

        self.start_index += 1

        return self.start_index


one_to_ten = custom_range(1, 10)
for num in one_to_ten:
    print(num)
