#imports
import pandas as pd
import os
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import time
import numpy as np
import matplotlib.pyplot as plt

#raw_data_dir = r"C:\\Users\\Eleanor.E.Watson\\OneDrive - Shell\\Examples\\Dirty_Up_Clean_Up\\DUCU-example\\ducu-example\\raw_"
#raw_data_files = os.listdir(raw_data_dir)
filtered_csv= r"C:\\Users\\Eleanor.E.Watson\\OneDrive - Shell\\Examples\\Dirty_Up_Clean_Up\\DUCU-example\\ducu-example\\full_data\\full_data_filtered.csv"
fp = r"C:\\Users\\Eleanor.E.Watson\\OneDrive - Shell\\Examples\\Dirty_Up_Clean_Up\\DUCU-example\\ducu-example\\full_data"
csv_folder = r"C:\\Users\\Eleanor.E.Watson\\OneDrive - Shell\\Examples\\Dirty_Up_Clean_Up\\DUCU-example\\ducu-example\\full_data\\csv"
#####################################

#df = pd.read_csv(filtered_csv, index_col = False )
# if grouping the CSV file does this help a lot? 
#print(df.columns)


# SPLITTING UP THE CSV FILES (UNCONCATENATING)
#create unique list of names
#Filenames = df.Filename.unique()

#for filename in list(Filenames):
#    df.loc[df['Filename'] == f"{filename}"].to_csv(f"{fp}\\{filename}.csv")
#    print(df['Filename', 'RUNTIMED', 'Intake Manifold Temp °C T_INTMAN', 'Compressor Air out °C T_CMPOUT' ].head(1000))

# why is run 11/da426 half the size of the rest? 

#create a data frame dictionary to store your data frames
#DataFrameDict = {elem : pd.DataFrame() for elem in Filenames}





csv_files = os.listdir(csv_folder)

csv = []
for filename in csv_files:
    df = pd.read_csv(f"{csv_folder}\\{filename}", index_col=False)
    csv.append(df)


######################################## 
output_folder = r"C:\\Users\\Eleanor.E.Watson\\OneDrive - Shell\\Examples\\Dirty_Up_Clean_Up\\DUCU-example\\ducu-example\\graphs"
csv_lists = []
def split(list_a, chunk_size):

  for i in range(0, len(list_a), chunk_size):
    yield list_a[i:i + chunk_size]



print("-------------")
for j,k in zip(range(len(csv)),csv_files):
    df = csv[j] 
    chunk_size = 2
    columns = list(df.columns)
    print("columns: ", columns)
    column_list = list(split(columns, chunk_size))
    print(csv_lists)
    filename = os.path.splitext(k)[0]
   
    print(f"Fliename: {filename}")
    #columns = ['Engine Torque NM TORQUE_1','Fuel Flow kg/hr FLOWFUEL','BSFC','Power kW']

    # 'Coolant Pressure Outlet kPA P_COOLOU','Supply Fuel pressure kpa P_FUELS','Engine speed RPM SPEED','Intake Humidity g/kg HUM75','Post Inter Cooler Air Temp Â°C T_CHGOUT','Exhaust Pressure after Turbo kpa P_EXHABS','OBD Long Term Fuel Trim Shift  % OBD_LTFT']
    for col_chunk in column_list:
        for i in col_chunk:
            print(f"col_chunk[i]: {col_chunk.index(i)}")
            try:
                x = df['RUNTIMED'].values
                y = df[i].values
                xaxis = 'RUNTIMED'
                yaxis=i
                #title= f"{str(csv[0].columns[0])} + {str(csv[0].columns[1])}")
                fig1 = px.scatter(x=x, y=y,labels= {"x":xaxis,"y":yaxis}, width=600,height=300)
                ####

            # f = open(f"{output_folder}p_graph.html", 'a')
                f = open(f"{output_folder}\\{filename}_filtered_{col_chunk.index(i)}_{i}.html", 'a+')
                f.write(fig1.to_html(full_html=False, include_plotlyjs='cdn')) #add \n
                f.write(f"\nData from: {k}\n")
                f.write("--------------------------------------\n")
                f.close()
            except Exception as e:
                print(e)
