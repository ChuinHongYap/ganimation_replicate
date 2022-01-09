"""
Image crop using face_recognition
1. IMG_PATH for input image path.
2. OUT_PATH for output image path.
"""

import face_recognition
from PIL import Image, ImageDraw
import numpy as np
import cv2
import matplotlib.pyplot as plt
import os

IMG_PATH = ""
OUT_PATH = ""

files = [file for file in os.listdir(IMG_PATH) if file.endswith('.jpg')]

for file in files:
    # Load image
    img = face_recognition.load_image_file(os.path.join(IMG_PATH, file))
    
    # Find all the faces and face encodings: (top, right, bottom, left)
    face_locations = face_recognition.face_locations(img)
    
    crop_img = img[face_locations[0][0]:face_locations[0][2], face_locations[0][3]:face_locations[0][1]]
    
    crop_img = cv2.cvtColor(crop_img, cv2.COLOR_BGR2RGB)
    
    crop_img = cv2.resize(crop_img, (128,128))

    cv2.imwrite(os.path.join(OUT_PATH, file), crop_img)
