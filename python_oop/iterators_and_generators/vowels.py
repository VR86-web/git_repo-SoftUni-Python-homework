class vowels:

    def __init__(self, string):
        self.string = string
        self.vowels = ['a', 'e', 'i', 'o', 'u', 'y']
        self.idx = - 1
        self.vowels_values = [c for c in self.string if c.lower() in self.vowels]

    def __iter__(self):
        return self

    def __next__(self):
        self.idx += 1
        if self.idx < len(self.vowels_values):
            return self.vowels_values[self.idx]

        raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)

