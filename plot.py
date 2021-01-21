from motion import df
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource

#Getting all the data from Times.csv(that was being created in motion.py file) in pandas dataframe structure 
df["Start_string"]=df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S") 
df["End_string"]=df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")


cds=ColumnDataSource(df)