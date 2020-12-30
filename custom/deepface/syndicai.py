from deepface import DeepFace
from PIL import Image


class PythonPredictor():

    def __init__(self, config):
        obj = DeepFace.analyze(img_path = "sample_data/matthew.jpg", 
                               actions = ['age', 'gender', 'race', 'emotion'])
    
    def predict(self, payload):
        img = Image.open(payload["image"].file)
        img.save('_image.jpeg', 'JPEG')
        obj = DeepFace.analyze(img_path = '_image.jpeg', 
                               actions = ['age', 'gender', 'race', 'emotion'])

        return {
            "age": obj["age"],
            "race": obj["dominant_race"],
            "emotions": obj["dominant_emotion"],
            "gender": obj["gender"]
        }