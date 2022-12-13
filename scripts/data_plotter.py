import pandas as pd
import os
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
import time
import numpy as np

raw_processed_csvs = r"C:\\Users\\Eleanor.E.Watson\\OneDrive - Shell\\Examples\\Dirty_Up_Clean_Up\\DUCU-example\\ducu-example\\raw_processed\\"
raw_processed_csvs_ls = os.listdir(raw_processed_csvs)
files_to_plot_ls = []
for file in raw_processed_csvs:
    df = pd.read_csv(f"raw_processed_csvs\\{file}.csv")
    files_to_plot_ls.append(df)

    