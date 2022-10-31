from case_fraudulent import \
    check_fraudulent_activity, \
    validate_first_input_fradulent_activity, \
    validate_second_input_fradulent_activity, \
    validate_constraint_fradulent_activity
from case_queens_attack import \
    check_queens_attack, \
    validate_first_input_queens_movement, \
    validate_second_input_queens_movement, \
    validate_third_input_queens_movement


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
    input1 = input("Please insert number of rows and columns in the board & total of obstacles: ")
    is_valid_input1 = validate_first_input_queens_movement(input1)
    if not is_valid_input1: return

    input2 = input("Please insert queen's position (row & column): ")
    is_valid_input2 = validate_second_input_queens_movement(input2)
    if not is_valid_input2: return

    total_row_and_column = int(input1.split(' ')[0])

    queens_row_position = int(input2.split(' ')[0])
    queens_column_position = int(input2.split(' ')[1])

    obstacles = {}

    should_input_obstacles = True
    while(should_input_obstacles):
        input3 = input("Please insert obstacle's position (row & column) *double enter to insert last obstacles: ")
        is_valid_input3 = validate_third_input_queens_movement(input3, input2)
        if not is_valid_input3: return

        if input3 == "": should_input_obstacles = False
        else: obstacles[input3] = 1

    result = check_queens_attack(total_row_and_column, queens_row_position, queens_column_position, obstacles)
    print('Total square(s) that the Queen can attack: ', result)


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
