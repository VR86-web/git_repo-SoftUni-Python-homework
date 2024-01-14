from collections import deque

numbers = deque(input().split())
numbers.reverse()
print(*numbers)