import requests

from io import BytesIO
from PIL import Image


def url_to_img(url):
    """
    Convert Url to PIL Image
    : param url : string with the link to the image
    : return : PIL Image object
    """
    response = requests.get(url)
    return Image.open(BytesIO(response.content))