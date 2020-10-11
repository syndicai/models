# Animal Classifier
[![Seldon](https://img.shields.io/badge/Engine-Seldon-F7B955)](https://www.seldon.io/)
[![OpenCV](https://img.shields.io/badge/Framework-Tensorflow-79FFE1)](https://www.tensorflow.org/)
![Computer Vision](https://img.shields.io/badge/Type-Computer%20Vision-79FFE1)
![Input](https://img.shields.io/badge/Input-JSON%20(base64)-79FFE1)
![Output](https://img.shields.io/badge/Output-JSON%20(string)-79FFE1)

The main of the algorthm is to check the species of the animal using object detection algorithm. For this task [Tensorflow](https://www.tensorflow.org/) library and [Seldon Core](https://seldon.io) was used.


## Deploy 
Click a button to deploy a model with [Syndicai](https://syndicai.co).

[![Syndicai-Deploy](https://raw.githubusercontent.com/syndicai/brand/main/button/deploy.svg)](https://app.syndicai.co/newModel?repository=https://github.com/syndicai/models/sample-animalclassifier)




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
