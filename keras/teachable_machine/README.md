# Teachable Machine
[![Keras](https://img.shields.io/badge/Framework-Keras-79FFE1)](https://keras.io/)
![Computer Vision](https://img.shields.io/badge/Type-Computer%20Vision-79FFE1)

[Teachable Machine](https://teachablemachine.withgoogle.com/) is a web platform introduced by Google. It allows you very easily build and train a machine learning model practically with no code.

In order to run your own model trained with [Image](https://teachablemachine.withgoogle.com/train/image):

1. Download `keras_model.h5` file and `labels.txt` by exporting Keras (Tensorflow) version. 
2. Unzip downlaoded package and substitute files in the `data` directory.
3. Model is ready to deploy!

## Deploy 
Click a button to deploy a model with [Syndicai](https://syndicai.co).

[![Syndicai-Deploy](https://raw.githubusercontent.com/syndicai/brand/main/button/deploy.svg)](https://app.syndicai.co/newModel?repository=https://github.com/syndicai/models/tree/master/keras/teachable_machine)

## Example
| input | output |
| --- | --- |
| <img src="sample_data/test_photo.jpg" width="410"> | `"PLASTIC": "0.10%", "PAPER": "0.00%", "METAL": "0.56%", "CARDBOARD": "0.00%", "GLASS": "99.34%" `|


## Reference
Model created with the use of [Teachable Machine](https://teachablemachine.withgoogle.com/) Platform - A fast, easy way to create machine learning models for your sites, apps, and more – no expertise or coding required. 