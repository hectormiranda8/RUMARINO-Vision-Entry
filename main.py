import sys
sys.path.append('./src')
sys.path.append('./images')
import os
from fileutils import files2list, list2file
from darknetutils import darknet_pretrain, darknet_train

def main():
    path = os.getcwd()

    # train.txt
    filearr = files2list("./images", ".jpg")
    modified = []
    for name in filearr:
        name = path + '\\images\\' + name
        modified.append(name)
    list2file("./model/train.txt", modified)

    # test.txt
    filearr = files2list("./images", ".txt")
    modified = []
    for name in filearr:
        name = path + '\\images\\' + name
        modified.append(name)
    list2file("./model/test.txt", modified)

    # modify detector.data
    detector_file = open("./model/detector.data", "r").read()
    detector_data = detector_file.split('\n')
    modified = []
    for i in detector_data:
        if "train" in i:
            line = "train=" + path + "\\model\\train.txt"
            modified.append(line)
        elif "valid" in i:
            line = "valid=" + path + "\\model\\test.txt"
            modified.append(line)
        elif "names" in i:
            line = "names=" + path + "\\model\\custom.names"
            modified.append(line)
        elif "backup" in i:
            line = "backup=" + path + "\\model\\backup\\weights"
            modified.append(line)
        else:
            modified.append(i)
    list2file("./model/detector.data", modified)

    
    
    # Change to your darknet path
    darknet_path = "C:\\Users\\HECTORAMIRANDA-SANCH\\source\\repos\\darknet\\darknet.exe"
    
    # darknet_pretrain(darknet, original_model, original_weights, trained_weights="pretrained-weights.conv.15")
    # os.system(f"{darknet} partial {original_model} {original_weights} {trained_weights} 15")

    og_model = path + "\\model\\yolov3-tiny.cfg"
    og_weights = path + "\\model\\yolov3-tiny.weights"
    darknet_pretrain(darknet_path, og_model, og_weights)

    # darknet_train(darknet, detector, model, trained_weights, log="train.log")
    # os.system(f"{darknet} detector train {detector} {model} {trained_weights} -gpus  0 -map > {log}")

    detector = path + "\\model\\detector.data"
    model = path + "\\model\\yolov3-tiny-generated.cfg"
    trained_weights = path + "\\pretrained-weights.conv.15"
    darknet_train(darknet_path, detector, model, trained_weights)


if __name__ == '__main__':
    main()