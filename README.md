# scripts

These functions have some additional arguments. I only write the required arguments in the descriptions below.

`utils.py`:

- `get_dates(date_list)`: input: list of dates; 
output: list of tuples of dates (start_of_train_set, start_of_label_buffer_t, start_of_valid_set, start_of_label_buffer_v) representing splits

- `get_splits(df)`: input: df with a date_posted column;
output: list of tuples of dfs (train_df, valid_df) representing splits (This uses the `get_dates` function defined above.)

`metrics.py`:

- `plot_prk_curve(logits, labels)`: input: logits(list of elements in (0,1)), labels (list of elements in {0,1});
output: n/a (generates a png file containing the PR-k curve)