while not (1 <= (weekday := int(input('Please give day of week (1-7): '))) <= 7):
    print('Please provide valid day')

while (vacation := input('Please tell if James is on vacation (yes/no): ')) != 'yes' and vacation != 'no':
    print('Please provide valid response (yes/no)')

sleeps_late = weekday == 6 or weekday == 7 or vacation == 'yes'
print(sleeps_late)