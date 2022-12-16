import sklearn 
import pandas as pd
import scipy
import datetime as dt 
from scipy import stats 
import plotly.express as px
import os
fp = r"C:\\Users\\Eleanor.E.Watson\\OneDrive - Shell\\Examples\\Ducu-git\\data\\csv_processed_cleaned_final\\"

# csv = "original_raw_data_processed.csv"
csv = "injector_pulse_width.csv"
df = pd.read_csv(fp+csv)

df = df.dropna()


#df = df.sort_values(by = ['Response', 'Fuel'])
grouped = df.groupby(df.Response)
BSFC_df = grouped.get_group("BSFC")
LTFT_df = grouped.get_group("OBD Long Term Fuel Trim Shift  % OBD_LTFT")
Power_df = grouped.get_group("Power kW")
Torque_df = grouped.get_group("Engine Torque NM TORQUE_1")
Fuel_Flow_df = grouped.get_group("Fuel Flow kg/hr FLOWFUEL")
BSFC_df.to_csv(fp+"BSFC.csv")
LTFT_df.to_csv(fp+"LTFC.csv")
Power_df.to_csv(fp+"Power.csv")
Torque_df.to_csv(fp+"Torque.csv")
Fuel_Flow_df.to_csv(fp+"Fuel_Flow.csv")