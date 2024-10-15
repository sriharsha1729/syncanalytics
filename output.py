import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport
import time

def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Select a Page", ["Landing Page", "Data Analysis Desk", "Generate Report"])

    if page == "Landing Page":
        landing_page()
    elif page == "Data Analysis Desk":
        data_analysis_desk()
    elif page == "Generate Report":
        pass
        # generate_report()

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
            if st.button('Generate Profile Report'):
                with st.spinner('Generating profile report...'):
                    # generate_profile_report(df)
                    profile = ProfileReport(df, title="Pandas Profiling Report")
                    profile.to_file("data.json")
                    profile.to_file("data.html")
                    st.success('Profile report generated successfully!')
        else:
            st.error("Uploaded file is empty or invalid. Please upload a different file.")

def generate_profile_report(df):
    try:
        profile = ProfileReport(df, title="Pandas Profiling Report")
        profile_html = profile.to_html()
        # st.session_state['profile_html'] = profile_html
        st.markdown(profile_html, unsafe_allow_html=True)
        st.success('Profile report generated successfully!')
    except Exception as e:
        st.error(f"Failed to generate profile report: {e}")

# def generate_report():
#     st.title("Generate HTML Report")
#     if 'profile_html' in st.session_state:
#         if st.button('Save Report to HTML'):
#             with open('report.html', 'w') as f:
#                 f.write(st.session_state['profile_html'])
#             st.success("Report saved to 'report.html'")
#     else:
#         st.warning("Please generate a profile report first before saving.")

if __name__ == "__main__":
    main()
