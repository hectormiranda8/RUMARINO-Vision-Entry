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

## How training works
Each image has a corresponding text file that keeps bounding box information that points the relative location of the object to be detected.
A test and train text file must be created having the official paths for each image, these must be created by you.

Then you must modify the detector.data file found in the models folder to point to these newly created files.

Once this has been done then its time to get pretrained weights and train the provided model with these pretrained weights. HINT: look at the src folder.

## What to do?
You must create a script or scripts that takes the provided images, and trains them with the model. There is very minimal programming involved as most of the solution can be done using the provided scripts located in "src".

Send over your cloned repo to guy.garcia@upr.edu.
As long as the training process starts and creates a log this is enough for evaluation.