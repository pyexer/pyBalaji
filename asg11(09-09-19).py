#code to convert  sec to hour:minute:seconds

sec=int(input("enter the value:"))
minutes=sec/60
print(minutes,"minutes")
m=int(minutes)
hour=minutes/60
h=int(hour)
s=sec%60

print("{}= {}H : {}M :{}S ".format(sec,h,m,s))
