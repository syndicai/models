import os
import base64
import matplotlib.pylab as plt
import numpy as np
import tensorflow as tf
from PIL import Image


def preprocess_image(image_b64):
    """ Loads image from base64 and preprocesses to make it model ready
        Args:
          image_b64: base64 image
    """
    hr_image = tf.image.decode_image(base64.b64decode(image_b64))
    # If PNG, remove the alpha channel. The model only supports
    # images with 3 color channels.
    if hr_image.shape[-1] == 4:
        hr_image = hr_image[..., :-1]
    hr_size = (tf.convert_to_tensor(hr_image.shape[:-1]) // 4) * 4
    hr_image = tf.image.crop_to_bounding_box(
        hr_image, 0, 0, hr_size[0], hr_size[1])
    hr_image = tf.cast(hr_image, tf.float32)
    return tf.expand_dims(hr_image, 0)


def get_image(image):
    """
      Return PIL Image
      Args:
        image: 3D image tensor. [height, width, channels]
        filename: Name of the file to save to.
    """
    if not isinstance(image, Image.Image):
        image = tf.clip_by_value(image, 0, 255)
        image = Image.fromarray(tf.cast(image, tf.uint8).numpy())
    return image
