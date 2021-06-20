from controller.download_image import DownloadImage

import os

dir_path = os.path.dirname(os.path.realpath(__file__))
download_path = dir_path+'//download/'

path = input("name file excel: ")

download_image = DownloadImage()

download_image.readFile(dir_path+'\excel\\'+path+'.xlsx', download_path)