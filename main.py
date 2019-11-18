import sys

max_range = 1000000000
max_number_of_cases = 10

number_of_cases = int(input())
if number_of_cases < 1 or number_of_cases > max_number_of_cases:
    sys.exit(0)

last_number_of_power_to = []
for i in range(0, number_of_cases):
    user_number_to_power = input()
    user_numbers_to_power = user_number_to_power.split()

    if len(user_numbers_to_power) != 2:
        sys.exit(0)

    try:
        user_number = int(user_numbers_to_power[0])
        to_the_power_of = int(user_numbers_to_power[1])
    except ValueError:
        sys.exit(0)
    else:
        if (user_number < 1 or user_number > max_range) or (to_the_power_of < 1 or to_the_power_of > max_range):
            sys.exit(0)
        else:
            last_number_of_power_to.append(str((user_number % 10) ** (4 + (to_the_power_of % 4)))[-1])

for i in last_number_of_power_to:
    print(i)
