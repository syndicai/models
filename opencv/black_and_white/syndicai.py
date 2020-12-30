import io
import os
import base64
import numpy as np

from cv2 import cv2
from imageio import imread


class PythonPredictor:

    def __init__(self, config):
        pass

    def predict(self, payload):

        # base64 to OpenCV Image
        img_array = imread(io.BytesIO(base64.b64decode(payload["base64"])))
        img = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)

        # change color image to black & white
        grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # OpenCV to base64 image
        _, im_arr = cv2.imencode('.jpg', grayimg)
        img_base64 = base64.b64encode(im_arr.tobytes())

        return img_base64.decode("utf-8")