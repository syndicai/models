import os
import io
import base64
import cv2
import numpy as np

from PIL import Image
from imageio import imread
from pyimagesearch.face_blurring import anonymize_face_pixelate
from pyimagesearch.face_blurring import anonymize_face_simple


args = {
	"face": "./face_detector",
	"method": "simple",
	"blocks": 20,
	"confidence": 0.5
}

class PythonPredictor:

	def __init__(self, config):
		# load our serialized face detector model from disk
		print("[INFO] loading face detector model...")
		prototxtPath = os.path.sep.join([args["face"], "deploy.prototxt"])
		weightsPath = os.path.sep.join([args["face"],
			"res10_300x300_ssd_iter_140000.caffemodel"])
		self.net = cv2.dnn.readNet(prototxtPath, weightsPath)

	def predict(self, payload):
		# load the input image from disk, clone it, and grab the image spatial
		# dimensions
		img = imread(io.BytesIO(base64.b64decode(payload["base64"])))  # numpy array (width, hight, 3)
		image = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
		orig = image.copy()
		(h, w) = image.shape[:2]

		# construct a blob from the image
		blob = cv2.dnn.blobFromImage(image, 1.0, (300, 300),
			(104.0, 177.0, 123.0))

		# pass the blob through the network and obtain the face detections
		print("[INFO] computing face detections...")
		self.net.setInput(blob)
		detections = self.net.forward()

		# loop over the detections
		for i in range(0, detections.shape[2]):
			# extract the confidence (i.e., probability) associated with the
			# detection
			confidence = detections[0, 0, i, 2]

			# filter out weak detections by ensuring the confidence is greater
			# than the minimum confidence
			if confidence > args["confidence"]:
				# compute the (x, y)-coordinates of the bounding box for the
				# object
				box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
				(startX, startY, endX, endY) = box.astype("int")

				# extract the face ROI
				face = image[startY:endY, startX:endX]

				# check to see if we are applying the "simple" face blurring
				# method
				if args["method"] == "simple":
					face = anonymize_face_simple(face, factor=3.0)

				# otherwise, we must be applying the "pixelated" face
				# anonymization method
				else:
					face = anonymize_face_pixelate(face,
						blocks=args["blocks"])

				# store the blurred face in the output image
				image[startY:endY, startX:endX] = face
		
		image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
		img = Image.fromarray(image)

		im_file = io.BytesIO()
		img.save(im_file, format="PNG")
		im_bytes = base64.b64encode(im_file.getvalue()).decode("utf-8") 

		return im_bytes
