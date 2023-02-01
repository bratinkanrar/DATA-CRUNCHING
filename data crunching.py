import os
import pandas as pd

data_file_folder='.\data'

df =[]

for file in os.listdir(data_file_folder):
	if file.endswith('.tsv'):
		print('Loading file {0}..' .format(file))
		df.append(pd.read_table(os.path.join(data_file_folder,file)))
df_master= pd.concat(df,axis=0)
df_master.to_table('output.tsv',index=False)


