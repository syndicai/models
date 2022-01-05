# This must be the first call in order to work properly!
import os
import io
import base64
import urllib.request
from deoldify import device
from deoldify.device_id import DeviceId
device.set(device=DeviceId.GPU0)

import torch

if not torch.cuda.is_available():
    print('GPU not available.')

import fastai
from deoldify.visualize import *
import warnings
warnings.filterwarnings("ignore", category=UserWarning, message=".*?Your .*? set is empty.*?")


artistic=True


class PythonPredictor:
    
    def __init__(self, config):
        if artistic:
            url = "https://data.deepai.org/deoldify/ColorizeArtistic_gen.pth"
            model_path = "./models/ColorizeArtistic_gen.pth"
        else:
            url = "https://www.dropbox.com/s/usf7uifrctqw9rl/ColorizeStable_gen.pth?dl=1"
            model_path = "./models/ColorizeStable_gen.pth"

        if not os.path.exists(model_path):
            urllib.request.urlretrieve(url, model_path)
            
        self.colorizer = get_image_colorizer(artistic=artistic)
    
    def predict(self, payload):
        
        render_factor = 19  #@param {type: "slider", min: 7, max: 40}
        
        img = self.colorizer.plot_transformed_image_from_url(url=payload["url"],
                                                         render_factor=render_factor)
        
        im_file = io.BytesIO()
        img.save(im_file, format="PNG")
        im_bytes = base64.b64encode(im_file.getvalue()).decode("utf-8") 

        return im_bytes