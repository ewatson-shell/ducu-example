import pandas as pd
import os
import time
import numpy as np
from functions.cleaning import cleaner # 

csv_dir = r"C:\\Users\\Eleanor.E.Watson\\OneDrive - Shell\\Examples\\Dirty_Up_Clean_Up\\DUCU-example\\ducu-example\\csv_manipulated\\"
csv_files = os.listdir(csv_dir)
full_data_dir = r"C:\\Users\\Eleanor.E.Watson\\OneDrive - Shell\\Examples\\Dirty_Up_Clean_Up\\DUCU-example\\ducu-example\\full_data\\"
full_data = os.listdir(full_data_dir)
full_data_csv = r"C:\\Users\\Eleanor.E.Watson\\OneDrive - Shell\\Examples\\Dirty_Up_Clean_Up\\DUCU-example\\ducu-example\\full_data\\full_data.csv"
pre_filtered_csv = r"C:\\Users\\Eleanor.E.Watson\\OneDrive - Shell\\Examples\\Dirty_Up_Clean_Up\\DUCU-example\\ducu-example\\full_data\\full_data_prefilter.csv"
csv_fp = "C:\\Users\\Eleanor.E.Watson\\OneDrive - Shell\\Examples\\Dirty_Up_Clean_Up\\DUCU-example\\ducu-example\\csv\\"
csv_fp_listdir = os.listdir(csv_fp)

# reading in the raw data csv files.
csv_orig = []
for filename in csv_files:
    df = pd.read_csv(f"{csv_dir}{filename}", index_col=0)
    csv_orig.append(df)

# renaming runtimed column
# remove unneccessary prints

# cleaning the DFs in this case
csv = []
for df in csv_orig: 
    df = df.iloc[2:]
    print(df.head(6))
    print("---------")
    csv.append(df)

for df in csv: 
    try:
       df.rename(columns={'RUNTIMED SECS Unnamed: 1_level_2': 'RUNTIMED'}, inplace=True)
    except:
        None

#############################################################
# why here is rename in white.
for i in csv: 
    print("----------------------------------------------------------------------------------------------------------------------------------------------------")
    print(i.head(6))
    try:
       i.rename(columns={'RUNTIMED SECS Unnamed: 1_level_2': 'RUNTIMED'}, inplace=True)
    except:
        None

# concat as keeping inline process as previous but can update in future.
for df in csv:
    full_df = pd.concat(csv)

# adding the kpa constant column.
df['KPA_Constant'] = 6.89476


# correct these from i and q's should be more clear and readable.
for i in df.columns:
    try:
        df[i] = df[i].astype(float)
    except:
        print(f"{i} cannot be changed")
    q = df[i].dtype
    print(f"{i}, {q})")


# updated from psi to kpa
df['Coolant Pressure Outlet kPA P_COOLOU'] = df['Coolant Pressure Outlet PSI P_COOLOU']*df['KPA_Constant']
df['Supply Fuel pressure kpa P_FUELS'] = df['Supply Fuel pressure  PSI P_FUELS']*df["KPA_Constant"]

# CREATE POWER COLUMN
try:
    df['Power kW'] = df['OBD Engine Speed RPM OBD_RPM']*60*2*np.pi*df['Engine Torque NM TORQUE_1']*(1/60**2)*(1/10**3)
    # CREATE BSFC
    df['BSFC'] = (df['Fuel Flow kg/hr FLOWFUEL']*10**3)/df['Power kW']
except:
    print("could not convert ")

start_len = len(df)

# think what data structure would like to implement to use the cleaner function? 
# check that the TRUES have been eliminated and record how much of those have been eliminated ovcerall. 
# can a tuple be an input to a function? 
