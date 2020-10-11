# Black and white
[![Seldon](https://img.shields.io/badge/Engine-Seldon-F7B955)](https://www.seldon.io/)
[![OpenCV](https://img.shields.io/badge/Framework-OpenCV-79FFE1)](https://opencv.org/)
![Computer Vision](https://img.shields.io/badge/Type-Computer%20Vision-79FFE1)
![Input](https://img.shields.io/badge/Input-JSON%20(base64)-79FFE1)
![Output](https://img.shields.io/badge/Output-JSON%20(base64)-79FFE1)

The idea of that algorithm is to convert colorful image to black-and-white one using [OpenCV](https://opencv.org/) library and [Seldon Core](https://seldon.io).


## Deploy 
Click a button to deploy a model with [Syndicai](https://syndicai.co).

[![Syndicai-Deploy](https://raw.githubusercontent.com/syndicai/brand/main/button/deploy.svg)](https://app.syndicai.co/newModel?repository=https://github.com/syndicai/models/opencv/black_and_white)




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
