import sklearn 
import pandas as pd
import scipy
import datetime as dt 
from scipy import stats 
import plotly.express as px
import os
from csv import DictWriter
import time
csv_folder = r"C:\\Users\\Eleanor.E.Watson\\OneDrive - Shell\\Examples\\Ducu-git\\data\\csv_processed_filtered\\"
csv_files = os.listdir(csv_folder)
final = r"C:\\Users\\Eleanor.E.Watson\\OneDrive - Shell\\Examples\\Ducu-git\\data\\csv_processed_cleaned_final\\final.csv"

df = pd.read_csv(f"{csv_folder}29-gminj-018DIA2.csv")


csv_list = [df]


print(csv_list)

feature_columns = ['BSFC', 'Power kW','Fuel Flow kg/hr FLOWFUEL', 'OBD Long Term Fuel Trim Shift  % OBD_LTFT', 'Engine Torque NM TORQUE_1' ]
#feature_columns = ['Injector Pulse width mS OBD_INJ']
df_cols = ['Fuel', 'Run', 'Fuel_Block', 'Block', 'Response', 'SOT', 'EOT', 'change', 'pert_change']


raw_data_processed_df = pd.DataFrame(columns = df_cols)
for df in csv_list:
    df['Filter_bool'] = df['Engine speed RPM SPEED'].apply(lambda x: isinstance(x, float))
    print(len(df))
    filter_df = df[df['Filter_bool']]
    print(len(filter_df))
    filter_df['time_list'] = filter_df['RUNTIMED'].apply(lambda x : x.strip(" ").split('.')[0].split(":"))
    print(filter_df['time_list'])
    filter_df['seconds'] = filter_df['time_list'].apply(lambda x : dt.timedelta(hours=int(x[0]), minutes=int(x[1]), seconds=int(x[2])).total_seconds())
    print(filter_df['seconds'])
    filter_df['seconds_index'] = filter_df['seconds']
    filter_df.drop(filter_df[(filter_df['seconds'] > 1888) & (filter_df['seconds'] < 5001)].index, inplace=True)
    filter_df['Fuel_Block'] = filter_df['Fuel']+filter_df['Block'].astype('str')
    print(filter_df.columns)
    print(filter_df.head(10))
    filter_df.set_index('seconds_index', inplace=True)
    x=filter_df['seconds'].values.astype(float)
    run = filter_df['Run'].values[2]
    block = filter_df['Block'].values[2]
    fuel_block = filter_df['Fuel_Block'].values[2]
    fuel = filter_df['Fuel'].values[2]
    filename = filter_df['Filename'].values[2]
    df = pd.DataFrame(columns=df_cols)
    for col in feature_columns:
        y=filter_df[col].values.astype(float)
        x=filter_df['seconds'].astype(float).loc[int(3600):int(21600)].values
        y=filter_df[col].astype(float).loc[x].values
        print(f"Len x: {len(x)}, Len y: {len(y)}")
        slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
        SOT = intercept
        print(f"Slope is: {slope}, intercept i.e. SOT is: {intercept}, r value: {r_value}, p value: {p_value}, standard error: {std_err}")
        x_eot=filter_df['seconds'].values.astype(float)
        y_eot=filter_df[col].values.astype(float)
        x_eot=filter_df['seconds'].astype(float).loc[int(198000):int(216000)].values
        y_eot=filter_df[col].astype(float).loc[x_eot].values
        y_eot_max = eot=filter_df[col].astype(float).loc[x_eot].values.max()
        print(f"Len x: {len(x_eot)}, Len y: {len(y_eot)}")
        slope_eot, intercept_eot, r_value_eot, p_value_eot, std_err_eot = stats.linregress(x_eot,y_eot)
        EOT = slope_eot*216000 + intercept_eot
        # see if can get variance from the linear regress documentation
        print(f"Slope is: {slope_eot},EOT is: {EOT}, intercept is: {intercept_eot} r value: {r_value_eot}, p value: {p_value_eot}, standard error: {std_err_eot}")
        delta = EOT - SOT 
        pct_delta = ((EOT-SOT)/SOT)*100
        print(f"SOT is: {SOT}, EOT is: {EOT}, EOT_max is: {y_eot_max}")
        print("=============================")
        print(f"Percentage Change: {pct_delta}, delta: {delta}")
        print("===============================")
        response = f"{col}_adjusted"
        row = {'Fuel':fuel, 'Run':run, 'Fuel_Block':fuel_block, 'Block':block, 'Response':response, 'SOT':SOT, 'EOT':EOT, 'change':delta, 'pert_change':pct_delta}
        raw_data_processed_df.append(row, ignore_index=True)
        df.append(row, ignore_index=True)
        print(raw_data_processed_df.head(20))

       # with open(r"C:\\Users\\Eleanor.E.Watson\\OneDrive - Shell\\Examples\\Dirty_Up_Clean_Up\\DUCU-example\\ducu-example\\full_data\\raw_data_processed.csv", 'a+') as f:
       #     dict_writer_object = DictWriter(f, fieldnames = df_cols)
       #     dict_writer_object.writerow(row)
       #     f.close()
        time.sleep(5)
        with open(f"{final}", 'a+') as f:
            dict_writer_object = DictWriter(f, fieldnames = df_cols)
            dict_writer_object.writerow(row)
            f.close()


