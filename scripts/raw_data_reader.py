import pandas as pd
import os

raw_data_dir = r"C:\\Users\\Eleanor.E.Watson\\OneDrive - Shell\\Examples\\Dirty_Up_Clean_Up\\DUCU-example\\ducu-example\\raw"
raw_data_ls = os.listdir(raw_data_dir)

raw_data_dfs = []
for file in raw_data_ls:
    os.chdir(raw_data_dir)
    df = pd.read_excel(file, sheet_name='Data Collection')
    raw_data_dfs.append(df)

for df in raw_data_dfs:
    print(df.head(10))
