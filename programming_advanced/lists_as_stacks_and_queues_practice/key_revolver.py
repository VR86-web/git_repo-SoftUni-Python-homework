from collections import deque

bullet_price = int(input())
mag_max = int(input())

bullets = deque([int(b) for b in input().split()])
locks = deque([int(l) for l in input().split()])

reward = int(input())

bullets_in_mag = mag_max
bullets_shot = 0

while bullets and locks:
    bullet = bullets.pop()
    lock = locks.popleft()

    if bullet <= lock:
        print("Bang!")
    else:
        print("Ping!")
        locks.appendleft(lock)

    bullets_in_mag -= 1
    bullets_shot += 1

    if bullets_in_mag == 0 and bullets:
        bullets_in_mag = mag_max if len(bullets) >= mag_max else len(bullets)
        print("Reloading!")

if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    earned_money = abs(bullet_price * bullets_shot - reward)
    print(f"{len(bullets)} bullets left. Earned ${earned_money}")

