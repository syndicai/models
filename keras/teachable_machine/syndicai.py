import io
import base64
import tensorflow.keras
import numpy as np

from PIL import Image, ImageOps
from helpers import get_labels

model_path = 'data/keras_model.h5'
labels_path = 'data/labels.txt'


class PythonPredictor:
    
    def __init__(self, config):
        # Load the model
        self.model = tensorflow.keras.models.load_model(model_path)

    def predict(self, payload):
        """
        Run a model in order to predict what's

        :param X : base64, input image
        :return : list, classes with probabilities
        """

        # covert image to base64
        input_image = io.BytesIO(base64.b64decode(payload["base64"]))

        # Disable scientific notation for clarity
        np.set_printoptions(suppress=True)

        # Create the array of the right shape to feed into the keras model
        # The 'length' or number of images you can put into the array is
        # determined by the first position in the shape tuple, in this case 1.
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

        # Replace this with the path to your image
        image = Image.open(input_image)

        # read labels
        labels = get_labels(labels_path)

        #resize the image to a 224x224 with the same strategy as in TM2:
        #resizing the image to be at least 224x224 and then cropping from the center
        size = (224, 224)
        image = ImageOps.fit(image, size, Image.ANTIALIAS)

        #turn the image into a numpy array
        image_array = np.asarray(image)

        # Normalize the image
        normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

        # Load the image into the array
        data[0] = normalized_image_array

        # run the inference
        prediction = self.model.predict(data).tolist()[0]

        # combine output with provided labels, 
        # and convert prediciton to percentage
        output = {}
        for x in range(0, len(prediction)):
            output[labels[x]] = '{:.2f}%'.format(prediction[x]*100)

        return [output]
