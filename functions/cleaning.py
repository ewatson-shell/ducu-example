
import pandas as pd

def cleaner(min, max, col):
    df = df[[df[col] > min | df[col] < max]]
    return df