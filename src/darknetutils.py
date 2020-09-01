import os

def darknet_pretrain(darknet, original_model, original_weights, trained_weights="pretrained-weights.conv.15"):
    os.system(f"{darknet} partial {original_model} {original_weights} {trained_weights} 15")

def darknet_train(darknet, detector, model, trained_weights, log="train.log"):
    os.system(f"{darknet} partial {detector} {model} {trained_weights} -gpus  0 -map > {log}")
