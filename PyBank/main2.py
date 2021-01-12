import pandas as pd
import csv

file = "Resources/budget_data.csv"
budget_df = pd.read_csv(file)
sum_column = budget_df["col1"] + budget_df["col2"]
budget_df["col3"] = sum_column
print(sum_column)


