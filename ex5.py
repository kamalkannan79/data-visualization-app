import streamlit as st
import plotly_express as px
import pandas as pd
import subprocess

# configuration
st.set_option('deprecation.showfileUploaderEncoding', False)

# title of the app
st.title("Visualization App For BI")

# Add a sidebar
st.sidebar.subheader("Visualization Settings")

# Setup file upload
uploaded_file = st.sidebar.file_uploader(
                        label="Upload your CSV or Excel file",
                         type=['csv', 'xlsx'])

global df

if uploaded_file is not None:
    print(uploaded_file)
    print("hello")

    try:
        df = pd.read_csv(uploaded_file)
    except Exception as e:
        print(e)
        df = pd.read_excel(uploaded_file)
        
st.write('Hi, *Guys!* :sunglasses:')
st.write("If you don't know about the app or the graphs please select the description given below")
if st.button("Description"):
    subprocess.Popen(["streamlit", "run", "new1.py"])

st.sidebar.write("(or)")
st.sidebar.write("Choose some default datasets")

default_dataset = st.sidebar.selectbox(
    label = "select the dataset",
    options=['None', 'Campus Requirement Dataset', 'Carseat Dataset', 'Cereal Dataset', 'Insurance Dataset', 'Iris Dataset', 'Mtcars Dataset', 'Penguin Dataset', 'Pokemon Dataset','Students Dataset','Students Test Performance Dataset']
)

if default_dataset == 'Campus Requirement Dataset':
    try:
        df = pd.read_csv("C:/Users/kamalesh/Desktop/Project Dataset/Campus Requirement.csv")
    except Exception as e:
        print(e)   

if default_dataset == 'Carseat Dataset':
    try:
        df = pd.read_csv("C:/Users/kamalesh/Desktop/Project Dataset/carseats.csv")
    except Exception as e:
        print(e)  

if default_dataset == 'Cereal Dataset':
    try:
        df = pd.read_csv("C:/Users/kamalesh/Desktop/Project Dataset/cereal.csv")
    except Exception as e:
        print(e)  

if default_dataset == 'Insurance Dataset':
    try:
        df = pd.read_csv("C:/Users/kamalesh/Desktop/Project Dataset/insurance.csv")
    except Exception as e:
        print(e)  

if default_dataset == 'Iris Dataset':
    try:
        df = pd.read_csv("C:/Users/kamalesh/Desktop/Project Dataset/IRIS.csv")
    except Exception as e:
        print(e)         

if default_dataset == 'Mtcars Dataset':
    try:
        df = pd.read_csv("C:/Users/kamalesh/Desktop/Project Dataset/mtcars.csv")
    except Exception as e:
        print(e)

if default_dataset == 'Penguin Dataset':
    try:
        df = pd.read_csv("C:/Users/kamalesh/Desktop/Project Dataset/Penguins_data.csv")
    except Exception as e:
        print(e)

if default_dataset == 'Pokemon Dataset':
    try:
        df = pd.read_csv("C:/Users/kamalesh/Desktop/Project Dataset/Pokemon.csv")
    except Exception as e:
        print(e)

if default_dataset == 'Students Dataset':
    try:
        df = pd.read_csv("C:/Users/kamalesh/Desktop/Project Dataset/students.csv")
    except Exception as e:
        print(e)
        
if default_dataset == 'Students Test Performance Dataset':
    try:
        df = pd.read_csv("C:/Users/kamalesh/Desktop/Project Dataset/StudentsPerformance.csv")
    except Exception as e:
        print(e)


st.header("Data")
global numeric_columns
global non_numeric_columns
try:
    st.write(df)
    numeric_columns = list(df.select_dtypes(['float','int','float32','int32','float64','int64']).columns)
    non_numeric_columns = list(df.select_dtypes(['object','bool']).columns)
    non_numeric_columns.append(None)
    print(non_numeric_columns)
except Exception as e:
    print(e)
    st.write("Please upload file to the application.")

# add a select widget to the side bar
chart_select = st.sidebar.radio(
    label="Select the chart type",
    options=['Scatterplots', 'Lineplots', 'Histogram', 'Boxplot', 'Violinplot', 'Piechart', 'Areaplot', 'Heatmap', 'Barchart', 'Contour']
)

st.header((chart_select))


if chart_select == 'Scatterplots':
    st.sidebar.subheader("Scatterplot Settings")
    try:
        x_values = st.sidebar.selectbox('X axis', options=numeric_columns)
        y_values = st.sidebar.selectbox('Y axis', options=numeric_columns)
        color_value = st.sidebar.selectbox("Color", options=non_numeric_columns)
        plot = px.scatter(data_frame=df, x=x_values, y=y_values, color=color_value)
        # display the chart
        st.plotly_chart(plot)
        st.header("Inference")
        st.write("Generally Scatterplot helps to find the relation between the variables. The x axis and Y axis Of the graph is ",x_values," and ",y_values," respectively. So we can find the graph shows the releationship between ", x_values, "and", y_values, ". Each color of the graph represents the ",color_value,"'s.")
    except Exception as e:
        print(e)
        

if chart_select == 'Lineplots':
    st.sidebar.subheader("Line Plot Settings")
    try:
        x_values = st.sidebar.selectbox('X axis', options=numeric_columns)
        y_values = st.sidebar.selectbox('Y axis', options=numeric_columns)
        color_value = st.sidebar.selectbox("Color", options=non_numeric_columns)
        plot = px.line(data_frame=df, x=x_values, y=y_values, color=color_value)
        st.plotly_chart(plot)
        st.header("Inference")
        st.write("A lineplot is a graph that displays data as points or check marks above a number line, showing the frequency of each value. In the above graph we take  x axis and Y axis as is ",x_values," and ",y_values,". Each color of the graph represents the ",color_value,"'s. It shows the difference between each ",color_value,".")
    except Exception as e:
        print(e)

if chart_select == 'Histogram':
    st.sidebar.subheader("Histogram Settings")
    try:
        x = st.sidebar.selectbox('Feature', options=numeric_columns)
        bin_size = st.sidebar.slider("Number of Bins", min_value=10,
                                     max_value=100, value=40)
        plot = px.histogram(x=x, data_frame=df,nbins = bin_size )
        st.plotly_chart(plot)
        st.header("Inference")
        st.write("A Histogram is a graphical representation of a grouped frequency distribution with continuous classes. Histogram is a univariate graph. In this graph we plotted a histogram for ",x,". In this we can find the frequency whether it is maximum frequency or minimum frequency in the ",x,". ")
    except Exception as e:
        print(e)

if chart_select == 'Boxplot':
    st.sidebar.subheader("Boxplot Settings")
    try:
        y = st.sidebar.selectbox("Y axis", options=numeric_columns)
        x = st.sidebar.selectbox("X axis", options=non_numeric_columns)
        color_value = st.sidebar.selectbox("Color", options=non_numeric_columns)
        plot = px.box(data_frame=df, y=y, x=x, color=color_value)
        st.plotly_chart(plot)
        st.header("Inference")
        st.write("This Graph Is Box Plot. Which shows us the lower limit(min),quartile 1,quartile 2,quartile 3 and upper limit(max). Which helps to find how the data is spreaded.In this graph we can see that maximum data is spread between ",x," and ",y,".")
    except Exception as e:
        print(e)

if chart_select == 'Violinplot':
    st.sidebar.subheader("Violinplot Settings")
    try:
        y = st.sidebar.selectbox("Y axis", options=numeric_columns)
        x = st.sidebar.selectbox("X axis", options=non_numeric_columns)
        color_value = st.sidebar.selectbox("Color", options=non_numeric_columns)
        plot = px.violin(data_frame=df, y=y, x=x, box=True, color=color_value)
        st.plotly_chart(plot)
        st.header("Inference")
        st.write(" Violin plots are similar to box plots, except that they also show the probability density of the data at different values, usually smoothed by a kernel density estimator. In this we plotted violin chart between ",x," and ",y,". The violin plot is plotted for ",y," with respect to ",x,". In this we find q1, q2, q3, min, max valuse and kde value.")
    except Exception as e:
        print(e)
        
if chart_select == 'Piechart':
    st.sidebar.subheader("Piechart Settings")
    try:
        x = st.sidebar.selectbox('Feature', options=numeric_columns)
        color_value = st.sidebar.selectbox("Color", options=non_numeric_columns)
        plot = px.pie(values=x, data_frame=df, names=color_value)
        st.plotly_chart(plot)
        st.header("Inference")
        st.write("A pie chart (or a circle chart) is a circular statistical graphic, which is divided into slices to illustrate numerical proportion. In this graph we draw for ",x," with respect to the ",color_value,". It helps to understand how many percentage of ",x," in ",color_value," .")
    except Exception as e:
        print(e)

if chart_select == 'Areaplot':
    st.sidebar.subheader("Areaplot Settings")
    try:
        x_values = st.sidebar.selectbox('X axis', options=numeric_columns)
        y_values = st.sidebar.selectbox('Y axis', options=numeric_columns)
        color_value = st.sidebar.selectbox("Color", options=non_numeric_columns)
        plot = px.area(data_frame=df, x=x_values, y=y_values, color=color_value)
        st.plotly_chart(plot)
        st.header("Inference")
        st.write("An Area Plot is an extension of a Line Chart. An Area Plot is obtained by filling the region between the Line Chart and the axes with a color. The graph is plotted with X and Y axis as ",x_values," and ",y_values," respectively.Each colour of the graph represents the ",color_value,". This graph shows the difference between ",x_values," and ",y_values," of each ",color_value,".")
    except Exception as e:
        print(e)

if chart_select == 'Heatmap':
    st.sidebar.subheader("Heatmap Settings")
    try:
        x_values = st.sidebar.selectbox('X axis', options=numeric_columns)
        y_values = st.sidebar.selectbox('Y axis', options=numeric_columns)
        plot = px.density_heatmap(data_frame=df, x=x_values, y=y_values)
        st.plotly_chart(plot)
        st.header("Inference")
        st.write("A heat map  is a data visualization technique that shows magnitude of a phenomenon as color in two dimensions. In this graph we taken X and Y axis as ",x_values," and ",y_values,". On the right side of the graph we can saw a count which has some color code for the values. We can understand the graph through the colors in it.")
    except Exception as e:
        print(e)

if chart_select == 'Barchart':
    st.sidebar.subheader("Bar Chart Settings")
    try:
        y_values = st.sidebar.selectbox("Y axis", options=numeric_columns)
        x_values = st.sidebar.selectbox("X axis", options=non_numeric_columns)
        plot = px.bar(data_frame=df, y=y_values, x=x_values)
        st.plotly_chart(plot)
        st.header("Inference")
        st.write("Generally bar graph is helps to find the difference between categorical data. In this graph we can easily find the difference between ",x_values," about their ",y_values,". It helps easily  to understand that which ",x_values," have more ",y_values," and which ",x_values," have less ",y_values,".")
    except Exception as e:
        print(e)

if chart_select == 'Contour':
    st.sidebar.subheader("Contour Settings")
    try:
        y_values = st.sidebar.selectbox("Y axis", options=numeric_columns)
        x_values = st.sidebar.selectbox("X axis", options=numeric_columns)
        color_value = st.sidebar.selectbox("Color", options=non_numeric_columns)
        plot = px.density_contour(data_frame=df, y=y_values, x=x_values,marginal_x="histogram", marginal_y="histogram",color=color_value)
        st.plotly_chart(plot)
        st.header("Inference")
        st.write(" Contour plot is computed by grouping a set of points specified by their x and y coordinates into bins. In this we plot between ",x_values," and ",y_values,". In the margin of the contour graph we saw some histogram, those histograms are ",x_values,"'s histogram which is parallel to X axis and ",y_values,"'s histogram which is parallel to Y axis. The color of the graph represents the ",color_value," which helps to find the difference between ",color_value," on their ",x_values,"and ",y_values,".")
    except Exception as e:
        print(e)

