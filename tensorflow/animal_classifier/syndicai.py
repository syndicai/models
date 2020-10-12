import io
import sys
import os
import json
import base64
import numpy as np
import tensorflow as tf

from PIL import Image
from helpers import download_model

models_url = 'https://www.dropbox.com/s/emee1vxmoch4sbu/models.zip?raw=1'
checkpoint = 'mobilenet_v2_1.0_224'


class syndicai(object):
    def __init__(self):
        self._model = None
        download_model(models_url, os.getcwd())
        sys.path.append(os.path.abspath('./models/tensorflow/research/slim'))        

    def predict(self, X, features_names=None):
        
        img = np.array(Image.open(io.BytesIO(base64.b64decode(X))).resize((224, 224))).astype(np.float) / 128 - 1

        gd = tf.GraphDef.FromString(open( "models/mobilenet/"+ checkpoint +'_frozen.pb', 'rb').read())
        inp, predictions = tf.import_graph_def(gd,  return_elements = ['input:0', 'MobilenetV2/Predictions/Reshape_1:0'])

        with tf.Session(graph=inp.graph):
            y = predictions.eval(feed_dict={inp: img.reshape(1, 224,224, 3)})

        with open('models/imagenet-simple-labels.json') as f:
            labels = json.load(f)

        return [labels[y.argmax()]]


    def metrics(self):
        return [{"type": "COUNTER", "key": "mycounter", "value": 1}]