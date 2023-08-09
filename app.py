import os
import cv2

path = r"C:\Users\rskch\Desktop\Python\Project 105\Images"
images = []

for file in os.listdir(path):
    name, ext = os.path.splitext(file)
    if ext in ['.jpg','.png','.jpeg','jfif']:
        file_name = path +"/"+ file
        print(file_name)
        images.append(file_name)

print(len(images))
count = len(images)
frame = cv2.imread(images[0])
height,width,color = frame.shape
newVideo = cv2.VideoWriter("friends.avi",cv2.VideoWriter_fourcc(*'DIVX'),0.8,(height,width))
for x in range(0,count-1,1):
    frame = cv2.imread(images[x])
    newVideo.write(frame)
newVideo.release()