import io
import zipfile
import requests


def download_model(url, save_path):
    """
    Download model files.
    """
    r = requests.get(url)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall(save_path)