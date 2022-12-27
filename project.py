#CLOCK ANGLE PROBLEM 
#CLOCK ANGLE PROBLEM: given time in hh:mm format in 24-hour notation, 
# calculate the shorter angle between the hour and minute hand in an analog clock
def clockangle(hour, minutes):
  if 00 <= hour <= 24 and 00 <= minutes <= 60:
    #1
    if hour > 12:
      hour = hour - 12
    #2
    if minutes == 60:
      hour = hour + 1
      minutes = 00
    #calculating the angle
    hour = hour + minutes / 60
    handiff = abs(hour - minutes / 5)
    preangle = handiff * 30
    reflexangle = min(preangle, 360 - preangle)
    return reflexangle
  else:
    print("Enter a correct time.")
    pass

print("Give a time in hh:mm format in 24 hour notation")
reflexangle=clockangle(int(input("Hour: ")), int(input("Minutes: ")))
angle=format(reflexangle,".2f")
print("\nThe difference between the hour and the minute hand is", angle + "degrees")

#there are three test cases in this question:
#1. the time is taken in 24hrs format so conversion also took place
#2. the minute may taken at 60 so converision to next