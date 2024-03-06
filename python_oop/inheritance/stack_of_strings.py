from typing import List


class Stack:

    def __init__(self):
        self.data: List = []

    def push(self, element: str) -> None:
        self.data.append(element)

    def pop(self) -> None:
        return self.data.pop()

    def top(self) -> None:
        return self.data[-1]

    def is_empty(self):
        return False if self.data else True

    def __str__(self):
        reversed_data = reversed(self.data)
        result = ", ".join(reversed_data)
        return f"[{result}]"
