wanted_high = int(input())
start_jump = wanted_high - 30
failed = False
total_jumps = 0
failed_jumps = 0
while not failed:
    jump_high = int(input())
    total_jumps += 1
    if jump_high <= start_jump:
        failed_jumps += 1
        if failed_jumps == 3:
            failed = True
    else:
        if start_jump >= wanted_high:
            break
        start_jump += 5
        failed_jumps = 0
if not failed:
    print(f"Tihomir succeeded, he jumped over {start_jump}cm after {total_jumps} jumps.")
else:
    print(f"Tihomir failed at {start_jump}cm after {total_jumps} jumps.")

