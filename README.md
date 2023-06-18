# ScrewingCell
Repository for Master's degree project made on Aalborg University called:

*"Time-Series Anomaly Detection for
Industrial Screwdriving Task with Machine
Learning Algorithms"*

This repository shows the code used on the project regarding the data collection, data processing, machine learning and deep learning.

## Dataset
The full dataset collected can be found on the following Google Drive:

[Dataset download](https://drive.google.com/file/d/1yo6eICPlD_ZEKKhkYUrDPdh4wYatlIMv/view?usp=drive_link)

The information regarding the dataset structure and the dataset can be found inside of the Dataset.zip which can be downloaded with the link provided. The dataset contains the following data sources:

- [Intrinsic data](#intrinsic-data)
- [Task data](#task-data)
- [Extrinsic data](#extrinsic-data)

### <a id="intrinsic-data"></a>Intrinsic data
Intrinsic data source provides the data from the sensors mounted on the automatic screwdriver. The sensors measure the screwdriving torque, angle, depth, current and RPM.

<img src="./Images/Automatic_Screwdriver.jpg" width="300">

### <a id="task-data"></a>Task data
Task data source provides the data from the Universal Robots UR10 robot. The data contains 6 Tool Centerpoint Position measurements, together with the current provided to the robot.

<img src="./Images/UR10.jpg" width="300">

### <a id="extrinsic-data"></a>Extrinsic data
Extrinsic data source provides the audio recording of the screwdriving process in .wav format.

<img src="./Images/Azure_Kinect_DK.jpg" width="300">


