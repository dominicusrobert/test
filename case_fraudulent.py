import numpy as np


def validate_first_input_fradulent_activity(input1):
    if ' ' not in input1:
        print('[ERROR] First input is not valid')
        print('Please insert the valid format, example: \'9 5\'')
        return False

    arr_input_1 = input1.split(' ')
    total_data = arr_input_1[0]
    number_of_trailing_days = arr_input_1[1]

    if not total_data.isnumeric():
        print('[ERROR] First input total data is not a number')
        print('Please insert the valid format, example: \'9 5\'')
        return False

    if not number_of_trailing_days.isnumeric():
        print('[ERROR] First input trailing days is not a number')
        print('Please insert the valid format, example: \'9 5\'')
        return False

    return True


def validate_second_input_fradulent_activity(input2):
    if ' ' not in input2:
        print('[ERROR] Second input is not valid')
        print('Please insert the valid format, example: \'2 3 4 2 3 6 8 4 5\'')
        return False

    arr_input_2 = input2.split(' ')
    for expenditure in arr_input_2:
        if not expenditure.isnumeric():
            print('[ERROR] Expenditure component is not a number')
            return False

    return True


def validate_constraint_fradulent_activity(total_data, number_of_trailing_days, expenditures):
    if total_data < 1 or total_data > 10 ** 5:
        print('[ERROR] Total data exceed the constraint')
        return False

    if number_of_trailing_days < 1 or number_of_trailing_days > total_data:
        print('[ERROR] Number of trailing days exceed the constraint')
        return False

    for expenditure in expenditures:
        if expenditure < 0 or expenditure > 200:
            print('[ERROR] Expenditure component exceed the constraint')
            return False

    return True


def check_fraudulent_activity(number_of_trailing_days, expenditures):
    result = 0

    for idx, expenditure in enumerate(expenditures):
        if idx < number_of_trailing_days: continue
        prev_periodical_expenditures = expenditures[(idx - number_of_trailing_days): idx]
        prev_median = np.median(prev_periodical_expenditures)
        if int(expenditure) >= prev_median * 2:
            result += 1

    return result
