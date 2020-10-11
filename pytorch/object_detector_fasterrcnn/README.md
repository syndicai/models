# Faster RCNN Object Detector
[![Cortex](https://img.shields.io/badge/Engine-Cortex-F7B955)](https://www.cortex.dev/)
[![PyTorch](https://img.shields.io/badge/Framework-PyTorch-79FFE1)](https://pytorch.org)
![Computer Vision](https://img.shields.io/badge/Type-Computer%20Vision-79FFE1)
![Input](https://img.shields.io/badge/Input-JSON%20(url)-79FFE1)
![Output](https://img.shields.io/badge/Output-JSON%20(url)-79FFE1)

Faster R-CNN has two networks: region proposal network (RPN) for generating region proposals and a network using these proposals to detect objects. The main different here with Fast R-CNN is that the later uses selective search to generate region proposals. The time cost of generating region proposals is much smaller in RPN than selective search, when RPN shares the most computation with the object detection network. Briefly, RPN ranks region boxes (called anchors) and proposes the ones most likely containing objects. The architecture is as follows.. The model was built on top of [Cortex](https://www.cortex.dev/) engine using [PyTorch](https://pytorch.org) framework.


## Deploy 
Click a button to deploy a model with [Syndicai](https://syndicai.co).

[![Syndicai-Deploy](https://raw.githubusercontent.com/syndicai/brand/main/button/deploy.svg)](https://app.syndicai.co/newModel?repository=https://github.com/syndicai/models/pytorch/object_detector_fasterrcnn)




## Run Locally
Execute following commands in order to run a model locally. For more details please visit [Cortex Documentation](https://docs.cortex.dev/install).
```bash
# Install cortex
bash -c "$(curl -sS https://raw.githubusercontent.com/cortexlabs/cortex/0.19/get-cli.sh)"

# Deploy a model
cortex deploy

# Run model
curl http://localhost:8892 -X POST -H "Content-Type: application/json" -d @sample_data/sample_input.json
```

