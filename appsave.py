import streamlit as st
import os
import matplotlib.pyplot as plt
from datetime import datetime
from data_loader import read_file
from filters import generate_filters
from text_analysis import textual_analysis
from visualization import plot_histogram, plot_scatter_plot, plot_box_plot, plot_count_plot, plot_heatmap

def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Select a Page", ["Landing Page", "Current Analysis Desk", "Generate Report"])

    if page == "Landing Page":
        landing_page()
    elif page == "Current Analysis Desk":
        analysis_desk()
    elif page == "Generate Report":
        generate_report()

def landing_page():
    st.title("Welcome to the Data and Text Exploration Tool")
    st.write("""
    This application helps you upload, filter, and analyze your data with interactive visualizations.
    You can:
    - Upload CSV or Excel files for analysis.
    - Apply filters and perform text analysis.
    - Generate different visualizations like histograms, scatter plots, heatmaps, and more.
    - Generate a report based on your analysis.
    Use the sidebar to navigate through the different functionalities.
    """)

def analysis_desk():
    st.title("Current Analysis Desk")
    uploaded_file = st.file_uploader("Upload your file", type=['csv', 'xlsx'])

    if uploaded_file is not None:
        df = read_file(uploaded_file)
        st.write("Data Preview:", df.head())
        filtered_data = generate_filters(df)

        if st.checkbox('Perform Text Analysis'):
            textual_analysis(df)

        visualize_data(filtered_data)

def visualize_data(df):
    st.title("Customizable Data Visualizations")
    if not df.empty:
        viz_type = st.selectbox("Select Visualization Type", ['Histogram', 'Count Plot', 'Scatter Plot', 'Heatmap', 'Box Plot'])
        plot_visualization(df, viz_type)

def plot_visualization(df, viz_type):
    if viz_type in ['Histogram', 'Scatter Plot', 'Box Plot']:
        numeric_columns = df.select_dtypes(['float', 'int']).columns.tolist()
        column = st.selectbox("Select Numeric Column", numeric_columns)
        if column:
            fig, ax = plt.subplots()
            if viz_type == 'Histogram':
                plot_histogram(df, column, ax)
            elif viz_type == 'Scatter Plot':
                second_column = st.selectbox("Select Second Numeric Column", numeric_columns)
                plot_scatter_plot(df, column, second_column, ax)
            elif viz_type == 'Box Plot':
                plot_box_plot(df, column)

            save_visualization(fig, viz_type.lower().replace(' ', '_'), column)
            plt.close(fig)  # Close plt to prevent it from displaying in the notebook

    elif viz_type == 'Count Plot':
        categorical_columns = df.select_dtypes(['object', 'category']).columns.tolist()
        column = st.selectbox("Select Categorical Column", categorical_columns)
        fig, ax = plt.subplots()
        plot_count_plot(df, column, ax)
        save_visualization(fig, 'count_plot', column)
        plt.close(fig)  # Close plt to prevent it from displaying in the notebook

    elif viz_type == 'Heatmap':
        fig, ax = plt.subplots()
        plot_heatmap(df, ax)
        save_visualization(fig, 'heatmap', 'correlation_matrix')
        plt.close(fig)  # Close plt to prevent it from displaying in the notebook

def save_visualization(fig, plot_type, column_name):
    # Create a unique filename with a timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{plot_type}_{column_name}_{timestamp}.png"
    
    # Save the figure to the current directory
    fig_path = os.path.join('./saved_visualizations', filename)
    os.makedirs(os.path.dirname(fig_path), exist_ok=True)  # Ensure the directory exists
    fig.savefig(fig_path)
    st.write(f"Visualization saved as {filename} in the 'saved_visualizations' directory.")
    st.image(fig_path)  # Optionally, display the saved image back in Streamlit

def generate_report():
    st.title("Generate Report")
    st.write("""
    Here, you can generate a summary report of your data analysis.
    Make sure you have completed your analysis and generated the necessary visualizations before creating the report.
    """)

    if st.button('Generate Report'):
        # Placeholder for report generation logic
        st.write("Generating your report...")
        # Example: You could gather all insights and visualizations into a PDF or text file.
        st.write("Report generated successfully! (This is a placeholder, add your report generation logic here.)")

if __name__ == "__main__":
    main()
