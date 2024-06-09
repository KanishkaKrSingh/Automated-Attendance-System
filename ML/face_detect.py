import os
from ultralytics import YOLO
import subprocess
from matplotlib.pyplot import imshow, axis
from matplotlib.image import imread
import cv2

HOME = os.getcwd()
print(HOME)

# Load the YOLOv8n model with face detection class
model = YOLO("yolov8n.yaml", classes=[0])  # class 0 is the face class

# Run the yolov8n.pt model on the image
subprocess.run(['yolo', 'task=detect', 'ode=predict',
                'odel=yolov8n.pt', 'conf=0.25', 'ource=DataSet/TestSet/IMG_1276.JPG'], cwd=HOME)

image_path = os.path.join(HOME, 'runs/detect/predict/IMG_1276.JPG')
image = imread(image_path)

# Load the image using OpenCV for face detection
img = cv2.imread(image_path)

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Initialize the face detector
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Detect faces in the image
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Draw rectangles around the detected faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Display the output
imshow(img)
axis('off')