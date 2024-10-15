import streamlit as st
from data_loader import read_file
from filters import generate_filters
from text_analysis import textual_analysis
from visualization import plot_histogram, plot_scatter_plot, plot_box_plot, plot_count_plot, plot_heatmap


def main():
    st.title('Advanced Interactive Data and Text Exploration Tool')
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
            if viz_type == 'Histogram':
                plot_histogram(df, column)
            elif viz_type == 'Scatter Plot':
                second_column = st.selectbox("Select Second Numeric Column", numeric_columns)
                plot_scatter_plot(df, column, second_column)
            elif viz_type == 'Box Plot':
                plot_box_plot(df, column)
    elif viz_type == 'Count Plot':
        categorical_columns = df.select_dtypes(['object', 'category']).columns.tolist()
        column = st.selectbox("Select Categorical Column", categorical_columns)
        plot_count_plot(df, column)
    elif viz_type == 'Heatmap':
        plot_heatmap(df)



if __name__ == "__main__":
    main()
