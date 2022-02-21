today = "Monday"
today = "Sunday"
# today = "Saturday"
condition = "Headache"

if today == "Saturday":
    print("Party")
elif today == "Sunday":
    if condition == "Headache":
        print("Rest and Recover")
    else:
        print("Recover")
else:
    print("Work...work...work...")