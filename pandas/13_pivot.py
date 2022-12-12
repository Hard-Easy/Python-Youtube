#Code Adhyayana
import pandas as pd
import numpy as np

sample_df = pd.read_excel('data\melt_output.xlsx', sheet_name='Sheet1')

print(sample_df.head(7))

#print(sample_df.pivot(index=['Language','other'], columns='month', 
#                      values='view'))

table = pd.pivot_table(sample_df, index=['Language','other'], 
            columns=['month'], values='views', aggfunc=np.sum)

table.to_excel('data\pivot_output.xlsx')