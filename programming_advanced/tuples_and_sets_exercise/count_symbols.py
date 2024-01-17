occurrences = {}

for symbol in input():
    occurrences[symbol] = occurrences.get(symbol, 0) + 1

for symbol, times in sorted(occurrences.items()):
    print(f"{symbol}: {times} time/s")

# second version
# text = input()

#for symbol in sorted(set(text)):
#    print(f"{symbol}: {text.count(symbol)} time/s")