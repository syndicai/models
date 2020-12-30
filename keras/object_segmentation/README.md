# Object detection and segmentation
[![Keras](https://img.shields.io/badge/Framework-Keras-79FFE1)](https://keras.io/)
![Computer Vision](https://img.shields.io/badge/Type-Computer%20Vision-79FFE1)

This is an implementation of Mask R-CNN on Python 3, Keras, and TensorFlow. The model generates bounding boxes and segmentation masks for each instance of an object in the image. It's based on Feature Pyramid Network (FPN) and a ResNet101 backbone.

## Deploy 
Click a button to deploy a model with [Syndicai](https://syndicai.co).

[![Syndicai-Deploy](https://raw.githubusercontent.com/syndicai/brand/main/button/deploy.svg)](https://app.syndicai.co/newModel?repository=https://github.com/syndicai/models/tree/master/keras/object_segmentation)

## Example

| input | output |
| --- | --- |
| <img src="sample_data/image.jpeg" width="410"> | <img src="sample_data/output.jpeg" width="410"> |


## Source
Code based on [Mask_RCNN](https://github.com/matterport/Mask_RCNN).
