a = int(input('Please give a year: '))

leap = False

if a % 4 == 0:
    leap = True

if a % 100 == 0:
    leap = False

if a % 400 == 0:
    leap = True

print(leap)
 #test