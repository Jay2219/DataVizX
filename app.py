import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


st.markdown("<h1 style='text-align: center; color: red;'>DataVizX</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: green; font-style: italic'>Developed By <a href = 'https://jayprajapati.netlify.app' style='color: lightblue;'>Jay</a></h3>", unsafe_allow_html=True)


# Add file uploader
uploaded_file = st.file_uploader("Choose a file", type=["csv", "xlsx"])

if uploaded_file is not None:
    # Read the uploaded file into a pandas DataFrame
    df = pd.read_csv(uploaded_file)  # for CSV files
    # df = pd.read_excel(uploaded_file)  # for Excel files

# Display the data table
if uploaded_file is not None:
    # Add a sidebar for sorting and filtering options
    sort_columns = st.sidebar.multiselect("Select columns to sort by", list(df.columns))
    filter_columns = st.sidebar.multiselect("Select columns to filter by", list(df.columns))
    filter_values = {}
    for col in filter_columns:
        filter_values[col] = st.sidebar.selectbox(f"Select a value for {col}", sorted(df[col].unique()))

    # Apply sorting and filtering
    df = df.sort_values(sort_columns) if sort_columns else df
    for col, value in filter_values.items():
        df = df[df[col] == value]

    # Display the data table
    st.experimental_data_editor(df)


st.set_option('deprecation.showPyplotGlobalUse', False)

# Add chart visualizations
if uploaded_file is not None:
    # Add a sidebar for chart options
    chart_type = st.sidebar.selectbox("Select a chart type", ["Scatter plot", "Line chart", "Bar chart"])
    x_column = st.sidebar.selectbox("Select a column for X-axis", list(df.columns))
    y_column = st.sidebar.selectbox("Select a column for Y-axis", list(df.columns))
    color_column = st.sidebar.selectbox("Select a column for color", ["None"] + list(df.columns))

    # Create the chart
    if chart_type == "Scatter plot":
        if color_column == "None":
            plt.scatter(df[x_column], df[y_column])
        else:
            sns.scatterplot(data=df, x=x_column, y=y_column, hue=color_column)
        plt.xlabel(x_column)
        plt.ylabel(y_column)
        st.pyplot()
    elif chart_type == "Line chart":
        if color_column == "None":
            plt.plot(df[x_column], df[y_column])
        else:
            sns.lineplot(data=df, x=x_column, y=y_column, hue=color_column)
        plt.xlabel(x_column)
        plt.ylabel(y_column)
        st.pyplot()
    elif chart_type == "Bar chart":
        if color_column == "None":
            plt.bar(df[x_column], df[y_column])
        else:
            sns.barplot(data=df, x=x_column, y=y_column, hue=color_column)
        plt.xlabel(x_column)
        plt.ylabel(y_column)
        st.pyplot()


# Add interactive widgets for adjusting chart parameters
if uploaded_file is not None:
    if chart_type == "Scatter plot":
        x_range = st.sidebar.slider("Select a range for X-axis", min(df[x_column]), max(df[x_column]),)