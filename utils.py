from datetime import datetime
from bisect import bisect_left

def get_dates(date_list, verbose=True):
    dates_sorted = sorted(date_list)

    label_buffer = 4        # months
    train_size = 12         # months
    validation_size = 1     # months
    train_valid_gap = 3     # months

    date_format = '%Y-%m-%d'
    curr_date = datetime.strptime(dates_sorted[-1], date_format)
    start_date = datetime.strptime(dates_sorted[0], date_format)
    fold_idx = 0
    return_dates = []

    while True:
        # start of label buffer (validation)
        start_of_label_buffer_v = curr_date - pd.DateOffset(months=label_buffer)

        print(start_of_label_buffer_v)
        # start of validation set
        start_of_validation_set = start_of_label_buffer_v - pd.DateOffset(months=validation_size)

        # start of labe buffer (train)
        start_of_label_buffer_t = start_of_validation_set - pd.DateOffset(months=label_buffer)

        # start of train set
        start_of_train_set = start_of_label_buffer_t - pd.DateOffset(months=train_size)

        curr_date = curr_date - pd.DateOffset(months=train_valid_gap)
        fold_idx+=1

        if start_of_train_set < start_date:
            break
        
        if verbose:
            print("Current fold:", fold_idx)
            print("Start of train set:", start_of_train_set)
            print("Start of label buffer (train):", start_of_label_buffer_t)
            print("Start of validation set:", start_of_validation_set)
            print("Start of label buffer (validation):", start_of_label_buffer_v)
            print(f"Num train: {bisect_left(dates_sorted, str(start_of_label_buffer_t)[:10]) - bisect_left(dates_sorted, str(start_of_train_set)[:10])}")
            print(f"Num valid: {bisect_left(dates_sorted, str(start_of_label_buffer_v)[:10]) - bisect_left(dates_sorted, str(start_of_validation_set)[:10])}")
            print()
        return_dates.append((str(start_of_train_set)[:10], str(start_of_label_buffer_t)[:10], str(start_of_validation_set)[:10], str(start_of_label_buffer_v)[:10]))

    return return_dates  