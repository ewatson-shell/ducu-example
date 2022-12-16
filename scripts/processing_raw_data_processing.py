import pandas as pd

fp = r"C:\\Users\\Eleanor.E.Watson\\OneDrive - Shell\\Examples\\Ducu-git\\data\\csv_processed_cleaned_final\\final.csv"
fp_processed = r"C:\\Users\\Eleanor.E.Watson\\OneDrive - Shell\\Examples\\Ducu-git\\data\\csv_processed_cleaned_final\\final_sorted.csv"
df = pd.read_csv(fp, index_col=0)
filter_df = df.dropna(axis=0)
print(filter_df)
filter_df.sort_values(by='Response', inplace=True)
filter_df.to_csv(fp_processed)
print(filter_df)


