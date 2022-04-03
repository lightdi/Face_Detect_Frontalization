import cv2 as cv
import numpy as np
from deepface import DeepFace


backends = ['opencv', 'ssd', 'dlib', 'mtcnn', 'retinaface', 'mediapipe']

#face detection and alignment
face = DeepFace.detectFace(img_path = "data/000001.jpg", 
                           target_size = (224, 224), 
                           detector_backend = backends[1])

faceOrig = cv.imread('data/000001.jpg')
cv.imshow("face Orig", faceOrig)
face = cv.cvtColor(face, cv.COLOR_RGB2BGR)
cv.imshow("face", face)
face = 255 * (face - face.min()) / (face.max() - face.min())
face = np.array(face, np.int)
print("Deucerto: ",cv.imwrite ('data/rt000001.jpg', face))
cv.imshow("Deu face", face)
cv.waitKey(0)
print(face)

def crop_image(path, type, out):
    