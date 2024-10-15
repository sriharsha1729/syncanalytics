import pandas as pd

def read_file(uploaded_file):
    if uploaded_file.type == "text/csv":
        return pd.read_csv(uploaded_file)
    else:
        return pd.read_excel(uploaded_file)
