from typing import ClassVar
import re
import pandas as pd
import requests

def handle(i, img, path, raito):
    try:
        response = requests.get(img)
        file = open(r""+path, "wb")
        file.write(response.content)
        file.close()
        print(str(round(i * raito, 2))+" %")
    except:
        print("FAIL: "+ str(i))


class DownloadImage:
    def __init__(self):
        self.data = []
    def readFile(self, path, download_path):
        data = pd.read_excel (r''+path) 
        df = pd.DataFrame(data, columns= ['title', 'image'])
        title = df.get('title')
        image = df.get('image')
        length = len(image)
        
        raito = 100 / length
        for i in range(0, length):
            path = re.sub(r'[^a-zA-Z0-9]', '%', title[i])
            handle(i, image[i], download_path+path+".png", raito)