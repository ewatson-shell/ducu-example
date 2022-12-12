
import pandas as pd

def cleaner(min, max, col):
    df = df[[df[col] > min | df[col] < max]]
    return df

# thought to myself -> should I be also including the length here? 
# if I clean on every individual file, is concatenation required? 
# something to check -> is matplotlib more memory efficient than plotly.



