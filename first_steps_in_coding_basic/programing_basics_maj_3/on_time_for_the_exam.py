hour_of_exam = int(input())
minute_of_exam = int(input())
hour_of_arrival = int(input())
minute_of_arrival = int(input())

time_of_exam = hour_of_exam * 60 + minute_of_exam
time_of_arriving = hour_of_arrival * 60 + minute_of_arrival

if time_of_arriving > time_of_exam:
    print("Late")
elif time_of_exam - 30 <= time_of_arriving <= time_of_exam:
    print("On time")
elif time_of_exam - 30 > time_of_arriving:
    print("Early")
difference = abs(time_of_exam - time_of_arriving)
hours = difference // 60
minutes = difference % 60
if time_of_exam - 60 < time_of_arriving < time_of_exam:
    print(f"{minutes} minutes before the start")
elif time_of_arriving <= time_of_exam - 60:
    print(f"{hours}:{minutes:02d} hours before the start")
elif time_of_exam < time_of_arriving < time_of_exam + 60:
    print(f"{minutes} minutes after the start")
elif time_of_arriving >= time_of_exam + 60:
    print(f"{hours}:{minutes:02d} hours after the start")