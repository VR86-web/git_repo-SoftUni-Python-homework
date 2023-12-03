command = input()
exam_results_dict = {}
exam_language = {}
while command != "exam finished":
    exam_data = command.split("-")
    if len(exam_data) == 3:
        username, language, points = exam_data
        points = int(points)
        if username not in exam_results_dict.keys():
            exam_results_dict[username] = points
        else:
            if exam_results_dict[username] <= points:
                exam_results_dict[username] = points
        if language not in exam_language:
            exam_language[language] = 0
        exam_language[language] += 1
    else:
        username = exam_data[0]
        for usernames, current_command in exam_results_dict.items():
            if username not in usernames:
                del exam_results_dict[username]
                break
    command = input()
print("Results:")
for username, points in exam_results_dict.items():
    print(f"{username} | {points}")
print("Submissions:")
for language, submission in exam_language.items():
    print(f"{language} - {submission}")
