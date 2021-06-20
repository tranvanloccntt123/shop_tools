from PIL import Image
from controller.render_mookup import Render
import os
render_image = Render()
dir_path = os.path.dirname(os.path.realpath(__file__))
crop_path = dir_path+'//crop/'
mock_path = dir_path+'//mock/'
mockup_path = dir_path+'//mockup/'
list_file = []
for filename in os.listdir(crop_path):
    list_file.append(filename)

for filename in os.listdir(mock_path):
    render_image.setBackground(mock_path+"/"+filename)
    #width:  height:  x:  y: 
    x = 585
    y = 483
    width = 450
    height = 600
    render_image.setPositionImportForground(x, y, width, height)
    for forground in list_file:
        render_image.setForground(crop_path+"/"+forground)
        render_image.scaleForground()
        render_image.paste(mockup_path+"/"+filename.replace(".png","")+forground)