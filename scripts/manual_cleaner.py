# 
import pandas as pd

# dfs of importance 

# cleaning 
#MG-1 (29-gminj-018DIA2): 
# #All the interested responses showed a peak from time 0:31:28 to 1:23:21, which was caused by unusual engine activities (eg: shutdowns) and the data were suggested 
#by the technician to be excluded.  

#•V power-3 (29-gminj-023DIA3): Fuel flow and BSFC showed one peak in the begining from time 
#1:15:00 to 3:00:00 and one peak in the end from time 56:00:00 to 57:00:00 . These data were 
#suggested by the technician to be excluded due to unusual engine activities.
csv_folder = "C:\\Users\\Eleanor.E.Watson\\OneDrive - Shell\\Examples\\Ducu-git\\data\\csv_processed_filtered\\"
df1 = pd.read_csv(f"{fp}\\29-gminj-018DIA2.csv")
df2 = pd.read_csv(f"{fp}\\29-gminj-023DIA3") 
# that is my plan ! 
# or maybe the filtering only happens when doing the linear fit? 
# all the interested resonses for df1 
# bring back relevant cols.

relevant_cols = ['Coolant Pressure Outlet PSI P_COOLOU', 'Intake Air Pressure KPAG P_INAIR','Intake Air Temp °C T_INAIR','Fuel Flow kg/hr FLOWFUEL', 'Engine speed RPM SPEED','Intake Humidity g/kg HUM75','Post Inter Cooler Air Temp °C T_CHGOUT', 'Engine Torque NM TORQUE_1','Exhaust Pressure after Turbo kpa P_EXHABS','Injector Pulse width mS OBD_INJ', 'BSFC', 'Power'] 
for col in relevant_cols:
    df1[col] # filter based on the time !! 

# for df2 fuel flow and bsfc
df2['Fuel Flow kg/hr FLOWFUEL']
df2['BSFC']


##copied

###### manual cleaning
df_manual =  pd.read_csv(f"{csv_folder}\\29-gminj-023DIA3.csv") 
df_manual['Fuel Flow kg/hr FLOWFUEL']
df_manual['BSFC']
response = f"{col}_filtered"
df_manual['Filter_bool'] = df_manual['Engine speed RPM SPEED'].apply(lambda x: isinstance(x, float))
print(len(df_manual))
filter_df = df_manual[df_manual['Filter_bool']]
print(len(filter_df))
filter_df['time_list'] = filter_df['RUNTIMED'].apply(lambda x : x.strip(" ").split('.')[0].split(":"))
print(filter_df['time_list'])
filter_df['seconds'] = filter_df['time_list'].apply(lambda x : dt.timedelta(hours=int(x[0]), minutes=int(x[1]), seconds=int(x[2])).total_seconds())
print(filter_df['seconds'])
filter_df['seconds_index'] = filter_df['seconds']
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
##copied
y=filter_df['Fuel Flow kg/hr FLOWFUEL'].values.astype(float) # need to figure how to do opposite of loc and not select those columns
#  x=filter_df['seconds'].astype(float).loc[int(3600):int(21600)].values
#1:15:00 to 3:00:00 
#4500 - 10800
filter_df['seconds'] = filter_df['seconds'].astype(float).loc[~int(4500):(10800)]
x=filter_df['seconds'].astype(float).loc[int(3600):int(21600)].values
y=filter_df['Fuel Flow kg/hr FLOWFUEL'].astype(float).loc[x].values
print(f"Len x: {len(x)}, Len y: {len(y)}")
slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
SOT = intercept
print(f"Slope is: {slope}, intercept i.e. SOT is: {intercept}, r value: {r_value}, p value: {p_value}, standard error: {std_err}")
x_eot=filter_df['seconds'].values.astype(float)
y_eot=filter_df['Fuel Flow kg/hr FLOWFUEL'].values.astype(float)
x_eot=filter_df['seconds'].astype(float).loc[int(198000):int(216000)].values
y_eot=filter_df['Fuel Flow kg/hr FLOWFUEL'].astype(float).loc[x_eot].values
y_eot_max = eot=filter_df['Fuel Flow kg/hr FLOWFUEL'].astype(float).loc[x_eot].values.max()
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

row = {'Fuel':fuel, 'Run':run, 'Fuel_Block':fuel_block, 'Block':block, 'Response':response, 'SOT':SOT, 'EOT':EOT, 'change':delta, 'pert_change':pct_delta}
raw_data_processed_df.append(row, ignore_index=True)
df.append(row, ignore_index=True)

#copied


with open(rf"{final}", 'a+') as f:
    dict_writer_object = DictWriter(f, fieldnames = df_cols)
    dict_writer_object.writerow(row)
    f.close()


