from PIL import Image
import image_slicer

img = Image.open('2.JPG')

if img.size >= (4000, 4000):
    tiles = image_slicer.slice('2.JPG', 36 , save=False)
elif img.size >= (2000, 2000):
    tiles = image_slicer.slice('2.JPG', 25, save=False)
elif img.size >= (1000, 1000):
    tiles = image_slicer.slice('2.JPG', 16, save=False)
elif img.size >= (500, 500):
    tiles = image_slicer.slice('2.JPG', 9, save=False)
else:
    tiles = image_slicer.slice('2.JPG', 4, save=False)
image_slicer.save_tiles(tiles, directory='croppedtemp', prefix='2', format='JPG')
