import os
import io
import time
import base64
import functools

from PIL import Image
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub

from helpers import *
os.environ["TFHUB_DOWNLOAD_PROGRESS"] = "True"


class PythonPredictor:

    def __init__(self, config):
        # Import TF-Hub module
        self.hub_module = hub.load("https://tfhub.dev/captain-pool/esrgan-tf2/1")

    def predict(self, payload):
        # Preprocess image
        hr_image = preprocess_image(payload["image_b64"])

        # Run model
        fake_image = self.hub_module(hr_image)

        # convert to base64
        img = get_image(tf.squeeze(fake_image))
        im_file = io.BytesIO()
        img.save(im_file, format="PNG")
        im_bytes = base64.b64encode(im_file.getvalue()).decode("utf-8")

        return im_bytes
