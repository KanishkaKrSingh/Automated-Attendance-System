import os
from ultralytics import YOLO
import subprocess
from matplotlib.pyplot import imshow, axis
from matplotlib.image import imread

HOME = os.getcwd()
print(HOME)
model = YOLO("yolov8n.yaml")  # build a new model from scratch
model = YOLO("yolov8n.pt")
# Run the yolov8n.pt model on the image
subprocess.run(['yolo', 'task=detect', 'mode=predict',
                'model=yolov8n.pt', 'conf=0.25', 'source=DataSet/TestSet/IMG_1276.JPG'], cwd=HOME)
image_path = os.path.join(HOME, 'runs/detect/predict/IMG_1276.JPG')
image = imread(image_path)
imshow(image)
axis('off')