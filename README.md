# RUMARINO-Vision-Entry
A simple little entry test that looks for good work understandings.

## Setup
Before starting you must first install some dependencies for this project.
Install [OpenCV](https://www.pyimagesearch.com/2018/08/15/how-to-install-opencv-4-on-ubuntu/).
Note: Avoid installing the pip library opencv-python as it has problems with using video.

Install Alexey's [Darknet](https://github.com/AlexeyAB/darknet).
Note: Read setup instructions as they show different compilations parameters.

Download [Yolov3-tiny cfg and weights](https://pjreddie.com/darknet/yolo/).

Install Numpy [Using pip](https://packaging.python.org/tutorials/installing-packages/).

The model, along with its pretrained weights can be found in "model", the training data can be found in "images".

## What to do?
You must create a script or scripts that takes the provided images, and trains them with the model. There is very minimal programming involved as most of the solution can be done using the provided scripts located in "src".

Read the /src/rundarknet.py comments to undestand what needs to be done.