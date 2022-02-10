# AlexNet Image Classifier
[![PyTorch](https://img.shields.io/badge/Framework-PyTorch-79FFE1)](https://pytorch.org)
![Computer Vision](https://img.shields.io/badge/Type-Computer%20Vision-79FFE1)

AlexNet is the name of a convolutional neural network (CNN) architecture, designed by Alex Krizhevsky. AlexNet contained eight layers; the first five were convolutional layers, some of them followed by max-pooling layers, and the last three were fully connected layers. It used the non-saturating ReLU activation function, which showed improved training performance over tanh and sigmoid.


## Deploy 
Click a button to deploy a model with [Syndicai](https://syndicai.co).

[![Syndicai-Deploy](https://raw.githubusercontent.com/syndicai/brand/main/button/deploy.svg)](https://app.syndicai.co/newModel?repository=https://github.com/syndicai/models/tree/master/pytorch/image_classifier)


## Example
| input | output |
| --- | --- |
| <img src="sample_data/input.jpg" width="410"> | `hotdog` |


## Local run
Run the following command in the terminal in order to test the model locally.
```
python run.py
```