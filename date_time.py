import datetime

date = datetime.date(2025,1,2)
print(type(date))

'''get today's date'''

dat_today = datetime.date.today()
print(dat_today,type(dat_today))

time = datetime.time(12,0,35)

print(type(time))

now = datetime.datetime.now()
print(now)

'''
formating time to HH:MM:SS
using built method strftime
'''
now = now.strftime("%H:%M:%S")

print(now)

'''
formating time to HH:MM:SS MM/DD/YYYY
using built method strftime
'''
now = datetime.datetime.now()
now = now.strftime("%H:%M:%S %m/%d/%Y")

print(now)

'''
check whether the date is past 
'''
dat_target = datetime.datetime(2030,12,12,12,0,0)
dat_current = datetime.datetime.now()

if dat_target < dat_current:
    print("Past Date")
else:
    print("Future Date")
