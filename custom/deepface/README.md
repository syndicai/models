# Deepface
[![Deepface](https://img.shields.io/badge/Framework-Deepface-79FFE1)](https://github.com/serengil/deepface)
![Computer Vision](https://img.shields.io/badge/Type-Computer%20Vision-79FFE1)

Analysis function under the DeepFace interface is used to find demography of a face. Model returns attribute such as age, gender, facial expression, and race predictions. 



## Deploy 
Click a button to deploy a model with [Syndicai](https://syndicai.co).

[![Syndicai-Deploy](https://raw.githubusercontent.com/syndicai/brand/main/button/deploy.svg)](https://app.syndicai.co/newModel?repository=https://github.com/syndicai/models/tree/master/custom/deepface)


## Example
| input | output |
| --- | --- |
| <img src="sample_data/matthew.jpg" width="410"> | `{"age": 26, "race": "white", "emotions": "happy", "gender": "Man"}` |


## Sample API
```bash
curl https://***.c1.syndic.ai \
    -X POST \
    -F "image=@sample_data/matthew.jpg"
```


## Reference
Code based on [Deepface](https://github.com/serengil/deepface)) implementation