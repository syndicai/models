import torch
from PIL import Image 
from helpers import draw_box, url_to_img, img_to_bytes


class syndicai:

    def __init__(self):
        """ Download pretrained model. """
        self.model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True).autoshape()

    def predict(self, X, features_name=None):
        """ Run a model based on url input. """

        # Inference
        img = url_to_img(X)
        results = self.model(img)

        # Draw boxes
        return img_to_bytes(box_img)
