import math

series_name = input()
series_lenght = int(input())
break_time = int(input())

lunch_time = break_time * 0.125
down_time = break_time * 0.25
time_used = lunch_time + down_time
time_left = break_time - time_used

time_abs = abs(time_left - series_lenght)
time_round = math.ceil(time_abs)

if time_left > series_lenght:
    print(
        f"You have enough time to watch {series_name} and left with {time_round} minutes free time."
    )

else:
    print(
        f"You don't have enough time to watch {series_name}, you need {time_round} more minutes."
    )
