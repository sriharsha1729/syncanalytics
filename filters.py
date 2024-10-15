import streamlit as st
import pandas as pd

def generate_filters(df):
    st.sidebar.title("Filters")
    filtered_df = df.copy()

    for col in df.columns:
        if pd.api.types.is_numeric_dtype(df[col]):
            min_val, max_val = df[col].min().item(), df[col].max().item()
            values = st.sidebar.slider(f"Filter by {col}", float(min_val), float(max_val), (float(min_val), float(max_val)))
            filtered_df = filtered_df[filtered_df[col].between(values[0], values[1])]
        elif pd.api.types.is_datetime64_any_dtype(df[col]):
            min_date, max_date = df[col].min(), df[col].max()
            date_range = st.sidebar.date_input(f"Filter by {col}", [min_date, max_date])
            filtered_df = filtered_df[filtered_df[col].between(*date_range)]
        elif pd.api.types.is_categorical_dtype(df[col]) or pd.api.types.is_object_dtype(df[col]):
            options = st.sidebar.multiselect(f"Filter by {col}", df[col].unique(), default=df[col].unique())
            filtered_df = filtered_df[filtered_df[col].isin(options)]

    st.write("Filtered Data:", filtered_df)
    return filtered_df
