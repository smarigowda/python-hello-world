from datetime import datetime

start, end = 1, 60

odds_in_a_minute = []
for num in range(start, end + 1):
    if num % 2 != 0:
        odds_in_a_minute.append(num)

print(odds_in_a_minute)

right_this_minute = datetime.today().minute

if right_this_minute in odds_in_a_minute:
    print("This minute seems a little odd")
else:
    print("No an odd minute")
