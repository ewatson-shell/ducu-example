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
raw_processed_csvs = r"C:\\Users\\Eleanor.E.Watson\\OneDrive - Shell\\Examples\\Ducu-git\\data\\raw_to_csv\\"
raw_processed_csvs_ls = os.listdir(raw_processed_csvs)
raw_csv_processed_fp = r"C:\\Users\\Eleanor.E.Watson\\OneDrive - Shell\\Examples\\Ducu-git\\data\\raw_to_csv_processed\\"
files_to_plot_ls = []
for file in raw_processed_csvs_ls:
    df = pd.read_csv(f"{raw_processed_csvs}{file}", index_col=0)
    df = df.iloc[1:]
    files_to_plot_ls.append(df)

for df in files_to_plot_ls: # torque is a float. # check that type also # uderstand why float can't be in this multiplication
    df['KPA_Constant'] = 6.89476 
    # conversions
    df['Coolant Pressure Outlet kPA P_COOLOU'] = df['KPA_Constant']*df['Coolant Pressure Outlet PSI P_COOLOU']
    df['Supply Fuel pressure kpa P_FUELS'] = df['KPA_Constant']*df['Supply Fuel pressure  PSI P_FUELS']
    mask = (df['Engine speed RPM SPEED'] != 'True')
    df = df[mask]
    mask = (df['Engine Torque NM TORQUE_1'] != 'True')
    df = df[mask]
    mask = (df['Fuel Flow kg/hr FLOWFUEL'] != 'True')
    df = df[mask]
    df['Engine speed RPM SPEED'] = pd.to_numeric(df['Engine speed RPM SPEED'])
    df['Engine Torque NM TORQUE_1'] = pd.to_numeric(df['Engine Torque NM TORQUE_1'])
    df['Fuel Flow kg/hr FLOWFUEL'] = pd.to_numeric(df['Fuel Flow kg/hr FLOWFUEL'])
    try:
        df['Power kW'] = df['Engine speed RPM SPEED']*np.float64(60)*np.float64(2.0)*np.float64(np.pi)*df['Engine Torque NM TORQUE_1']*(np.float64(1)/np.float64(60)**np.float64(2))*np.float64((1)/np.float64(10)**np.float64(3))
        df['BSFC'] = (df['Fuel Flow kg/hr FLOWFUEL']*10**3)/df['Power kW']
    except:
        print("could not convert ")
    filename = df['Filename'][5]
    df.to_csv(f"{raw_csv_processed_fp}{filename}.csv")