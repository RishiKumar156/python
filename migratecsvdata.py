

import pandas as pd

f1 = pd.read_csv('zoho_auths.csv')
f2 = pd.read_csv('zoho_auths1.csv')

# Merge the DataFrames on the 'itemdesc' column
merged_df = f1.merge(f2[['zohoname', 'grn']], on='zohoname', how='inner')

# Replace the column in f1 with the corresponding column from f2
merged_df['grn'] = merged_df['grn']

# Drop the original 'column_to_replace' column
merged_df.drop(columns=['grn'], inplace=True)

# Save the modified DataFrame to a new CSV file
merged_df.to_csv('merged_file.csv', index=False)
