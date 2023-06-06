import os
import pandas as pd
import xml.etree.ElementTree as ET
import shutil
import datetime

wood = input("Wood number:")

# Function that converts kxml files to csv and renames them
def convert_xml_to_csv(input_folder_KXML, output_folder_CSV):
    # get today's date as a datetime object
    today = datetime.date.today()
    # convert the datetime object to a string using strftime()
    date_string = today.strftime('%d%m%Y')
    # Iterate over all files in the input folder with .xml extension
    for filename in os.listdir(input_folder_KXML):
        if filename.endswith(".KXML"):
            # Parse the XML data
            tree = ET.parse(os.path.join(input_folder_KXML, filename))
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

            # Save the DataFrame to a CSV file with the same name as the input file
            output_filename = os.path.join(output_folder_CSV, os.path.splitext(filename)[0] + ".csv")
            df.to_csv(output_filename, index=False)
            
            

            print(f"{filename} converted to {output_filename}")
            
    for filename in os.listdir(output_folder_CSV):
        if "csv" in filename:
            # construct the new file name by adding the prefix to the original file name
            new_filename = "i" + date_string + wood + filename[1:4] + ".csv"
        
            # use the rename() function to rename the file
            os.rename(os.path.join(output_folder_CSV, filename), os.path.join(output_folder_CSV, new_filename))
input_folder_KXML = r"C:\Users\GHB\Desktop\Screwcell dataset\Intrinsic data\KXML"
output_folder_CSV = r"C:\Users\GHB\Desktop\Screwcell dataset\Intrinsic data"
convert_xml_to_csv(input_folder_KXML, output_folder_CSV)





taskdata_dir = r"C:\Users\GHB\Desktop\Screwcell dataset\Task data"
intrinsic_dir = r"C:\Users\GHB\Desktop\Screwcell dataset\Intrinsic data"
extrinsic_dir = r"C:\Users\GHB\Desktop\Screwcell dataset\Extrinsic data"


# Input types of screwdrivings
miss = int(input("Type number of missing screws:"))
miss_s = []
no = int(input("Type the number of no-screws:"))
no_s = []
bent = int(input("Type number of out-of-plane screws:"))
bent_s = []
ot = int(input("Type number of over-tightened screws:"))
ot_s = []
n = int(input("Type number of normal screws:"))
n_s = []

# Loop through n times and get an input from the user each time
for i in range(miss):
    input_miss = input("Enter mising pins #" + str(i+1) + ": ")
    miss_s.append(input_miss)
    
for i in range(no):
    input_no = input("Enter no pins #" + str(i+1) + ": ")
    no_s.append(input_no)
    
for i in range(bent):
    input_bent = input("Enter bent pins #" + str(i+1) + ": ")
    bent_s.append(input_bent)
    
for i in range(ot):
    input_ot = input("Enter over-tightened pins #" + str(i+1) + ": ")
    ot_s.append(input_ot)

for i in range(n):
    input_n = input("Enter normal pins #" + str(i+1) + ": ")
    n_s.append(input_n)

print(miss_s)
print(bent_s)
print(ot_s)
print(n_s)

# Function that will move the files
def move_files(number_list, source_dir, dest_dir):
    files = os.listdir(source_dir)
    # Loop through the files and move any that end with a number in the number_list
    for filename in files:
        for number in number_list:
            if filename.endswith(number + ".csv") or filename.endswith(number + ".wav"):
                # Construct the full paths for the source and destination files
                src_path = os.path.join(source_dir, filename)
                dest_path = os.path.join(dest_dir, filename)
                
                # Move the file to the destination directory
                shutil.move(src_path, dest_path)
                print(f"Moved {filename} to {dest_dir}")

#Task data
move_files(miss_s, taskdata_dir, r"C:\Users\GHB\Desktop\Screwcell dataset\Task data\M")
move_files(no_s, taskdata_dir, r"C:\Users\GHB\Desktop\Screwcell dataset\Task data\NS")
move_files(bent_s, taskdata_dir, r"C:\Users\GHB\Desktop\Screwcell dataset\Task data\B")
move_files(ot_s, taskdata_dir, r"C:\Users\GHB\Desktop\Screwcell dataset\Task data\OT")
move_files(n_s, taskdata_dir, r"C:\Users\GHB\Desktop\Screwcell dataset\Task data\N")
files_t = os.listdir(taskdata_dir)
for filename in files_t:
    if "csv" in filename:
        # Construct the full paths for the source and destination files
        src_path_t = os.path.join(taskdata_dir, filename)
        dest_path_t = os.path.join(r"C:\Users\GHB\Desktop\Screwcell dataset\Task data\UT", filename)
        # Move the underscrewd files to UT
        shutil.move(src_path_t, dest_path_t)



#Extrinsic data
move_files(miss_s, extrinsic_dir, r"C:\Users\GHB\Desktop\Screwcell dataset\Extrinsic data\M")
move_files(no_s, extrinsic_dir, r"C:\Users\GHB\Desktop\Screwcell dataset\Extrinsic data\NS")
move_files(bent_s, extrinsic_dir, r"C:\Users\GHB\Desktop\Screwcell dataset\Extrinsic data\B")
move_files(ot_s, extrinsic_dir, r"C:\Users\GHB\Desktop\Screwcell dataset\Extrinsic data\OT")
move_files(n_s, extrinsic_dir, r"C:\Users\GHB\Desktop\Screwcell dataset\Extrinsic data\N")
files_e = os.listdir(extrinsic_dir)
for filename in files_e:
    if "wav" in filename:
        src_path_e = os.path.join(extrinsic_dir, filename)
        dest_path_e = os.path.join(r"C:\Users\GHB\Desktop\Screwcell dataset\Extrinsic data\UT", filename)
        # Move the good screw files to N
        shutil.move(src_path_e, dest_path_e)



#Intrinsic data
move_files(miss_s, intrinsic_dir, r"C:\Users\GHB\Desktop\Screwcell dataset\Intrinsic data\M")
move_files(no_s, intrinsic_dir, r"C:\Users\GHB\Desktop\Screwcell dataset\Intrinsic data\NS")
move_files(bent_s, intrinsic_dir, r"C:\Users\GHB\Desktop\Screwcell dataset\Intrinsic data\B")
move_files(ot_s, intrinsic_dir, r"C:\Users\GHB\Desktop\Screwcell dataset\Intrinsic data\OT")
move_files(n_s, intrinsic_dir, r"C:\Users\GHB\Desktop\Screwcell dataset\Intrinsic data\N")
files_i = os.listdir(intrinsic_dir)
for filename in files_i:
    if "csv" in filename:
        src_path_i = os.path.join(intrinsic_dir, filename)
        dest_path_i = os.path.join(r"C:\Users\GHB\Desktop\Screwcell dataset\Intrinsic data\UT", filename)
        # Move the under tightened files to UT
        shutil.move(src_path_i, dest_path_i)






