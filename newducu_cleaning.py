<<<<<<< HEAD
#imports
import pandas as pd
import os
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import time

#######################################

raw_data_dir = r"C:\\Users\\Eleanor.E.Watson\\OneDrive - Shell\\Examples\\Dirty_Up_Clean_Up\\DUCU-example\\raw_"
raw_data_files = os.listdir(raw_data_dir)
csv_dir = r"C:\\Users\\Eleanor.E.Watson\\OneDrive - Shell\\Examples\\Dirty_Up_Clean_Up\\DUCU-example\\csv_manipulated\\"
csv_files = os.listdir(csv_dir)
output_folder = r"C:\\Users\\Eleanor.E.Watson\\graphs\\html\\"
graph_html = os.listdir(output_folder)

######################################
csv = []
for i in csv_files:
    df = pd.read(f"{csv_files}{i}")
    csv.append(df)
################
# columns
################

cols = csv[0].columns
for i in cols:
    print(i)

#TODO
#concatenate the files
# identify which to be converted to KPA
# filter

# plot again
# then is the pivot stage 
# then the fitting stage 


# have I done the kPA data manipulation?
# if not in future do at same time as all other data manipulation
=======
#imports
import pandas as pd
import os
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import time
import numpy as np

#######################################

#raw_data_dir = r"C:\\Users\\Eleanor.E.Watson\\OneDrive - Shell\\Examples\\Dirty_Up_Clean_Up\\DUCU-example\\ducu-example\\raw_"
#raw_data_files = os.listdir(raw_data_dir)
csv_dir = r"C:\\Users\\Eleanor.E.Watson\\OneDrive - Shell\\Examples\\Dirty_Up_Clean_Up\\DUCU-example\\ducu-example\\csv_manipulated\\"
csv_files = os.listdir(csv_dir)
graph_output_folder = r"C:\\Users\\Eleanor.E.Watson\\graphs\\html\\"
graph_html = os.listdir(graph_output_folder)
full_data_dir = r"C:\\Users\\Eleanor.E.Watson\\OneDrive - Shell\\Examples\\Dirty_Up_Clean_Up\\DUCU-example\\ducu-example\\full_data\\"
full_data = os.listdir(full_data_dir)
full_data_csv = r"C:\\Users\\Eleanor.E.Watson\\OneDrive - Shell\\Examples\\Dirty_Up_Clean_Up\\DUCU-example\\ducu-example\\full_data\\full_data.csv"
pre_filtered_csv = r"C:\\Users\\Eleanor.E.Watson\\OneDrive - Shell\\Examples\\Dirty_Up_Clean_Up\\DUCU-example\\ducu-example\\full_data\\full_data_prefilter.csv"
csv_fp = "C:\\Users\\Eleanor.E.Watson\\OneDrive - Shell\\Examples\\Dirty_Up_Clean_Up\\DUCU-example\\ducu-example\\csv\\"
csv_fp_listdir = os.listdir(csv_fp)
######################################

csv_orig = []
for filename in csv_files:
    df = pd.read_csv(f"{csv_dir}{filename}", index_col=0)
    csv_orig.append(df)
################
# columns - renaming the runtimed column so it is consistent in all dataframes in CSV dir.
################

############## DEBUGGING #################################
csv = []
for df in csv_orig: 
    df = df.iloc[2:]
    print(df.head(6))
    print("---------")
    csv.append(df)

for i in csv:
    print("----------------------------------------------------------------------------------------------------------------------------------------------------")
    print(i.head(10))
    print("----------------------------------------------------------------------------------------------------------------------------------------------------")
    print(i.dtypes)
    print("----------------------------------------------------------------------------------------------------------------------------------------------------")
    for j in i.columns:
        try:    
            print(df[j].unique())
            print("-----")
        except:
            pass
    print("----------------------------------------------------------------------------------------------------------------------------------------------------")
#############################################################
for i in csv: 
    print("----------------------------------------------------------------------------------------------------------------------------------------------------")
    print(i.head(6))
    try:
       i.rename(columns={'RUNTIMED SECS Unnamed: 1_level_2': 'RUNTIMED'}, inplace=True)
    except:
        None

for i in csv:
    print(i.head(4))
##########################################################

# need to rename the column runtimed in rest of the csvs
# write to a new directory 
# :-)
##########################
# concatenating files
#########################
# have to squish the columns into 1 header before concatenation!
for df in csv:
    full_df = pd.concat(csv)

print(full_df.head(10))

#full_df.to_csv(f"{full_data_dir}full_data.csv")
#print(full_df.head(20))



#TODO
########################################
# converting UNITS
# identify which to be converted to KPA
########################################


## adding the kpa conversion column
#df = pd.read_csv(f"{full_data_dir}full_data.csv", index_col=False)

df['KPA_Constant'] = 6.89476

print(df.head())



for i in df.columns:
    print(i)
    print("-----------------------------")

# check in kpa or convert
#-----------------------------
# check data dict on what these are 
#---------------------------
# inlet airpressure -> P_INAIR (kPa)
# coolant pressure -> P_COOLOU(PSI) (   CONVERT    )
# exhaust backpressure -> P_EXHABS(kPa)
# fuel rail pressure -> P_FUELS(PSI) (   CONVERT    )

# haven't done this yet 
# changing object types to float where possible 
print(df.dtypes)

for j in df.columns:
    try:
        df[j].astype(float)
    except:
        pass
print("==============================")
print(df.dtypes)
print("===========================")
df['Coolant Pressure Outlet PSI P_COOLOU'] = df['Coolant Pressure Outlet PSI P_COOLOU'].astype(float)

for i in df.columns:
    try:
        df[i] = df[i].astype(float)
    except:
        print(f"{i} cannot be changed")
    q = df[i].dtype
    print(f"{i}, {q})")

print("df['Coolant Pressure Outlet PSI P_COOLOU']", df['Coolant Pressure Outlet PSI P_COOLOU'].dtype)
print("df['KPA_Constant']", df['KPA_Constant'].dtype)
print("--------------------------------------------------------------------------------------")

# updated from psi to kpa
df['Coolant Pressure Outlet kPA P_COOLOU'] = df['Coolant Pressure Outlet PSI P_COOLOU']*df['KPA_Constant']
df['Supply Fuel pressure kpa P_FUELS'] = df['Supply Fuel pressure  PSI P_FUELS']*df["KPA_Constant"]

print("Fuel Flow kg/hr FLOWFUEL uniques:")
print(df['Fuel Flow kg/hr FLOWFUEL'].unique())
for i in df['Fuel Flow kg/hr FLOWFUEL'].unique():
    print(i)
    print(type(i))

# TODO ANCORA
# CREATE POWER COLUMN
try:
    df['Power kW'] = df['OBD Engine Speed RPM OBD_RPM']*60*2*np.pi*df['Engine Torque NM TORQUE_1']*(1/60**2)*(1/10**3)
    # CREATE BSFC
    df['BSFC'] = (df['Fuel Flow kg/hr FLOWFUEL']*10**3)/df['Power kW']
except:
    print("could not convert ")

print("------------------------------------------------------------------------------------------------------------")
print(df.head(10))
print("------------------------------------------------------------------------------------------------------------")

#df.to_csv(pre_filtered_csv)

# filter # WHEN FILTERING SHOULD I ALSO CUT OUT THE "NOT RELEVANT COLS" TO MAKE THE DATA EASIER TO HANDLE? I THINK SO 
# AS WILL HAVE THE FULL DF AS BEFORE
# OR CAN FILTER
# THEN CUT OUT IRELLEVANT COLS (Y)
# NEED TO KEEP TRACK OF HOW MANY ROWS HAVE BEEN EXCLUDED 
    # FUTURE output to log file 

#df = pd.read_csv(pre_filtered_csv, index_col = False)
print("----------------")
x = len(df)
print(x)
print("----------------")
print(df.head(10))
print("--------------")


###
### filtering
###

#df = df[[df['Engine speed RPM SPEED'] >= 1990 | df['Engine speed RPM SPEED'] <= 2010]]
df = df[[df['Engine speed RPM SPEED'].ge(1990) | df['Engine speed RPM SPEED'].le(2010)]]
y = len(df)

z = x - y
print("--------------------------------------------------------")
print(f"Number of lines lost after engine speed filter is: {z}")
print("--------------------------------------------------------")

df = df[[df['Engine Torque NM TORQUE_1'] < 103 | df['Engine Torque NM TORQUE_1'] > 97]]
y = len(df)

z = x - y
print("--------------------------------------------------------")
print(f"Number of lines lost after Engine Torque NM TORQUE_1 is: {z}")
print("--------------------------------------------------------")

# will be inlet air pressure here but not currently as haven't done the kPa conversion ! 
# #'Intake Air Pressure KPAG P_INAIR'

df = df[[df['Intake Air Pressure KPAG P_INAIR'] > 0.04 | df['Intake Air Pressure KPAG P_INAIR'] < 0.06]]
y = len(df)

z = x - y
print("--------------------------------------------------------")
print(f"Number of lines lost after Intake Air Pressure KPAG P_INAIR  is: {z}")
print("--------------------------------------------------------")

df = df[[df['Oil Galley Temp °C T_OILGAL'] > 84 | df['Oil Galley Temp °C T_OILGAL'] < 90]]
y = len(df)

z = x - y
print("--------------------------------------------------------")
print(f"Number of lines lost after Oil Galley Temp °C T_OILGAL is: {z}")
print("--------------------------------------------------------")

df = df[[df['Coolant Temp Outlet °C T_COOLOU'] < 83 | df['Coolant Temp Outlet °C T_COOLOU'] > 77]]
y = len(df)

z = x - y
print("--------------------------------------------------------")
print(f"Number of lines lost after Coolant Temp Outlet °C T_COOLOU is: {z}")
print("--------------------------------------------------------")


df = df[[df['Intake Air Temp °C T_INAIR'] < 35 | df['Intake Air Temp °C T_INAIR'] > 29]]
y = len(df)

z = x - y
print("--------------------------------------------------------")
print(f"Number of lines lost after Intake Air Temp °C T_INAIR is: {z}")
print("--------------------------------------------------------")


df = df[[df['Coolant Pressure Outlet PSI P_COOLOU'] < 100 | df['Coolant Pressure Outlet PSI P_COOLOU'] > 80]]
y = len(df)

z = x - y
print("--------------------------------------------------------")
print(f"Number of lines lost after Coolant Pressure Outlet PSI P_COOLOU is: {z}")
print("--------------------------------------------------------")


df = df[[df['Fuel Temp °C T_FUELS'] < 33 | df['Fuel Temp °C T_FUELS'] > 27]]
y = len(df)

z = x - y
print("--------------------------------------------------------")
print(f"Number of lines lost after Fuel Temp °C T_FUELS is: {z}")
print("--------------------------------------------------------")

df = df[[df['Post Inter Cooler Air Temp °C T_CHGOUT'] < 38 | df['Post Inter Cooler Air Temp °C T_CHGOUT'] > 32]]
y = len(df)

z = x - y
print("--------------------------------------------------------")
print(f"Number of lines lost after Post Inter Cooler Air Temp °C T_CHGOUT is: {z}")
print("--------------------------------------------------------")

df = df[[df['Exhaust Pressure after Turbo kpa P_EXHABS'] < 103 | df['Exhaust Pressure after Turbo kpa P_EXHABS'] > 101]]
y = len(df)
z = x - y
print("--------------------------------------------------------")
print(f"Number of lines lost after Exhaust Pressure after Turbo kpa P_EXHABS is: {z}")
print("--------------------------------------------------------")

# would be p fuels here 'Supply Fuel pressure  PSI P_FUELS'

df = df[[df['Supply Fuel pressure  PSI P_FUELS'] < 103 | df['Supply Fuel pressure  PSI P_FUELS'] > 101]]
y = len(df)
z = x - y
print("--------------------------------------------------------")
print(f"Number of lines lost after Supply Fuel pressure  PSI P_FUELS is: {z}")
print("--------------------------------------------------------")

df = df[[df['Intake Humidity g/kg HUM75'] < 12.4 | df['Intake Humidity g/kg HUM75'] > 11.4]]
y = len(df)
z = x - y
print("--------------------------------------------------------")
print(f"Number of lines lost after Intake Humidity g/kg HUM75 is: {z}")
print("--------------------------------------------------------")

total_length = len(df)

length_lost = x - total_length

print("--------------------------------------------------------")
print(f"total length lost: {length_lost}")
print("--------------------------------------------------------")

df.to_csv(f"{full_data_dir}full_data_filtered.csv")


# plot again
# then is the pivot stage 
# then the fitting stage 


# have I done the kPA data manipulation?
# if not in future do at same time as all other data manipulation
>>>>>>> 808621a3bb3273d2fea73b5ca86aaec0b68ea224
