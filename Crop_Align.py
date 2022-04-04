import cv2 as cv
import numpy as np
from deepface import DeepFace

class Crop_Align(object):
    """
    
        The class that has all method for crop and align the face
  
    """
    OPENCV = 0
    SSD = 1
    DLIB = 2
    MTCNN = 3
    RETINAFACE = 4
    MEDIAPIPE = 5
    
    
    

    
    def __init__(self, method =  "ssd" ) -> None:
        
        """
            Initialize the class with the method to be used to decect and align
            
            Parameters:
                method: The method to be used to detect and align the face
                Valid methods:['opencv', 'ssd', 'dlib', 'mtcnn', 'retinaface', 'mediapipe']
                
        """
        super().__init__()
        self.method = method
        if self.method.lower() == 'opencv':
            self.method = self.OPENCV
        elif self.method.lower() == 'ssd':
            self.method = self.SSD
        elif self.method.lower() == 'dlib':
            self.method = self.DLIB
        elif self.method.lower() == 'mtcnn':
            self.method = self.MTCNN
        elif self.method.lower() == 'retinaface':
            self.method = self.RETINAFACE
        elif self.method.lower() == 'mediapipe':
            self.method = self.MEDIAPIPE
        else:
            raise ValueError('The method is not valid')
        
    def crop(self, image_path, image_out):
        """
        This function crop and align imagem 
        
        Parameters: 
            image_path: The path of imagem to be cropped
            image_out: The path to out the image 
        """
        backends = ['opencv', 'ssd', 'dlib', 'mtcnn', 'retinaface', 'mediapipe']
        
        face = DeepFace.detectFace(img_path = image_path,
                               target_size = (224, 224), 
                               detector_backend = backends[self.method])
    
        face = cv.cvtColor(face, cv.COLOR_RGB2BGR)
        face = 255 * (face - face.min()) / (face.max() - face.min())
        face = np.array(face, np.int)
        cv.imwrite (image_out , face)

      
            
            
        
    
   
    




