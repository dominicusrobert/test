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
