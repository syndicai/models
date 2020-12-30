# MobileNetV2 Object detector
[![Tensorflow](https://img.shields.io/badge/Framework-Tensorflow-79FFE1)](https://www.tensorflow.org/)
![Computer Vision](https://img.shields.io/badge/Type-Computer%20Vision-79FFE1)
Classical object detection algorithm based on MobileNet V2. For this task [Tensorflow](https://www.tensorflow.org/) library and [Seldon Core](https://seldon.io) was used.


## Deploy 
Click a button to deploy a model with [Syndicai](https://syndicai.co).

[![Syndicai-Deploy](https://raw.githubusercontent.com/syndicai/brand/main/button/deploy.svg)](https://app.syndicai.co/newModel?repository=https://github.com/syndicai/models/tree/master/seldon/object_detector)


## Example
| input | output |
| --- | --- |
| <img src="sample_data/input.jpg" width="410"> | `snow leopard` |


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