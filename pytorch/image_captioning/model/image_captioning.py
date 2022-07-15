import torch
import re
from transformers import AutoTokenizer, ViTFeatureExtractor, VisionEncoderDecoderModel

from model.helpers import url_to_img


device = "cpu"
version = "nlpconnect/vit-gpt2-image-captioning"


class ImageCaptioning:

    def __init__(self):
        """
        Loads model
        """
        encoder_checkpoint = version
        decoder_checkpoint = version
        model_checkpoint = version
        self.feature_extractor = ViTFeatureExtractor.from_pretrained(encoder_checkpoint)
        self.tokenizer = AutoTokenizer.from_pretrained(decoder_checkpoint)
        self.model = VisionEncoderDecoderModel.from_pretrained(model_checkpoint).to(device)

    def run(self, image_url):
        """
        Runs the inference of the model.
        :param image_url : a string with the url to the image
        :returns : a string with the caption
        """
        image = url_to_img(image_url)
        image = self.feature_extractor(image, return_tensors="pt").pixel_values.to(device)
        clean_text = lambda x: x.replace('<|endoftext|>','').split('\n')[0]
        caption_ids = self.model.generate(image, max_length = 64)[0]
        caption_text = clean_text(self.tokenizer.decode(caption_ids))
        return caption_text
