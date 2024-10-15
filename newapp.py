import streamlit as st
import pandas as pd

def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Select a Page", ["Landing Page", "Data Analysis Desk", "Generate Report"])

    if page == "Landing Page":
        landing_page()
    elif page == "Data Analysis Desk":
        data_analysis_desk()
    elif page == "Generate Report":
        generate_report()

def landing_page():
    st.title("Welcome to the Data and Text Exploration Tool")
    st.write("""
    This application allows you to upload, analyze, and save your data with comprehensive insights.
    - Upload CSV or Excel files for analysis.
    - Adjust filters as needed.
    - Generate a detailed report in HTML format.
    """)

def data_analysis_desk():
    st.title("Data Analysis Desk")
    uploaded_file = st.file_uploader("Upload your file", type=['csv', 'xlsx'])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        if df is not None and not df.empty:
            st.write("Data Preview:", df.head())
            analysis_results = perform_full_analysis(df)
            st.session_state['analysis_results'] = analysis_results  # Store results in session state
            display_analysis_results(analysis_results)
        else:
            st.error("Uploaded file is empty or invalid. Please upload a different file.")

def perform_full_analysis(df):
    try:
        numeric_df = df.select_dtypes(include=['number'])
        results = {
            "Descriptive Statistics": numeric_df.describe(),
            "Correlation Analysis": numeric_df.corr(),
            "Missing Data Analysis": {
                "Counts": df.isnull().sum(),
                "Percentage": df.isnull().sum() / len(df) * 100
            },
            "Categorical Data Analysis": {
                col: df[col].value_counts() for col in df.select_dtypes(include=['object', 'category']).columns
            }
        }
        return results
    except Exception as e:
        st.error(f"Failed to perform analysis due to: {str(e)}")
        return {}

def display_analysis_results(results):
    for analysis_type, result in results.items():
        st.subheader(analysis_type)
        st.dataframe(result)

def generate_report():
    st.title("Generate HTML Report")
    if 'analysis_results' in st.session_state and st.button('Save Report to HTML'):
        save_html_report(st.session_state['analysis_results'])
        st.success("Report saved to 'report.html'")

def save_html_report(analysis_results):
    with open('report.html', 'w') as f:
        for title, data in analysis_results.items():
            f.write(f"<h1>{title}</h1>\n")
            f.write(pd.DataFrame(data).to_html() + "\n")

if __name__ == "__main__":
    main()
