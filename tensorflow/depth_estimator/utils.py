import os
import io
import cv2
import base64
import urllib
import numpy as np
from PIL import Image
from imageio import imread


def url_to_image(url):
	"""
    Download the image, convert it to a NumPy array,
    and then read it into OpenCV format.
    """
	resp = urllib.request.urlopen(url)
	image = np.asarray(bytearray(resp.read()), dtype="uint8")
	image = cv2.imdecode(image, cv2.IMREAD_COLOR)

	return image


def b64_to_image(img_base64):
	"""
	Convert base64 imge to a NumPy array,
	and then read it into OpenCV format.
	"""
	img = imread(io.BytesIO(base64.b64decode(img_base64)))
	image = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

	return image


def image_to_base64(image):
	"""
	Convert image from OpenCV format
	to base64 format.
	"""
	image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
	img = Image.fromarray(image)

	im_file = io.BytesIO()
	img.save(im_file, format="PNG")
	im_bytes = base64.b64encode(im_file.getvalue()).decode("utf-8") 

	return im_bytes
