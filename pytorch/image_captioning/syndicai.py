from model.image_captioning import ImageCaptioning

class PythonPredictor:

    def __init__(self, config):
        self.mode = ImageCaptioning()

    def predict(self, payload):
        url = payload['url']
        output = self.mode.run(url)
        return output
