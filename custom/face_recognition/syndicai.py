import os
import io
import base64
import face_recognition
import numpy as np
from PIL import Image, ImageDraw


class PythonPredictor:

    def __init__(self, config):
        # extract face features of the following person
        image_data = [['David Beckham', 'assets/face.jpg']]

        self.known_face_encodings = []
        self.known_face_names = []

        # Load a sample picture and learn how to recognize it.
        for person in image_data:
            person_name = person[0]
            person_file = person[1]

            person_image = face_recognition.load_image_file(person_file)
            person_face_encoding = face_recognition.face_encodings(person_image)[0]
            self.known_face_encodings.append(person_face_encoding)
            self.known_face_names.append(person_name)

    def predict(self, payload):
        check_image = io.BytesIO(base64.b64decode(payload["base64"]))

        # Load an image with an unknown face
        unknown_image = face_recognition.load_image_file(check_image)

        # Find all the faces and face encodings in the unknown image
        face_locations = face_recognition.face_locations(unknown_image)
        face_encodings = face_recognition.face_encodings(unknown_image, face_locations)

        # Convert the image to a PIL-format image so that we can draw on top of it with the Pillow library
        # See http://pillow.readthedocs.io/ for more about PIL/Pillow
        pil_image = Image.fromarray(unknown_image)
        # Create a Pillow ImageDraw Draw instance to draw with
        draw = ImageDraw.Draw(pil_image)

        # Loop through each face found in the unknown image
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)

            name = "Unknown"

            # Or instead, use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = self.known_face_names[best_match_index]

            # Draw a box around the face using the Pillow module
            draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 255))

            # Draw a label with a name below the face
            text_width, text_height = draw.textsize(name)
            draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0, 0, 255), outline=(0, 0, 255))
            draw.text((left + 6, bottom - text_height - 5), name, fill=(255, 255, 255, 255))


        # Remove the drawing library from memory as per the Pillow docs
        del draw

        # Display the resulting image
        #pil_image.save(output_file)

        im_file = io.BytesIO()
        pil_image.save(im_file, format="PNG")
        im_bytes = base64.b64encode(im_file.getvalue()).decode("utf-8") 

        return im_bytes
