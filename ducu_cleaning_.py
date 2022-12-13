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
 # csv_orig is a list of dataframes//csvs from the list of files from csv_dir which is in a folder called CSV manipulated.
 # QUESTION: currently unsure what exactly csv_manipulated involves.
 # ANSWER: csv_manipulated is just the read in datafiles it seems. 
    # Still the three index rows
    # everything else the same.
 # have a feeling csv_manipulated may be ... just the read in files only their sheets potentially? 
 # pretty un processed but still need to check and confirm this.
for filename in csv_files:
    df = pd.read_csv(f"{csv_dir}{filename}", index_col=0)
    csv_orig.append(df)
  #  print(len(df))
  #  print("--------------------")
################
# columns - renaming the runtimed column so it is consistent in all dataframes in CSV dir.
################

############## DEBUGGING #################################
 # csv_orig is a list of dataframes//csvs from the list of files from csv_dir which is in a folder called CSV manipulated.
 # QUESTION: currently unsure what exactly csv_manipulated involves.
 # csv - is a list of dataframes from csv_orig however they had 2 extra columns on the side so this is removing these extra columns.
csv = []
for df in csv_orig: 
    df = df.iloc[2:]
    csv.append(df)

# renaming the columns in the dataframe from a long RUNTIMED to more concise RUNTIMED.
for df, filename_ in zip(csv, csv_files): 
    try:
       df.rename(columns={'RUNTIMED SECS Unnamed: 1_level_2': 'RUNTIMED'}, inplace=True)
       df.to_csv( f"C:\\Users\\Eleanor.E.Watson\\OneDrive - Shell\\Examples\\Dirty_Up_Clean_Up\\DUCU-example\\ducu-example\\raw_processed\\{filename_}.csv")
    except:
        None



## write these cleaned files to be plotted? 
## QUESTION: where did I do this originally and with what data? 

##########################################################
##########################
# concatenating files
#########################
# have to squish the columns into 1 header before concatenation!
#for df in csv:
full_df = pd.concat([csv[0],csv[1],csv[2],csv[3],csv[4],csv[5],csv[6],csv[7],csv[8],csv[9],csv[10]], ignore_index = True)

# HERE WE ARE REMOVING THE RELATIVE TRUES (DOES THIS WORK MAYBE CHECK?)
# QUESTION: If this is the point where the trues are removed then do need to make a note of number of datarows lost.

for col in df.columns: 
    df = df[df[col] !='True']
    df = df[df[col] !='TRUE']

#writing to full df to csv, but specifically to the _2 version? why? what is the difference? 

full_df.to_csv(f"{full_data_dir}full_data_2.csv")
#TODO
########################################
# converting UNITS
# identify which to be converted to KPA
########################################


## adding the kpa conversion column
# here it reads in the full_data csv and not the full_data2 version? why is that?  
# # additionally it doesn't actually even read either csv because it has commented out csv and doesn't read it in.
#df = pd.read_csv(f"{full_data_dir}full_data.csv", index_col=False)
df = full_df
df['KPA_Constant'] = 6.89476 
# QUESTION: 15:31 - 13/12/2022
# QUESTION: what comes before csv_manipulated? in this question I mean which script comes before? 
#---------------------------
# inlet airpressure -> P_INAIR (kPa)
# coolant pressure -> P_COOLOU(PSI) (   CONVERT    )
# exhaust backpressure -> P_EXHABS(kPa)
# fuel rail pressure -> P_FUELS(PSI) (   CONVERT    )
df['Coolant Pressure Outlet PSI P_COOLOU'] = df['Coolant Pressure Outlet PSI P_COOLOU'].astype(float)

for column in df.columns:
    try:
        df[column] = df[df[column] != 'True']
        df[column] = df[df[column] != 'TRUE']
        df[column] = df[column].astype(float)
    except:
        print(f"{column} cannot be changed") # does this happen? # TODO: ACTION: change the q's and i's here.
    col_dtype = df[column].dtype
    print(f"{column}, {col_dtype})")

print("df['Coolant Pressure Outlet PSI P_COOLOU']", df['Coolant Pressure Outlet PSI P_COOLOU'].dtype)
print("df['KPA_Constant']", df['KPA_Constant'].dtype)
print("--------------------------------------------------------------------------------------")

print(df['Engine speed RPM SPEED'].unique())

# UP TO HERE
# updated from psi to kpa
df['Coolant Pressure Outlet kPA P_COOLOU'] = df['Coolant Pressure Outlet PSI P_COOLOU']*df['KPA_Constant']
df['Supply Fuel pressure kpa P_FUELS'] = df['Supply Fuel pressure  PSI P_FUELS']*df["KPA_Constant"]

print("uniques:")
print(df['Supply Fuel pressure kpa P_FUELS'].unique())

try:
    df['Power kW'] = df['OBD Engine Speed RPM OBD_RPM']*60*2*np.pi*df['Engine Torque NM TORQUE_1']*(1/60**2)*(1/10**3)
    # CREATE BSFC
    df['BSFC'] = (df['Fuel Flow kg/hr FLOWFUEL']*10**3)/df['Power kW']
except:
    print("could not convert ")

# UP TO HERE.
#df.to_csv(pre_filtered_csv)
# where is prefiltered csv.

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

#for i in df['Engine speed RPM SPEED'].unique():
#    print(type(i))
#   
#    try:
#        print(f"length of item: {len(i)}")
#        y = i.strip()
#        y = y.replace(" ", "")
#        print(f"Length of stripped i: {len(y)}: i is - {i}abc")
#        length_difference = len(i) - len(y)
#        if length_difference > 0:
#            print("!!!!!!!!!!!! !!!!!!!!!!!!!")
#            print(f"i is {i}:y is {y} - length difference is {length_difference}")#

#        z = y.astype(float)
#        print(type(z))
#        print("==================")
#    except:
#        pass
print(df['Engine speed RPM SPEED'].unique())
df['Engine speed RPM SPEED'].astype(float)
#df = df[[df['Engine speed RPM SPEED'] >= 1990 | df['Engine speed RPM SPEED'] <= 2010]]
df = df.loc[df['Engine speed RPM SPEED'].ge(1990)]
df= df.loc[df['Engine speed RPM SPEED'].le(2010)]
y = len(df)
print(df.head(4))
z = x - y
print("--------------------------------------------------------")
print(f"Number of lines lost after engine speed filter is: {z}")
perc = (x-y)/(x)*100
print(f"Percentage Lost: {perc}")
print("--------------------------------------------------------")

#df = df[[df['Engine Torque NM TORQUE_1'] < 103 | df['Engine Torque NM TORQUE_1'] > 97]]
df = df.loc[df['Engine Torque NM TORQUE_1'].le(103)] 
df = df.loc[df['Engine Torque NM TORQUE_1'].ge(97)]
print(df.head(4))
y = len(df)

z = x - y
print("--------------------------------------------------------")
print(f"Number of lines lost after Engine Torque NM TORQUE_1 is: {z}")
perc = (x-y)/(x)*100
print(f"Percentage Lost: {perc}")
print("--------------------------------------------------------")

# will be inlet air pressure here but not currently as haven't done the kPa conversion ! 
# #'Intake Air Pressure KPAG P_INAIR'

#df = df[[df['Intake Air Pressure KPAG P_INAIR'] > 0.04 | df['Intake Air Pressure KPAG P_INAIR'] < 0.06]]
df = df.loc[df['Intake Air Pressure KPAG P_INAIR'].ge(0.04)]
df = df.loc[df['Intake Air Pressure KPAG P_INAIR'].le(0.06)]

y = len(df)

z = x - y
print("--------------------------------------------------------")
print(f"Number of lines lost after Intake Air Pressure KPAG P_INAIR  is: {z}")
perc = (x-y)/(x)*100
print(f"Percentage Lost: {perc}")
print("--------------------------------------------------------")

#df = df[[df['Oil Galley Temp °C T_OILGAL'] > 84 | df['Oil Galley Temp °C T_OILGAL'] < 90]]
df = df.loc[df['Oil Galley Temp °C T_OILGAL'].ge(84)]
df = df.loc[df['Oil Galley Temp °C T_OILGAL'].le(90)]
y = len(df)

z = x - y
print("--------------------------------------------------------")
print(f"Number of lines lost after Oil Galley Temp °C T_OILGAL is: {z}")
perc = (x-y)/(x)*100
print(f"Percentage Lost: {perc}")

print("--------------------------------------------------------")

#df = df[[df['Coolant Temp Outlet °C T_COOLOU'] < 83 | df['Coolant Temp Outlet °C T_COOLOU'] > 77]]
df = df.loc[df['Coolant Temp Outlet °C T_COOLOU'].ge(77)]
df = df.loc[df['Coolant Temp Outlet °C T_COOLOU'].le(83)]
y = len(df)

z = x - y
print("--------------------------------------------------------")
print(f"Number of lines lost after Coolant Temp Outlet °C T_COOLOU is: {z}")
perc = (x-y)/(x)*100
print(f"Percentage Lost: {perc}")

print("--------------------------------------------------------")


#df = df[[df['Intake Air Temp °C T_INAIR'] < 35 | df['Intake Air Temp °C T_INAIR'] > 29]]
df = df.loc[df['Intake Air Temp °C T_INAIR'].ge(29)]
df = df.loc[df['Intake Air Temp °C T_INAIR'].le(35)]
y = len(df)

z = x - y
print("--------------------------------------------------------")
print(f"Number of lines lost after Intake Air Temp °C T_INAIR is: {z}")
perc = (x-y)/(x)*100
print(f"Percentage Lost: {perc}")
print("--------------------------------------------------------")


#df = df[[df['Coolant Pressure Outlet PSI P_COOLOU'] < 100 | df['Coolant Pressure Outlet PSI P_COOLOU'] > 80]]
df = df.loc[df['Coolant Pressure Outlet kPA P_COOLOU'].ge(80)]
df = df.loc[df['Coolant Pressure Outlet kPA P_COOLOU'].le(100)]

y = len(df)

z = x - y
print("--------------------------------------------------------")
print(f"Number of lines lost after Coolant Pressure Outlet PSI P_COOLOU is: {z}")
perc = (x-y)/(x)*100
print(f"Percentage Lost: {perc}")
print("--------------------------------------------------------")


#df = df[[df['Fuel Temp °C T_FUELS'] < 33 | df['Fuel Temp °C T_FUELS'] > 27]]
df = df.loc[df['Fuel Temp °C T_FUELS'].ge(27)]
df = df.loc[df['Fuel Temp °C T_FUELS'].le(33)]
y = len(df)
#------
# where is intake box filter temp?
#-------
z = x - y
print("--------------------------------------------------------")
print(f"Number of lines lost after Fuel Temp °C T_FUELS is: {z}")
perc = (x-y)/(x)*100
print(f"Percentage Lost: {perc}")
print("--------------------------------------------------------")

#df = df[[df['Post Inter Cooler Air Temp °C T_CHGOUT'] < 38 | df['Post Inter Cooler Air Temp °C T_CHGOUT'] > 32]]
df = df.loc[df['Post Inter Cooler Air Temp °C T_CHGOUT'].ge(32)]
df = df.loc[df['Post Inter Cooler Air Temp °C T_CHGOUT'].le(38)]
y = len(df)

z = x - y
print("--------------------------------------------------------")
print(f"Number of lines lost after Post Inter Cooler Air Temp °C T_CHGOUT is: {z}")
perc = (x-y)/(x)*100
print(f"Percentage Lost: {perc}")
print("--------------------------------------------------------")

#df = df[[df['Exhaust Pressure after Turbo kpa P_EXHABS'] < 103 | df['Exhaust Pressure after Turbo kpa P_EXHABS'] > 101]]
df = df.loc[df['Exhaust Pressure after Turbo kpa P_EXHABS'].ge(101)]
df = df.loc[df['Exhaust Pressure after Turbo kpa P_EXHABS'].le(103)]
y = len(df)
z = x - y
print("--------------------------------------------------------")
print(f"Number of lines lost after Exhaust Pressure after Turbo kpa P_EXHABS is: {z}")
perc = (x-y)/(x)*100
print(f"Percentage Lost: {perc}")
print("--------------------------------------------------------")

# would be p fuels here 'Supply Fuel pressure  PSI P_FUELS'


#df = df[[df['Supply Fuel pressure  PSI P_FUELS'] < 600 | df['Supply Fuel pressure  PSI P_FUELS'] > 450]]
df = df.loc[df['Supply Fuel pressure kpa P_FUELS'].ge(390)] #needs to be kpa 
df = df.loc[df['Supply Fuel pressure kpa P_FUELS'].le(600)]
# --------------------------------------
#---------------------------------------
# removed because filtered out too many 
# --------------------------------------
#---------------------------------------

y  = len(df)
z = x - y
print("--------------------------------------------------------")
print(f"Number of lines lost after Supply Fuel pressure  kpa P_FUELS is: {z}")
perc = (x-y)/(x)*100
print(f"Percentage Lost: {perc}")
print("--------------------------------------------------------")

#df = df[[df['Intake Humidity g/kg HUM75'] < 12.4 | df['Intake Humidity g/kg HUM75'] > 11.4]]
# --------------------------------------
#---------------------------------------
# removed because filtered out too many 
# --------------------------------------
#---------------------------------------
df = df.loc[df['Intake Humidity g/kg HUM75'].ge(10.4)] #needs to be kpa 
df = df.loc[df['Intake Humidity g/kg HUM75'].le(12.4)]
y = len(df)
z = x - y

print("--------------------------------------------------------")
print(f"Number of lines lost after Intake Humidity g/kg HUM75 is: {z}")
perc = (x-y)/(x)*100
print(f"Percentage Lost: {perc}")
print("--------------------------------------------------------")

total_length = len(df)

length_lost = x - total_length
percentage_loss = ((total_length-length_lost)/total_length)*100

print("--------------------------------------------------------")
print(f"total length lost: {length_lost}")
print("--------------------------------------------------------")
print(f"Total Percentage of Data lost: {percentage_loss}")
print("--------------------------------------------------------")

df.to_csv(f"{full_data_dir}full_data_filtered_additional.csv")

