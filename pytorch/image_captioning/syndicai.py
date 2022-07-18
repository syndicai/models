from model.image_captioning import ImageCaptioning

class PythonPredictor:

    def __init__(self, config):
        self.model = ImageCaptioning()

    def predict(self, payload):
        url = payload['url']
        output = self.model.run(url)
        return output