import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

def plot_histogram(df, column, ax):
    df[column].hist(ax=ax, bins=20, edgecolor='black')
    ax.set_title(f"Histogram of {column}")
    ax.set_xlabel(column)
    ax.set_ylabel("Frequency")

def plot_scatter_plot(df, column, second_column, ax):
    ax.scatter(df[column], df[second_column], alpha=0.7)
    ax.set_title(f"Scatter Plot of {column} vs {second_column}")
    ax.set_xlabel(column)
    ax.set_ylabel(second_column)

def plot_box_plot(df, column):
    fig, ax = plt.subplots()
    sns.boxplot(data=df, y=column, ax=ax)
    st.pyplot(fig)

def plot_count_plot(df, column, ax):
    df[column].value_counts().plot(kind='bar', ax=ax)
    ax.set_title(f"Count Plot of {column}")
    ax.set_xlabel(column)
    ax.set_ylabel("Count")

def plot_heatmap(df, ax):
    # Select only numeric columns
    numeric_df = df.select_dtypes(include=['float', 'int'])
    
    # Check if there are any numeric columns to correlate
    if not numeric_df.empty:
        correlation_matrix = numeric_df.corr()
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', ax=ax)
        ax.set_title("Correlation Heatmap")
    else:
        ax.text(0.5, 0.5, "No numeric data available for correlation.", 
                horizontalalignment='center', verticalalignment='center', fontsize=12)
        ax.set_title("Correlation Heatmap")
