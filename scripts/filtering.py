import sklearn 
import pandas as pd
import scipy
import datetime as dt 
from scipy import stats 
import plotly.express as px
import os


csv_folder = r"C:\\Users\\Eleanor.E.Watson\\OneDrive - Shell\\Examples\\Ducu-git\\data\\raw_to_csv_processed\\"
csv_files = os.listdir(csv_folder)
full_data_dir = r"C:\\Users\\Eleanor.E.Watson\\OneDrive - Shell\\Examples\\Ducu-git\\data\\csv_processed_filtered\\"


csv_list = []
for file in csv_files:
    df = pd.read_csv(csv_folder+file)
    csv_list.append(df)

for df in csv_list:
    filename = df['Filename'].values[2]
    x = len(df)
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

    # need to do these conversions. !!
    # so coolout and what else. 
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

    df.to_csv(f"{full_data_dir}//{filename}.csv")
