class dictionary_iter:

    def __init__(self, dictionary):
        self.dictionary = list(dictionary.items())
        self.start_idx = - 1
        self.end_idx = len(self.dictionary)

    def __iter__(self):
        return self

    def __next__(self):
        if self.start_idx == self.end_idx - 1:
            raise StopIteration

        self.start_idx += 1

        return self.dictionary[self.start_idx]


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
