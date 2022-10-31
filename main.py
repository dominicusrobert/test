from case_fraudulent import \
    check_fraudulent_activity, \
    validate_first_input_fradulent_activity, \
    validate_second_input_fradulent_activity, \
    validate_constraint_fradulent_activity
from case_queens_attack import check_queens_attack


def handle_case_fraudulent():
    input1 = input("Please insert expenditure size & number of trailing days: ")
    is_valid_input1 = validate_first_input_fradulent_activity(input1)
    if not is_valid_input1: return

    input2 = input("Please insert expenditure: ")
    is_valid_input2 = validate_second_input_fradulent_activity(input2)
    if not is_valid_input2: return

    total_data = int(input1.split(' ')[0])
    number_of_trailing_days = int(input1.split(' ')[1])
    expenditures = list(map(int, input2.split(', ')))

    is_valid_constraint = validate_constraint_fradulent_activity(total_data, number_of_trailing_days, expenditures)
    if not is_valid_constraint: return

    result = check_fraudulent_activity(number_of_trailing_days, expenditures)
    print('Fraudulent Activity that will be notified: ', result)


def handle_case_queens_attack():
    total_row_and_column = 5
    queens_row_position = 4
    queens_column_position = 3
    obstacles = {'5 5': 1, '4 2': 1, '2 3': 1}

    result = check_queens_attack(total_row_and_column, queens_row_position, queens_column_position, obstacles)
    print(result)


if __name__ == '__main__':
    print('Please select test case: ')
    print('1. Fraudulent Activity Notifications')
    print('2. Queen\'s Attack')
    test_case_selection = input("Your selection: ")

    if test_case_selection == '1':
        handle_case_fraudulent()
    elif test_case_selection == '2':
        handle_case_queens_attack()
    else:
        print('Input is not valid')
