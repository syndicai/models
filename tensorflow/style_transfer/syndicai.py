import os
import io
import base64
import functools

from PIL import Image
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub

from helpers import *


class PythonPredictor:

    def __init__(self, config):
        # Define style image
        self.style_image_url = 'https://upload.wikimedia.org/wikipedia/commons/c/c5/Edvard_Munch%2C_1893%2C_The_Scream%2C_oil%2C_tempera_and_pastel_on_cardboard%2C_91_x_73_cm%2C_National_Gallery_of_Norway.jpg'

        # Import TF-Hub module
        hub_handle = 'https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2'
        self.hub_module = hub.load(hub_handle)

    def predict(self, payload):
        # Define content image
        content_image_url = payload["image_url"]

        # Load images
        content_img_size = (500, 500)
        style_img_size = (300, 300)

        style_image = load_image(self.style_image_url, style_img_size)
        content_image = load_image(content_image_url, content_img_size)
        style_image = tf.nn.avg_pool(
            style_image, ksize=[3, 3], strides=[1, 1], padding='SAME')

        # Stylize content image with given style image.
        outputs = self.hub_module(tf.constant(content_image),
                                  tf.constant(style_image))
        stylized_image = outputs[0]

        # get PIL image and convert to base64
        img = Image.fromarray(np.uint8(stylized_image.numpy()[0] * 255))
        im_file = io.BytesIO()
        img.save(im_file, format="PNG")
        im_bytes = base64.b64encode(im_file.getvalue()).decode("utf-8")

        return im_bytes
