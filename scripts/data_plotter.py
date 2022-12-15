import pandas as pd
import os
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
import time
import numpy as np

#temporariliy commenting this out so that can see if it works for just one df.

# inputting the raw files
raw_processed_csvs = r"C:\\Users\\Eleanor.E.Watson\\OneDrive - Shell\\Examples\\Ducu-git\\data\\raw_to_csv_processed\\"
#raw_processed_csvs = r"C:\\Users\\Eleanor.E.Watson\\OneDrive - Shell\\Examples\\Ducu-git\\data\\csv_processed_filtered\\"
#raw_processed_csvs = r"C:\\Users\\Eleanor.E.Watson\\OneDrive - Shell\\Examples\\Ducu-git\\data\\csv_processed_cleaned_final\\"
raw_processed_csvs_ls = os.listdir(raw_processed_csvs)
files_to_plot_ls = []
for file in raw_processed_csvs_ls:
    df = pd.read_csv(f"{raw_processed_csvs}{file}", index_col=0)
    df = df.iloc[1:]
    files_to_plot_ls.append(df)

#plotting.
graph_fp = r"C:\\Users\\Eleanor.E.Watson\\OneDrive - Shell\\Examples\\Ducu-git\\graphs\\pre\\"
graph_fp = r"C:\\Users\\Eleanor.E.Watson\\OneDrive - Shell\\Examples\\Ducu-git\\graphs\\mid\\"
graph_fp = r"C:\\Users\\Eleanor.E.Watson\\OneDrive - Shell\\Examples\\Ducu-git\\graphs\\post\\"
relevant_cols = ['Coolant Pressure Outlet PSI P_COOLOU', 'Intake Air Pressure KPAG P_INAIR','Intake Air Temp °C T_INAIR','Fuel Flow kg/hr FLOWFUEL', 'Engine speed RPM SPEED','Intake Humidity g/kg HUM75','Post Inter Cooler Air Temp °C T_CHGOUT', 'Engine Torque NM TORQUE_1','Exhaust Pressure after Turbo kpa P_EXHABS','Injector Pulse width mS OBD_INJ', 'BSFC', 'Power'] 

import datetime as dt 
df['time_list'] = df['RUNTIMED'].apply(lambda x : x.strip(" ").split('.')[0].split(":"))
df['seconds'] = df['time_list'].apply(lambda x : dt.timedelta(hours=int(x[0]), minutes=int(x[1]), seconds=int(x[2])).total_seconds())
df['seconds'] = df['seconds'].astype(int)

print(df['seconds'])
for df, filename in zip(files_to_plot_ls, raw_processed_csvs_ls ):
    df['time_list'] = df['RUNTIMED'].apply(lambda x : x.strip(" ").split('.')[0].split(":"))
    df['seconds'] = df['time_list'].apply(lambda x : dt.timedelta(hours=int(x[0]), minutes=int(x[1]), seconds=int(x[2])).total_seconds())
    df['seconds'] = df['seconds'].astype(int)
    filename = df['Filename'].values[3]
    for col in relevant_cols:
    #print(df.plot.scatter(x= 'RUNTIMED', y = 'Coolant Pressure Outlet PSI P_COOLOU'))
        try:
            print(col)
            print(df.head())
            print(df.columns)
            x = df['seconds']
            y = df[col]
            df.plot(x='seconds', y=col)
            plt.scatter(x,y)
            plt.xlabel("Seconds")
            plt.ylabel(col)
            time.sleep(5)
         #   plt.show()
            plt.savefig(f"{graph_fp}\\{filename}_{col}.png", transparent=True)
        except Exception as e:
            print(e)









