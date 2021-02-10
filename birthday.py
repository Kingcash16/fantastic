#Joshua Jaja ID:1543343 Coding Problem 1:
month1 = int(input('Month:'))
day1 = int(input('day'))
year1 = int(input('year'))
print('Birthday')
month2 = int(input('Month:'))
Day2 = int(input('Day:'))
Year2 = int(input('Year:'))
years = year1-Year2-1
if(month1<month2):
    years+=1
elif(month2==month1):
    if (Day2<day1):
        years+=2
if(month2==month1 and day1==Day2):
    print('Happy Birthday')
print('You are '+str(years)+"years old.")

