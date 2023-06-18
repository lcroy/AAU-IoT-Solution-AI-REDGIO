import pandas as pd
import xml.etree.ElementTree as ET

# Parse the XML data
tree = ET.parse(r"C:\Users\GHB\Desktop\SCREW PROJECT\Data\Sensor data\ScrewingCell\_000.KXML")
root = tree.getroot()

# Extract the header information
version = root.find('Wsk3Header/Version').text
date = root.find('Wsk3Header/Date').text
time = root.find('Wsk3Header/Time').text
title = root.find('Wsk3Header/Title').text
num_y_axes = int(root.find('Wsk3Header/NumberofYAxes').text)
num_vectors = int(root.find('Wsk3Header/NumberOfVectors').text)

# Extract the X axis data
x_axis = root.find('Wsk3Vectors/X_Axis')
x_name = x_axis.find('Header/Name').text
x_unit = x_axis.find('Header/Unit').text
x_values = [float(x.text) for x in x_axis.find('Values').iter('float')]

# Extract the Y axis data
y_axes = root.find('Wsk3Vectors/Y_AxesList')
y_data = {}
for axis in y_axes.iter('AxisData'):
    y_index = int(axis.find('_Index').text)
    y_name = axis.find('Header/Name').text
    y_unit = axis.find('Header/Unit').text
    y_values = [float(x.text) for x in axis.find('Values').iter('float')]
    y_data[y_index] = {'name': y_name, 'unit': y_unit, 'values': y_values}

# Combine the X and Y axis data into a single DataFrame
data = {'Time (ms)': x_values}
for i in range(num_y_axes):
    data[y_data[i]['name'] + ' (' + y_data[i]['unit'] + ')'] = y_data[i]['values']
df = pd.DataFrame(data)


# save the DataFrame to a CSV file
df.to_csv(r"C:\Users\GHB\Desktop\SCREW PROJECT\Data\Sensor data\ScrewingCell\_000.csv", index=False)

print(df.head())