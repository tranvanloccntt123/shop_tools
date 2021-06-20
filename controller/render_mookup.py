from PIL import Image
import os
class Render:
    def setFolder(self, path):
        if os.path.exists(r""+path) == False:
            os.mkdir(r""+path)
    
    def setBackground(self, path):
        self.path = path
        
    def setForground(self, path):
        self.forground = Image.open(r""+path).convert("RGBA")

    def setPositionImportForground(self, x, y, width, height):
        self.x = int(x)
        self.y = int(y)
        self.width = int(width)
        self.height = int(height)

    def scaleForground(self):
        #self.forground.show()
        get_size = self.forground.size
        width = get_size[0]
        height = get_size[1]
        raito_height = width / height
        width = self.width
        height = int(width / raito_height)
        if height > self.height:
            height -= (height - self.height)
            width = int(raito_height * height)

        self.forground = self.forground.resize((width, height))
    
    def paste(self, path):
        img = Image.open(r""+self.path)
        forground_size =  self.forground.size
        x = self.x + int((self.width - forground_size[0]) / 2)
        img.paste(self.forground, (x, self.y), self.forground)
        img.save(r""+path)