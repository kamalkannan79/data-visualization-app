import streamlit as st
from PIL import Image



img1 = Image.open("image/data1.jpg")
img2 = Image.open("image/data2.jpg")
img3 = Image.open("image/data3.jpg")
img4 = Image.open("image/data4.jpg")
img5 = Image.open("image/data5.jpg")
img6 = Image.open("image/data6.jpg")
img7 = Image.open("image/data7.jpg")
img8 = Image.open("image/data8.jpg")
img9 = Image.open("image/data9.jpg")
img10 = Image.open("image/data10.jpg")


st.title("Description")

x = ['About App', 'Description of Graphs']

selectbox = st.sidebar.selectbox("Information",x)

if selectbox == 'About App':
    st.write("This is an Visualization app in this you can easily visualize your data. This graph automatically shows the inference of the graph you plotted.")
    st.write("In this app you can plot ten different types of graphs")
    st.write("1.Scatterplots")
    st.write("2.Lineplots")
    st.write("3.Histogram")
    st.write("4.Boxplot")
    st.write("5.Violinplot")
    st.write("6.Piechart")
    st.write("7.Areaplot")
    st.write("8.Heatmap")
    st.write("9.Barchart")
    st.write("10.Contour")
    st.write("If you have any doubt in these graph please check on description of graph, which gave you more idea about those graphs")

elif selectbox == 'Description of Graphs':

    select = ['None', 'Scatterplots', 'Lineplots', 'Histogram', 'Boxplot', 'Violinplot', 'Piechart', 'Areaplot', 'Heatmap', 'Barchart', 'Contour']
     
    chart_select = st.sidebar.selectbox("Choose Graphs",select)

    st.header((chart_select))
    
    if chart_select == 'None':
        try:
            st.markdown("Please select what graph you want to see")
        except Exception as e:
            print(e)
            
            
    if chart_select == 'Scatterplots':
        try:
            st.write( "A scatter plot is also called a scatter chart, scattergram, or scatter plot, XY graph. The scatter diagram graphs numerical data pairs, with one variable on each axis, show their relationship.")
            st.subheader("when to use a scatter plot?")
            st.write("1. When we have paired numerical data")
            st.write("2. When there are multiple values of the dependent variable for a unique value of an independent variable.")
            st.write("3. In determining the relationship between variables in some scenarios, such as identifying potential root causes of problems, checking whether two products that appear to be related both occur with the exact cause and so on.")
            st.subheader("Example")
            st.image(img1,width = 800)
        except Exception as e:
            print(e)
        
    if chart_select == 'Lineplots':
        try:
            st.write("  A line graph or line chart or line plot is a graph that utilizes points and lines to represent change over time. It is a chart that shows a line joining several points or a line that shows the relation between the points. The graph represents quantitative data between two changing variables with a line or curve that joins a series of successive data points. Linear graphs compare these two variables in a vertical axis and a horizontal axis.")
            st.subheader("Which is Used for")
            st.write("Generally, line graphs or line charts are used to track variations over time, which may be long-term or short-term. We can also use line graphs to compare changes over the same period for more than one group.")
            st.subheader("Example")
            st.image(img2,width = 800)
        except Exception as e:
            print(e)   

    if chart_select == 'Histogram':    
        try:
            st.write("  A histogram is a graphical representation of a grouped frequency distribution with continuous classes. It is an area diagram and can be defined as a set of rectangles with bases along with the intervals between class boundaries and with areas proportional to frequencies in the corresponding classes. In such representations, all the rectangles are adjacent since the base covers the intervals between class boundaries. The heights of rectangles are proportional to corresponding frequencies of similar classes and for different classes, the heights will be proportional to corresponding frequency densities.")
            st.subheader("When to Use Histogram?")
            st.write("1. The data should be numerical.")
            st.write("2. A histogram is used to check the shape of the data distribution. ")
            st.write("3. Used to check whether the process changes from one period to another.")
            st.subheader("Example")
            st.image(img3,width = 800)
        except Exception as e:
            print(e)

    if chart_select == 'Boxplot':   
        try:
            st.write("We can define the box plot in terms of descriptive statistics related concepts. That means box or whiskers plot is a method used for depicting groups of numerical data through their quartiles graphically. These may also have some lines extending from the boxes or whiskers which indicates the variability outside the lower and upper quartiles, hence the terms box-and-whisker plot and box-and-whisker diagram. Outliers can be indicated as individual points.")
            st.write("It helps to find out how much the data values vary or spread out with the help of graphs. As we need more information than just knowing the measures of central tendency, this is where the box plot helps. This also takes less space. It is also a type of pictorial representation of data.")
            st.subheader("Example")
            st.image(img4,width = 700)
        except Exception as e:
            print(e)

    if chart_select == 'Violinplot':   
        try:
            st.write("Violin Plot is a method to visualize the distribution of numerical data of different variables. It is similar to Box Plot but with a rotated plot on each side, giving more information about the density estimate on the y-axis.")
            st.write("The density is mirrored and flipped over and the resulting shape is filled in, creating an image resembling a violin. The advantage of a violin plot is that it can show nuances in the distribution that aren’t perceptible in a boxplot. On the other hand, the boxplot more clearly shows the outliers in the data.")
            st.write("A violin plot is more informative than a plain box plot. While a box plot only shows summary statistics such as mean/median and interquartile ranges, the violin plot shows the full distribution of the data. The difference is particularly useful when the data distribution is multimodal (more than one peak). In this case a violin plot shows the presence of different peaks, their position and relative amplitude.")
            st.subheader("Example")
            st.image(img5,width = 600)
        except Exception as e:
            print(e)
    
    if chart_select == 'Piechart':  
        try:
            st.write("The pie chart is also known as circle chart, that divides the circular statistical graphic into sectors or slices in order to illustrate the numerical problems. Each sector denotes a proportionate part of the whole. To find out the composition of something, Pie-chart works the best at that time.")
            st.write("The pie chart is an important type of data representation. It contains different segments and sectors in which each segment and sectors of a pie chart forms a certain portion of the total(percentage). The total of all the data is equal to 360°.")
            st.subheader("Why do we use pie charts?")
            st.write("Pie charts are used to represent the proportional data or relative data in a single chart. The concept of pie slices is used to show the percentage of a particular data from the whole pie.")
            st.subheader("Example")
            st.image(img6,width = 600)
        except Exception as e:
            print(e)
        
    if chart_select == 'Areaplot': 
        try:
            st.write("An area chart or area graph displays graphically quantitative data. It is based on the line chart. The area between axis and line are commonly emphasized with colors, textures and hatchings. Commonly one compares two or more quantities with an area chart.")
            st.write("Area charts are used to represent cumulated totals using numbers or percentages (stacked area charts in this case) over time. Use the area chart for showing trends over time among related attributes. The area chart is like the plot chart except that the area below the plotted line is filled in with color to indicate volume.")
            st.write("When multiple attributes are included, the first attribute is plotted as a line with color fill followed by the second attribute, and so on.")
            st.subheader("Example")
            st.image(img7,width = 700)
        except Exception as e:
            print(e)
        
    if chart_select == 'Heatmap': 
        try:
            st.write("A heatmap  depicts values for a main variable of interest across two axis variables as a grid of colored squares. The axis variables are divided into ranges like a bar chart or histogram, and each cell’s color indicates the value of the main variable in the corresponding cell range.")
            st.write("Heatmaps are used to show relationships between two variables, one plotted on each axis. By observing how cell colors change across each axis, you can observe if there are any patterns in value for one or both variables.")
            st.write("The variables plotted on each axis can be of any type, whether they take on categorical labels or numeric values. In the latter case, the numeric value must be binned like in a histogram in order to form the grid cells where colors associated with the main variable of interest will be plotted.")
            st.subheader("Example")
            st.image(img8,width = 800)
        except Exception as e:    
            print(e)
        
    if chart_select == 'Barchart': 
        try:
            st.write("Bar graphs are the pictorial representation of data (generally grouped), in the form of vertical or horizontal rectangular bars, where the length of bars are proportional to the measure of data. They are also known as bar charts. Bar graphs are one of the means of data handling in statistics.")
            st.write("Bar graphs are used to match things between different groups or to trace changes over time. Yet, when trying to estimate change over time, bar graphs are most suitable when the changes are bigger.")
            st.write("Bar charts possess a discrete domain of divisions and are normally scaled so that all the data can fit on the graph. When there is no regular order of the divisions being matched, bars on the chart may be organized in any order. ")
            st.subheader("Example")
            st.image(img9,width = 800)
        except Exception as e:
            print(e)
            
    if chart_select == 'Contour': 
        try:
            st.write("Contour Plots is the way in which you can represent the three-dimensional surface (having a length(X), Width(Y) and depth/volume(Z)) chart on a two-dimensional plane (i.e. in a plane with X and Y axis only). In this chart, lines are drawn for (x, y) coordinates where the response (z) values are occurring. Contour charts are similar to the surface charts that can be seen from above (any height) and are 2-D charts most of the time.")
            st.write("A contour graph can be used when we have two predictors X & Y, which have an impact on the response variable Z. The values of Z in the graph are called contours. Contour graphs are frequently used in Cartography which is more associated with geocoding of the regions. However, it also has some utilization under different branches such as Astrology, Meteorology; in statistics, this type of chart is used to check the relationship between two predictors and response.")
            st.subheader("Example")
            st.image(img10,width = 700)
        except Exception as e:
            print(e)
        