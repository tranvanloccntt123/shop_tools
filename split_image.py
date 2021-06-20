from PIL import Image
from controller.filter_object import FilterImage
import os
filter_image = FilterImage()
dir_path = os.path.dirname(os.path.realpath(__file__))
crop_path = dir_path+'//crop/'
download_path = dir_path+'//download'
list_file = []
for filename in os.listdir(download_path):
    filter_image.setImage(download_path+'/'+filename)
    dir_save_file = crop_path+'/'+filename
    objs = filter_image.getObjectsInImage()
    if len(objs) > 100:
        continue
    size = filter_image.getSize(objs[0])
    position = filter_image.FindSubImage(objs[0])
    startY = position[1]
    startX = position[0]
    endY = startY + size[0]
    endX = startX + size[1]
    for obj in objs:
        position = filter_image.FindSubImage(obj)
        size = filter_image.getSize(obj)
        if position[1] < startY:
            startY = position[1]
        if position[0] < startX:
            startX = position[0]
        if position[1] + size[0] > endY:
            endY = position[1] + size[0]
        if position[0] + size[1] > endX:
            endX = position[0] + size[1]
    
    filter_image.save(dir_save_file, startY, endY, startX, endX)
    
    