from matplotlib import pyplot as plt
from matplotlib.pyplot import imshow, axis
from matplotlib.image import imread

image_path = 'DataSet/TestSet/IMG_1276.JPG'
image = imread(image_path)
imshow(image)
axis('off')
plt.show()