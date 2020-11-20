import os
import base64
import requests

from io import BytesIO
from PIL import Image, ImageDraw


def draw_box(img, boxes):
    """
    Draw boxes on the picture
    :param img : PIL Image object
    :param boxes : numpy array of size [number_of_boxes, 6]
    :return img : PIL Image object with rectangles
    """
    box = ImageDraw.Draw(img)
    for i in range(boxes.shape[0]):
        data = list(boxes[i])
        shape = [data[0], data[1], data[2], data[3]]
        box.rectangle(shape, outline ="#02d5fa", width=3)
    return img


def url_to_img(url):
    """
    Convert Url to PIL Image
    : param url : string with the link to the image
    : return : PIL Image object
    """
    response = requests.get(url)
    return Image.open(BytesIO(response.content))


def img_to_bytes(img):
    """
    Convert PIL image to base64
    :param img : PIL Image object
    :return string : image in the form of base64
    """
    buffered = BytesIO()
    img.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue())
    return img_str.decode("utf-8")