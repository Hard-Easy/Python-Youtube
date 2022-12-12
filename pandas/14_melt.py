#Code Adhyayana

import pandas as pd

sample_df = pd.read_excel("data\melt_data.xlsx", sheet_name='Sheet1')
col_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep',
	'Oct', 'Nov', 'Dec']

new_df = pd.melt(sample_df, id_vars=['Language','other'], 
                    value_vars=col_list, var_name='month',
                    value_name='views')

new_df.to_excel('data\melt_output.xlsx')