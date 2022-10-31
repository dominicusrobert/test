import numpy as np

# Fraudulent Activity Notifications
if __name__ == '__main__':
    result = 0

    # TEST CASE 1
    # expenditures = [10,20,30,40,50]
    # total_data = 5
    # number_of_trailing_days = 3

    # TEST CASE 2
    expenditures = [2, 3, 4, 2, 3, 6, 8, 4, 5]
    total_data = 9
    number_of_trailing_days = 5

    # TEST CASE 3
    # expenditures = [1,2,3,4,4]
    # total_data = 5
    # number_of_trailing_days = 4

    for idx, expenditure in enumerate(expenditures):
        if idx < number_of_trailing_days: continue
        prev_periodical_expenditures = expenditures[(idx - number_of_trailing_days) : idx]
        prev_median = np.median(prev_periodical_expenditures)
        if expenditure >= prev_median * 2:
            result += 1

    print(result)