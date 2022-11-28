import sklearn 
import pandas as pd
import scipy
import datetime as dt 
from scipy import stats 
import plotly.express as px
import os


csv_folder = r"C:\\Users\\Eleanor.E.Watson\\OneDrive - Shell\\Examples\\Dirty_Up_Clean_Up\\DUCU-example\\ducu-example\\full_data\\csv\\"
csv_files = os.listdir(csv_folder)

df = pd.read_csv(csv_folder+csv_files[0])


print(df.head(100))

df['Filter_bool'] = df['Engine speed RPM SPEED'].apply(lambda x: isinstance(x, float))
print(len(df))

filter_df = df[df['Filter_bool']]

print(len(filter_df))

filter_df['time_list'] = filter_df['RUNTIMED'].apply(lambda x : x.strip(" ").split('.')[0].split(":"))

print(filter_df['time_list'])

filter_df['seconds'] = filter_df['time_list'].apply(lambda x : dt.timedelta(hours=int(x[0]), minutes=int(x[1]), seconds=int(x[2])).total_seconds())

print(filter_df['seconds'])
filter_df['seconds_index'] = filter_df['seconds']

print(filter_df.columns)
print(filter_df.head(10))
filter_df.set_index('seconds_index', inplace=True)

x=filter_df['seconds'].values.astype(float)
y=filter_df['Injector Pulse width mS OBD_INJ'].values.astype(float)

x=filter_df['seconds'].astype(float).loc[int(3600):int(21600)].values
y=filter_df['Injector Pulse width mS OBD_INJ'].astype(float).loc[x].values

print(f"Len x: {len(x)}, Len y: {len(y)}")

slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
SOT = intercept
print(f"Slope is: {slope}, intercept i.e. SOT is: {intercept}, r value: {r_value}, p value: {p_value}, standard error: {std_err}")


x_eot=filter_df['seconds'].values.astype(float)
y_eot=filter_df['Injector Pulse width mS OBD_INJ'].values.astype(float)

x_eot=filter_df['seconds'].astype(float).loc[int(198000):int(216000)].values
y_eot=filter_df['Injector Pulse width mS OBD_INJ'].astype(float).loc[x_eot].values

y_eot_max = eot=filter_df['Injector Pulse width mS OBD_INJ'].astype(float).loc[x_eot].values.max()
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

