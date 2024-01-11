contest_dict = {}
while True:
    data = input()
    if data == "end of contests":
        break
    contest, password_for_contest = data.split(":")
    if contest not in contest_dict:
        contest_dict[contest] = password_for_contest
submission_dict = {}
while True:
    submission_data = input()
    if submission_data == "end of submissions":
        break
    contest, current_password, username, points = submission_data.split("=>")
    points = int(points)
    if contest in contest_dict and contest_dict[contest] == current_password:
        if username not in submission_dict:
            submission_dict[username] = {contest: points}
        if contest in submission_dict[username]:
            if submission_dict[username][contest] < points:
                submission_dict[username][contest] = points
        else:
            submission_dict[username][contest] = points

sorted_submission_dict = {u: c for u, c in (sorted(submission_dict.items()))}
for key, value in sorted_submission_dict.items():
    sorted_points = {k: p for k, p in sorted(value.items(), key=lambda x: -x[1])}
    sorted_submission_dict[key] = sorted_points

max_points = 0
best_candidate = ""

for key, value in sorted_submission_dict.items():
    current_points = 0
    for u, v in value.items():
        current_points += v
    if current_points > max_points:
        max_points = current_points
        best_candidate = key
print(f"Best candidate is {best_candidate} with total {max_points} points.")
print("Ranking:")
for key, value in sorted_submission_dict.items():
    print(key)
    for u, v in value.items():
        print(f"#  {u} -> {v}")

