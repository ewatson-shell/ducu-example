import pandas as pd
import os

raw_data_dir = r"C:\\Users\\Eleanor.E.Watson\\OneDrive - Shell\\Examples\\Ducu-git\\data\\raw\\"
raw_data_ls = os.listdir(raw_data_dir)

# TODO
# need to add block and fuel column, run and filename
# somewhere along road lost that piece of code - rewrite.
raw_data_dfs = []
for file in raw_data_ls:
    os.chdir(raw_data_dir)
    df = pd.read_excel(file, sheet_name='Data Collection')
    raw_data_dfs.append(df)

for df in raw_data_dfs:
    print(df.head(10))
