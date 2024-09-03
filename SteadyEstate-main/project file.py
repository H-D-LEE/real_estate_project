# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 10:11:40 2024

@author: user
"""

import pandas as pd

# Load the Excel file
file_path = 'C:/Users/user/Documents/python/project_ex/seoul_apt_subway_update.xlsx'
df = pd.read_excel(file_path)

# Function to expand each row based on the 'recentlyTransaction' column
def expand_transactions(row):
    data = row['recentlyTransaction']
    if pd.isna(data):
        return None
    transaction = eval(data)
    rent_list = transaction.get('rentList', [])
    
    # Create a list of rows for each rent transaction
    rows = []
    for rent_transaction in rent_list:
        net_area = rent_transaction.get('netArea', {}).get('m2')
        gross_area = rent_transaction.get('grossArea', {}).get('m2')
        utime = rent_transaction.get('utime')
        floor = rent_transaction.get('floor')
        type_ = rent_transaction.get('type')
        # Append new row with additional columns
        new_row = row.copy()
        new_row['netArea'] = net_area
        new_row['grossArea'] = gross_area
        new_row['utime'] = utime
        new_row['floor'] = floor
        new_row['type'] = type_
        rows.append(new_row)
    
    return pd.DataFrame(rows)

# Apply the function to expand each row
expanded_df = df.apply(expand_transactions, axis=1)

# Concatenate all the expanded dataframes into a single dataframe
expanded_df = pd.concat(expanded_df.tolist(), ignore_index=True)

# Save the expanded DataFrame to a new Excel file
output_file_path = 'C:/Users/user/Documents/python/project_ex/seoul_apt_subway_expanded.xlsx'
expanded_df.to_excel(output_file_path, index=False)

print(f"Expanded DataFrame saved to {output_file_path}")