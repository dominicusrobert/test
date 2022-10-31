
def validate_first_input_queens_movement(input1):
    if ' ' not in input1:
        print('[ERROR] First input is not valid')
        print('Please insert the valid format, example: \'5 3\'')
        return False

    arr_input_1 = input1.split(' ')
    total_row_and_column = arr_input_1[0]
    total_obstacles = arr_input_1[1]

    if not total_row_and_column.isnumeric():
        print('[ERROR] First input number row and column is not a number')
        print('Please insert the valid format, example: \'5 3\'')
        return False

    if not total_obstacles.isnumeric():
        print('[ERROR] First input total obstacles is not a number')
        print('Please insert the valid format, example: \'5 3\'')
        return False

    if int(total_row_and_column) < 1 or int(total_row_and_column) > 10**5:
        print('[ERROR] First input number row and column exceed the constraint')
        print('The value should be more than equal 1 & less than 10^5')
        return False

    if int(total_obstacles) < 0 or int(total_obstacles) > 10**5:
        print('[ERROR] First input total obstacles exceed the constraints')
        print('The value should be more than equal 0 & less than 10^5')
        return False

    return True


def validate_second_input_queens_movement(input2):
    if ' ' not in input2:
        print('[ERROR] Second input is not valid')
        print('Please insert the valid format, example: \'4 3\'')
        return False

    arr_input_2 = input2.split(' ')
    queens_row_position = arr_input_2[0]
    queens_column_position = arr_input_2[1]

    if not queens_row_position.isnumeric():
        print('[ERROR] Second input queens\'s row position is not a number')
        print('Please insert the valid format, example: \'4 3\'')
        return False

    if not queens_column_position.isnumeric():
        print('[ERROR] Second input queens\'s column position is not a number')
        print('Please insert the valid format, example: \'4 3\'')
        return False

    return True


def validate_third_input_queens_movement(input3, queens_position):
    if input3 == "": return True

    if ' ' not in input3:
        print('[ERROR] Third input is not valid')
        print('Please insert the valid format, example: \'5 5\'')
        return False

    arr_input_2 = input3.split(' ')
    obstacle_row_position = arr_input_2[0]
    obstacle_column_position = arr_input_2[1]

    if input3 == queens_position:
        print('[ERROR] Third input obstacle\'s position is equal to Queen\'s position')
        return False

    if not obstacle_row_position.isnumeric():
        print('[ERROR] Third input obstacle\'s row position is not a number')
        print('Please insert the valid format, example: \'5 5\'')
        return False

    if not obstacle_column_position.isnumeric():
        print('[ERROR] Third input obstacle\'s column position is not a number')
        print('Please insert the valid format, example: \'5 5\'')
        return False

    return True


def check_queens_attack(total_row_and_column, queens_row_position, queens_column_position, obstacles):
    result = 0

    # to_vertical_top
    for next_row in range(queens_row_position + 1, total_row_and_column + 1):
        pointer = str(next_row) + ' ' + str(queens_column_position)
        if pointer in obstacles:
            break
        else:
            result += 1

    # to_vertical_btm
    for prev_row in reversed(range(1, queens_row_position)):
        pointer = str(prev_row) + ' ' + str(queens_column_position)
        if pointer in obstacles:
            break
        else:
            result += 1

    # to_horizontal_right
    for next_column in range(queens_column_position + 1, total_row_and_column + 1):
        pointer = str(queens_row_position) + ' ' + str(next_column)
        if pointer in obstacles:
            break
        else:
            result += 1

    # to_horizontal_left
    for prev_column in reversed(range(1, queens_column_position)):
        pointer = str(queens_row_position) + ' ' + str(prev_column)
        if pointer in obstacles:
            break
        else:
            result += 1

    # to_right_top: row (+), col (+)
    additional = 0
    for next_column in range(queens_column_position + 1, total_row_and_column):
        additional += 1
        pointer = str(queens_row_position + additional) + ' ' + str(next_column)
        if pointer in obstacles:
            break
        else:
            result += 1

    # to_right_btm: row (-), col (+)
    subtraction = 0
    for next_column in range(queens_column_position + 1, total_row_and_column + 1):
        subtraction -= 1
        pointer = str(queens_row_position + subtraction) + ' ' + str(next_column)
        if pointer in obstacles:
            break
        else:
            result += 1

    # to_left_top: row (+), col (-)
    additional = 0
    for prev_column in reversed(range(1, queens_column_position)):
        additional += 1
        pointer = str(queens_row_position + additional) + ' ' + str(prev_column)
        if pointer in obstacles:
            break
        elif queens_row_position + additional > total_row_and_column:
            break
        else:
            result += 1

    # to_left_btm: row (-), col (-)
    subtraction = 0
    for prev_column in reversed(range(1, queens_column_position)):
        subtraction -= 1
        pointer = str(queens_row_position + subtraction) + ' ' + str(prev_column)
        if pointer in obstacles:
            break
        else:
            result += 1

    return result
