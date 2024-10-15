import os
import pandas as pd
import matplotlib.pyplot as plt

def save_analysis_to_html(df, visualizations, file_name="analysis_report.html"):
    """Save pandas DataFrame and visualizations to an HTML file."""
    # Save DataFrame to HTML
    df_html = df.to_html()

    # Save plots
    plots_html = ""
    for viz in visualizations:
        fig = viz.figure
        fig.savefig("temp_plot.png")
        plt.close(fig)  # Close the plot to avoid display in Streamlit
        plots_html += f'<img src="temp_plot.png">'

    # Combine everything into one HTML
    html_content = f"<html><body>{df_html}<br>{plots_html}</body></html>"

    # Write to HTML file
    with open(file_name, "w") as file:
        file.write(html_content)

    # Optionally delete temporary plot images if needed
    os.remove("temp_plot.png")
