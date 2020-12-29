import cv2
import numpy as np
import urllib.request
import matplotlib.pyplot as plt

import tensorflow as tf
import tensorflow_hub as hub

from utils import *


class PythonPredictor:

    def __init__(self, config):
        # the runtime initialization will not allocate all memory on the device to avoid out of GPU memory
        gpus = tf.config.experimental.list_physical_devices('GPU')
        for gpu in gpus:
            #tf.config.experimental.set_memory_growth(gpu, True)
            tf.config.experimental.set_virtual_device_configuration(gpu,
        [tf.config.experimental.VirtualDeviceConfiguration(memory_limit=4000)])

        # load model
        self.module = hub.load("https://tfhub.dev/intel/midas/v2_1_small/1", tags=['serve'])

    def predict(self, payload):
        # convert base64 to OpenCv format
        img = b64_to_image(payload["image_b64"]) / 255.0

        img_resized = tf.image.resize(img, [256,256], method='bicubic', preserve_aspect_ratio=False)
        img_resized = tf.transpose(img_resized, [2, 0, 1])
        img_input = img_resized.numpy()
        reshape_img = img_input.reshape(1,3,256,256)
        tensor = tf.convert_to_tensor(reshape_img, dtype=tf.float32)

        # run a model
        output = self.module.signatures['serving_default'](tensor)
        prediction = output['default'].numpy()
        prediction = prediction.reshape(256, 256)
                    
        # output file
        prediction = cv2.resize(prediction, (img.shape[1], img.shape[0]), interpolation=cv2.INTER_CUBIC)
        depth_min = prediction.min()
        depth_max = prediction.max()
        img_out = (255 * (prediction - depth_min) / (depth_max - depth_min)).astype("uint8")
        heatmap_img = cv2.applyColorMap(img_out, cv2.COLORMAP_HOT)

        return image_to_base64(heatmap_img)
