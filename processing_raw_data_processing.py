import pandas as pd

fp = "C:\\Users\\Eleanor.E.Watson\\OneDrive - Shell\\Examples\\Dirty_Up_Clean_Up\\DUCU-example\\ducu-example\\full_data\\raw_data_processed.csv"
fp_processed = "C:\\Users\\Eleanor.E.Watson\\OneDrive - Shell\\Examples\\Dirty_Up_Clean_Up\\DUCU-example\\ducu-example\\full_data\\processed_raw_data_processed.csv"

df = pd.read_csv(fp, index_col=0)
filter_df = df.dropna(axis=0)
print(filter_df)
filter_df.sort_values(by='Response', inplace=True)
filter_df.to_csv(fp_processed)
print(filter_df)

