import sys

max_range = 1000000000
max_number_of_cases = 10

number_of_cases = int(input())
if number_of_cases < 1 or number_of_cases > max_number_of_cases:
    sys.exit(0)


def number_to_the_power_of(user_number, to_the_power_of):
    if to_the_power_of == 1:
        return str(user_number)[-1]

    if user_number % 10 == 0:
        return 0

    if str(user_number)[-1] == '4':
        if to_the_power_of % 2 == 0:
            return 6
        else:
            return 4

    if str(user_number)[-1] == '5':
        return 5

    if str(user_number)[-1] == '6':
        return 6

    if str(user_number)[-1] == '9':
        if to_the_power_of % 2 == 0:
            return 1
        else:
            return 9

    if to_the_power_of < 10:
        return int(str(user_number ** to_the_power_of)[-1])

    temp_num = []

    if str(user_number)[-1] == '2':
        temp_num = [4, 8, 6, 2]
    elif str(user_number)[-1] == '3':
        temp_num = [9, 7, 1, 3]
    elif str(user_number)[-1] == '7':
        temp_num = [9, 3, 1, 7]
    elif str(user_number)[-1] == '8':
        temp_num = [4, 2, 6, 8]

    zaleznosc_4 = 1
    for i in range(2, to_the_power_of + 1):
        if i == to_the_power_of:
            if zaleznosc_4 == 1:
                return temp_num[0]
            elif zaleznosc_4 == 2:
                return temp_num[1]
            elif zaleznosc_4 == 3:
                return temp_num[2]
            elif zaleznosc_4 == 4:
                return temp_num[3]

        zaleznosc_4 += 1
        if zaleznosc_4 > 4:
            zaleznosc_4 = 1


last_number_of_power_to = []
for i in range(0, number_of_cases):
    user_number_to_power = input()
    user_numbers_to_power = user_number_to_power.split()
    user_number = int(user_numbers_to_power[0])
    to_the_power_of = int(user_numbers_to_power[1])

    if (user_number < 1 or user_number > max_range) or (to_the_power_of < 1 or to_the_power_of > max_range):
        sys.exit(0)
    else:
        last_number_of_power_to.append(number_to_the_power_of(user_number, to_the_power_of))

for i in last_number_of_power_to:
    print(i)
