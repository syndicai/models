from model.image_captioning import ImageCaptioning


class PythonPredictor:
    
    def __init__(self, config):
        """(Required) 
        Called once before the API becomes available. Performs setup such as 
        downloading/initializing the model or downloading a vocabulary.
        :param config (required): a dictionary passed from API configuration 
                                  (if specified). This may contain information 
                                  on where to download the model and/or metadata.
        """
        self.image_captioning = ImageCaptioning()

    def predict(self, payload):
        """(Required) 
        Called once per request. Preprocesses the request payload (if necessary), 
        runs inference, and postprocesses the inference output (if necessary).
        :param payload (optional): The request payload with the json that consists 
                                   a url to the image.
        :returns : a string with the caption of the image.
        """
        image_url = payload["url"]
        output = self.image_captioning.run(image_url)
        return output