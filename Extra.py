    
def crop_image(path,detector_number , out_path):
    #face detection and alignment
    face = DeepFace.detectFace(img_path = path, 
                           target_size = (224, 224), 
                           detector_backend = backends[detector_number])
    
    face = cv.cvtColor(face, cv.COLOR_RGB2BGR)
    face = 255 * (face - face.min()) / (face.max() - face.min())
    face = np.array(face, np.int)
    cv.imwrite (out_path , face)


def crop_image_ssd_dlib(path, detector_number, out_path):
    #face detection and alignment
    face = DeepFace.detectFace(img_path = path, 
                           target_size = (224, 224), 
                           detector_backend = backends[1])
    face = DeepFace.detectFace(img_path = path, 
                           target_size = (224, 224), 
                           detector_backend = backends[0])
    face = cv.cvtColor(face, cv.COLOR_RGB2BGR)
    face = 255 * (face - face.min()) / (face.max() - face.min())
    face = np.array(face, np.int)
    cv.imwrite (out_path , face)

for j in range(1,6):
    for i in range(4):
        print('data/00000'+ str(j) + 
                   '.jpg')
        try:
            crop_image('data/00000'+ str(j) + 
                   '.jpg',i, 'data/teste/00000'+ 
                   str(j) + '_'+backends[i]+'.jpg')    
        except Exception as e:
            print ("error: " + backends[i] + "msg: " + str(e))


for j in range(1,5):        

    print('data/00000'+ str(j) + 
                   '.jpg')
    try:
        crop_image_ssd_dlib ('data/00000'+ str(j) + 
                '.jpg',i, 'data/teste/00000'+ 
                str(j) + '_ssd_opencv.jpg')    
    except Exception as e:
        print ("error: _ssd_opencv msg: " + str(e))



