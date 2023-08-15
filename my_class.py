# Create a class that can be called to fix the formatting of the csv in this dir (sample.csv) and return it as a df. 
# BONUS: Return the data grouped in the best manner you see fit.

import pandas as pd

class CSVFormatter:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_csv_and_fix_formatting(self):
        try:
            df = pd.read_csv(self.file_path)
            # Additional formatting fixes can be added here
            df.columns = df.columns.str.strip()
            return df
        except Exception as e:
            print(f"An error occurred while reading and formatting the CSV: {e}")
            return None

    def group_data(self, df, group_by_column):
        try:
            grouped_data = df.groupby(group_by_column).sum(numeric_only=True)
            return grouped_data
        except Exception as e:
            print(f"An error occurred while grouping data: {e}")
            return None

if __name__ == "__main__":
    csv_file_path = "sample.csv"
    
    csv_formatter = CSVFormatter(csv_file_path)
    
    formatted_df = csv_formatter.read_csv_and_fix_formatting()
    if formatted_df is not None:
        print("Formatted DataFrame:")
        print(formatted_df)
        
        group_column = 'Profit'
        grouped_data = csv_formatter.group_data(formatted_df, group_column)
        if grouped_data is not None:
            print("\nGrouped Data:")
            print(grouped_data)
