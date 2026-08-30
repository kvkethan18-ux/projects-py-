userName = input("type your name:")
Mood = int(input("Enter your mood out of 10:"))
energyLevel = int(input("Enter your energy level out of 10:"))

if Mood > 7:
    print("Good! Looks like you are good to go today!")
elif Mood >= 5:
    print("You're kinda down today.")
else:
    print("You seem pretty low today. Take some time to relax.")

if energyLevel > 7:
    print("your hyped up")
elif energyLevel >= 5:
    print("get back your energy")
else :print("drink some coffee for energy")

import datetime
import calendar

now = datetime.datetime.now()
print("userName", userName)
print("Time now", now)

print(calendar.calendar(now.year))