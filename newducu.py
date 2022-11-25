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

#run_time = time.now().strftime()
run_time = "test"
'''
data_units = [pd.read_excel(f"{raw_data_dir}\\{x}", sheet_name="Data Collection", header=[11,12,13]) for x in raw_data_files ]

for df, filename in zip(data_units, raw_data_files):
    filename = os.path.splitext(filename)[0]
    df.to_csv(f"C:\\Users\\Eleanor.E.Watson\\OneDrive - Shell\\Examples\\Dirty_Up_Clean_Up\\DUCU-example\\csv\\dataframe_{filename}.csv")
'''
#######################################

csv = []
for filename in csv_files:
    df = pd.read_csv(f"{csv_dir}{filename}", index_col=False)
    csv.append(df)


######################################## 
for j,k in zip(range(len(csv)),csv_files):
    df = csv[j] 
    filename = os.path.splitext(k)
    filename = filename[0]
    print(f"{filename}")
    for i in range(2,len(df.columns)):
        try:
            x = df.iloc[:,1]
            y = df.iloc[:,i]
            xaxis = df.columns[1]
            yaxis=df.columns[i]
            #title= f"{str(csv[0].columns[0])} + {str(csv[0].columns[1])}")
            fig1 = px.scatter(x=x, y=y,labels= {"x":f"{xaxis}","y":f"{yaxis}"}, width=600,height=300)
            ####

           # f = open(f"{output_folder}p_graph.html", 'a')
            f = open(f"{output_folder}{filename}.html", 'a+')
            f.write(fig1.to_html(full_html=False, include_plotlyjs='cdn'))
            f.write(f"Data from: {k}")
            f.write("--------------------------------------")
            f.close()
        except:
            print("NONE")


=======
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

#run_time = time.now().strftime()
run_time = "test"
'''
data_units = [pd.read_excel(f"{raw_data_dir}\\{x}", sheet_name="Data Collection", header=[11,12,13]) for x in raw_data_files ]

for df, filename in zip(data_units, raw_data_files):
    filename = os.path.splitext(filename)[0]
    df.to_csv(f"C:\\Users\\Eleanor.E.Watson\\OneDrive - Shell\\Examples\\Dirty_Up_Clean_Up\\DUCU-example\\csv\\dataframe_{filename}.csv")
'''
#######################################

csv = []
for filename in csv_files:
    df = pd.read_csv(f"{csv_dir}{filename}", index_col=False)
    csv.append(df)


######################################## 
for j,k in zip(range(len(csv)),csv_files):
    df = csv[j] 
    filename = os.path.splitext(k)
    filename = filename[0]
    print(f"{filename}")
    for i in range(2,len(df.columns)):
        try:
            x = df.iloc[:,1]
            y = df.iloc[:,i]
            xaxis = df.columns[1]
            yaxis=df.columns[i]
            #title= f"{str(csv[0].columns[0])} + {str(csv[0].columns[1])}")
            fig1 = px.scatter(x=x, y=y,labels= {"x":f"{xaxis}","y":f"{yaxis}"}, width=600,height=300)
            ####

           # f = open(f"{output_folder}p_graph.html", 'a')
            f = open(f"{output_folder}{filename}.html", 'a+')
            f.write(fig1.to_html(full_html=False, include_plotlyjs='cdn'))
            f.write(f"Data from: {k}")
            f.write("--------------------------------------")
            f.close()
        except:
            print("NONE")


>>>>>>> 808621a3bb3273d2fea73b5ca86aaec0b68ea224
