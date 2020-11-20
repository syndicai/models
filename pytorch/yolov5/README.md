# Yolo V5
[![Seldon](https://img.shields.io/badge/Engine-Seldon-F7B955)](https://www.seldon.io/)
[![PyTorch](https://img.shields.io/badge/Framework-PyTorch-79FFE1)](https://pytorch.org)
![Computer Vision](https://img.shields.io/badge/Type-Computer%20Vision-79FFE1)
![Input](https://img.shields.io/badge/Input-JSON%20(string)-79FFE1)
![Output](https://img.shields.io/badge/Output-JSON%20(string)-79FFE1)

One of the most popular and most powerful computer vision algorithms in the field of real-time object detection. V5 version outperforms all the previous versions and got near to EfficientDet AP with higher FPS.


## Deploy 
Click a button to deploy a model with [Syndicai](https://syndicai.co).

[![Syndicai-Deploy](https://raw.githubusercontent.com/syndicai/brand/main/button/deploy.svg)](https://app.syndicai.co/newModel?repository=https://github.com/syndicai/models/tree/master/pytorch/yolov5)



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