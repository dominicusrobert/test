import numpy as np

# Queen's Attack
if __name__ == '__main__':
    result = 0

    # CASE 1
    # total_row_and_column = 8
    # queens_row_position = 4
    # queens_column_position = 4
    # obstacles = {}

    # CASE 2
    total_row_and_column = 5
    queens_row_position = 4
    queens_column_position = 3
    obstacles = {'5 5': 1, '4 2': 1, '2 3': 1}

    queens_position = str(queens_row_position) + " " + str(queens_column_position)

    # to_vertical_top
    for next_row in range(queens_row_position + 1, total_row_and_column+1):
        pointer = str(next_row) + ' ' + str(queens_column_position)
        if pointer in obstacles: break
        else: result += 1

    # to_vertical_btm
    for prev_row in reversed(range(1, queens_row_position)):
        pointer = str(prev_row) + ' ' + str(queens_column_position)
        if pointer in obstacles: break
        else: result += 1

    # to_horizontal_right
    for next_column in range(queens_column_position + 1, total_row_and_column+1):
        pointer = str(queens_row_position) + ' ' + str(next_column)
        if pointer in obstacles: break
        else: result += 1

    # to_horizontal_left
    for prev_column in reversed(range(1, queens_column_position)):
        pointer = str(queens_row_position) + ' ' + str(prev_column)
        if pointer in obstacles: break
        else: result += 1

    # to_right_top: row (+), col (+)
    additional = 0
    for next_column in range(queens_column_position + 1, total_row_and_column):
        additional += 1
        pointer = str(queens_row_position + additional) + ' ' + str(next_column)
        if pointer in obstacles: break
        else: result += 1

    # to_right_btm: row (-), col (+)
    subtraction = 0
    for next_column in range(queens_column_position + 1, total_row_and_column + 1):
        subtraction -= 1
        pointer = str(queens_row_position + subtraction) + ' ' + str(next_column)
        if pointer in obstacles: break
        else: result += 1

    # to_left_top: row (+), col (-)
    additional = 0
    for prev_column in reversed(range(1, queens_column_position)):
        additional += 1
        pointer = str(queens_row_position+additional) + ' ' + str(prev_column)
        if pointer in obstacles: break
        elif queens_row_position + additional > total_row_and_column: break
        else: result += 1

    # to_left_btm: row (-), col (-)
    subtraction = 0
    for prev_column in reversed(range(1, queens_column_position)):
        subtraction -= 1
        pointer = str(queens_row_position+subtraction) + ' ' + str(prev_column)
        if pointer in obstacles: break
        else: result += 1

    print('result', result)

# Fraudulent Activity Notifications
# if __name__ == '__main__':
#     result = 0
#
#     # TEST CASE 1
#     # expenditures = [10,20,30,40,50]
#     # total_data = 5
#     # number_of_trailing_days = 3
#
#     # TEST CASE 2
#     expenditures = [2, 3, 4, 2, 3, 6, 8, 4, 5]
#     total_data = 9
#     number_of_trailing_days = 5
#
#     # TEST CASE 3
#     # expenditures = [1,2,3,4,4]
#     # total_data = 5
#     # number_of_trailing_days = 4
#
#     for idx, expenditure in enumerate(expenditures):
#         if idx < number_of_trailing_days: continue
#         prev_periodical_expenditures = expenditures[(idx - number_of_trailing_days) : idx]
#         prev_median = np.median(prev_periodical_expenditures)
#         if expenditure >= prev_median * 2:
#             result += 1
#
#     print(result)