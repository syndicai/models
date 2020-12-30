import os
import io
import base64
import numpy as numpy

from imageio import imread
from PIL import Image
from PIL import ImageFilter
from ISR.models import RDN



class PythonPredictor:
    def __init__(self, config):
        #self.model = RRDN(weights='gans')
        self.model = RDN(weights='noise-cancel')   

    def predict(self, payload):
        
        # read image
        lr_img = imread(io.BytesIO(base64.b64decode(payload["base64"])))

        # run model
        sr_img = self.model.predict(lr_img)
        output_image = Image.fromarray(sr_img)

        # denoise image
        #output_image.filter(ImageFilter.SMOOTH_MORE)

        im_file = io.BytesIO()
        output_image.save(im_file, format="JPEG")
        im_bytes = im_file.getvalue()  # im_bytes: image in binary format.
        
        return base64.b64encode(im_bytes).decode("utf-8")