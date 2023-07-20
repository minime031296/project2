#1st sketch using user image
import sketchpy
from sketchpy import library as lib
from sketchpy import canvas
obj = canvas.sketch_from_image(r"C:\Users\Admin\Desktop\robby.jpg")#can change the image by just using image file
obj.draw(threshold=50 )


# #2rd sketch using built-in bts--->v

# from sketchpy import library as lib
# obj = lib.bts()
# obj.draw()


# #3rd sketch using built-in rdj 


# from sketchpy import library as l
# image = l.rdj()
# image.draw()