# 1 
while (shining := input('Is the sun shining ? (yes/no): ')) != 'yes' and shining != 'no':
    print('Please provide valid response (yes/no)')

while (time := int(input('Please give time in number (0-23): '))) < 0 or time > 23:
    print('Please provide valid time (0-23)')

response = shining == 'yes' and (10 <= time <= 16)
print(response)

# 2
while (a := int(input('Please give positive inteteger a: '))) <= 0:
    print('Please provide valid positive integer')

while (b := int(input('Please give positive integer b: '))) <= 0:
    print('Please provide valid positive integer')

same_last_digit = (a % 10) == (b % 10)
print(same_last_digit)

# 3
while (s := int(input('Please give a positive integer s: '))) <= 0:
    print('Please provide valid positive integer')

n = 0


while n ** 3 - 10 * n ** 2 < s:
    n += 1

print(n, n ** 3 - 10 * n ** 2)
