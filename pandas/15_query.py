#Code Adhyayana

import pandas as pd

sample_df = pd.read_excel('data\melt_output.xlsx', sheet_name='Sheet1')

print(sample_df.head())

print(sample_df.query('Language=="Python"'))
#print(sample_df.query('Language=="Python" | Language=="Java"'))
#print(sample_df.query("Language=='Python' & month=='Jan'"))