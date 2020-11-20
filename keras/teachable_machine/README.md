# Teachable Machine
[![Seldon](https://img.shields.io/badge/Engine-Seldon-F7B955)](https://www.seldon.io/)
[![Keras](https://img.shields.io/badge/Framework-Keras-79FFE1)](https://keras.io/)
![Computer Vision](https://img.shields.io/badge/Type-Computer%20Vision-79FFE1)
![Input](https://img.shields.io/badge/Input-JSON%20(base64)-79FFE1)
![Output](https://img.shields.io/badge/Output-JSON%20(list)-79FFE1)

[Teachable Machine](https://teachablemachine.withgoogle.com/) is a web platform introduced by Google. It allows you very easily build and train a machine learning model practically with no code.

In order to run your own model trained with [Image](https://teachablemachine.withgoogle.com/train/image):

1. Download `keras_model.h5` file and `labels.txt` by exporting Keras (Tensorflow) version. 
2. Unzip downlaoded package and substitute files in the `data` directory.
3. Model is ready to deploy!

## Deploy 
Click a button to deploy a model with [Syndicai](https://syndicai.co).

[![Syndicai-Deploy](https://raw.githubusercontent.com/syndicai/brand/main/button/deploy.svg)](https://app.syndicai.co/newModel?repository=https://github.com/syndicai/models/tree/master/keras/teachable_machine)


## Run Locally
Execute following commands in order to run a model locally.
```bash
# Download and run docker container
docker run -v ${PWD}:/mnt/workspace:ro -p 8000:8000 syndicai/engine:python3.7 local

# Run Model
curl -X POST http://localhost:8000/predict \
  -H 'content-type: application/json' \
  -d @sample_data/sample_input.json
```
