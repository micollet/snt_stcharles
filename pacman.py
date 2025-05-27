from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
nom_image = "pacman.png"
img = Image.new("RGB", (16, 16),(255,255,255))
#ligne 1
for i in range(7,11):
    img.putpixel((i,0),(255,255,0))
#ligne 2
for i in range(6,12):
    img.putpixel((i,1),(255,255,0))
#ligne 3
for i in range(5,13):
    img.putpixel((i,2),(255,255,0))
#ligne 4
for i in range(4,14):
    img.putpixel((i,3),(255,255,0))
#ligne 5
for i in range(3,13):
    img.putpixel((i,4),(255,255,0))
#ligne 6
for i in range(2,12):
    img.putpixel((i,5),(255,255,0))
#ligne 7
for i in range(2,11):
    img.putpixel((i,6),(255,255,0))
#ligne 8
for i in range(1,10):
    img.putpixel((i,7),(255,255,0))
###################################
### LIGNE 9 - 15 A COMPLETER
###
###################################

img.save(nom_image,"PNG")
im = mpimg.imread("pacman.png")
plt.imshow(im)
plt.axis("off")
plt.show()