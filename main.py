import cv2
import face_recognition
import numpy as np

imgElon = face_recognition.load_image_file("ImageBasic/Elon Musk.jpg")
imgElon = cv2.cvtColor(imgElon, cv2.COLOR_BGR2RGB)


