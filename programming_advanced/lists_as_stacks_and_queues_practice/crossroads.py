from collections import deque

green_light_duration = int(input())
free_window_duration = int(input())

while True:
    command = input()
    if command == "END":
        break
