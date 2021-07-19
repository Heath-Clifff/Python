from motion_detection import df
from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.models import HoverTool, ColumnDataSource

df['Start_String'] = df['Start'].dt.strftime("%Y-%m-%d %H:%M:%S")
df['End_String'] = df['End'].dt.strftime("%Y-%m-%d %H:%M:%S")
cds = ColumnDataSource(df)

p = figure(x_axis_type='datetime', height=100,
           width=500, sizing_mode='scale_both', title='Motion Graph')
p.yaxis.minor_tick_line_color = None


hover = HoverTool(
    tooltips=[("Start ", "@Start_String"), ("End ", "@End_String")])
p.add_tools(hover)

q = p.quad(left="Start", right="End", top=1,
           bottom=0, color='green', source=cds)
output_file("Graph1.html")
show(p)
