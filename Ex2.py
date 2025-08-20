a = int(input('Please give a year: '))

leap = False

if a % 4 == 0:
    leap = True

if a % 100 == 0:
    leap = False

if a % 400 == 0:
    leap = True

print(leap)

year = int(input('Please give a year: '))

if year % 4 ==0 and (year % 100 != 0 or year % 400 == 0):
    year = True
else:
    year = False

print(year)