import warnings
warnings.filterwarnings("ignore")

import os
import io
import sys
import base64
import random
import argparse
import math
import numpy as np

from PIL import Image
from imageio import imread
from keras import backend as K

import coco
import utils
import model as modellib
import visualize
from classes import class_names


# Root directory of the project
ROOT_DIR = os.getcwd()

# Directory to save logs and trained model
MODEL_DIR = os.path.join(ROOT_DIR, "logs")

# Local path to trained weights file
COCO_MODEL_PATH = os.path.join(ROOT_DIR, "mask_rcnn_coco.h5")


class PythonPredictor:
    def __init__(self, config):
        K.clear_session()

        if not os.path.exists(COCO_MODEL_PATH):
            utils.download_trained_weights(COCO_MODEL_PATH)

        class InferenceConfig(coco.CocoConfig):
            GPU_COUNT = 1
            IMAGES_PER_GPU = 1
        config = InferenceConfig()
        
        self.model = modellib.MaskRCNN(mode="inference", model_dir=MODEL_DIR, config=config)
        self.model.load_weights(COCO_MODEL_PATH, by_name=True)

    def predict(self, payload):
        image = imread(io.BytesIO(base64.b64decode(payload["base64"])))

        results = self.model.detect([image], verbose=1)
        
        # Get results and save them
        r = results[0]
        output_image = visualize.display_instances_and_save(image, 'sample_data/output_image.jpeg', 
            r['rois'], r['masks'], r['class_ids'], class_names, r['scores'])

        im_file = io.BytesIO()
        output_image.save(im_file, format="JPEG")
        im_bytes = im_file.getvalue()  # im_bytes: image in binary format.
        
        return base64.b64encode(im_bytes).decode("utf-8")
