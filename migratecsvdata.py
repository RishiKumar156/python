import pandas as ps 

file1 = ps.read_csv('zoho_auths.csv')
file2 = ps.read_csv('zoho_auths1.csv')

merge = file1.merge(file2[['zohoname', 'grn']], on='zohoname', how='inner')

# file1['grn'] = merge['grn']
print(merge.head())
# print(file2.head())