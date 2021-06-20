from PIL import Image
import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt
import cv2

class FilterImage:
    def __init__(self):
        self.blur_radius = 1.0
        self.threshold = 0

    def setImage(self, path):
        self.img = Image.open(r""+path)
        self.img = np.asarray(self.img)

    def getObjectsInImage(self):
        # smooth the image (to remove small objects)
        imgf = ndimage.gaussian_filter(self.img, self.blur_radius)
        # find connected components
        labeled, nr_objects = ndimage.label(imgf > self.threshold)   
        objs = ndimage.find_objects(labeled)
        return objs

    def FindSubImage(self, obj):
        try:
            result = cv2.matchTemplate(self.img.astype(np.float32),self.img[obj].astype(np.float32),cv2.TM_CCOEFF_NORMED)
            y,x = np.unravel_index(result.argmax(), result.shape)
            return x,y
        except:
            return 0, 0


    def getSize(self, obj):
        try:
            y = len(self.img[obj])
            x = len(self.img[obj][0])
            return y,x
        except:
            print(self.img[obj])
            return 0, 0

    def save(self, path, startY, endY, startX, endX):
        try:
            img = self.img[startY : endY, startX : endX]
            data = Image.fromarray(img)
            data.save(r""+path)
            print("=============== done save =============")
        except:
            print("=============== fail save =============")