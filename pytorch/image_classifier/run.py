import os
import argparse

from helpers import bytes_to_img
from syndicai import PythonPredictor


sample_data = "https://i.imgur.com/PzXprwl.jpg"
output_dir = "./output"
save_response = True


def run(opt):

    # Convert image url to JSON string
    sample_json = {"url": opt.image}

    # Run a model using PythonPredictor from syndicai.py
    model = PythonPredictor([])
    response = model.predict(sample_json)

    # Save output image locally 
    if opt.save:

        # Convert base64 to .JPEG
        img, format = bytes_to_img(response)

        # Create output dir
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        # Save image
        img_name = f"output.{format}"
        img.save(os.path.join(output_dir, img_name))

    # Print a response in the terminal
    if opt.response:
        print(response)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--image', default=sample_data, type=str, help='URL to a sample input data')
    parser.add_argument('--save', action='store_true', help='Save output image in the ./output directory')
    parser.add_argument('--response', default=True, type=bool, help='Print a response in the terminal')
    opt = parser.parse_args()
    run(opt)