import glob
from matplotlib import pyplot as plt
import csv
import cv2

CSV_PATH = 'allParkinsons_test.csv'
img_array = []


with open(CSV_PATH) as csvfile:
    read_csv_ = csv.reader(csvfile, delimiter=',')
    bbox_list = list(read_csv_)

for img_num in sorted(glob.glob('parkinson_test/*.jpg')):
    x,y,xw,yh = bbox_list.pop(0)
    x = int(x)
    y = int(y)
    xw = int(xw)
    yh = int(yh)
    image = cv2.imread(img_num)
    height, width, layers = image.shape
    size = (width, height)
    
    cv2.rectangle(image,(x,y),(xw,yh),(0,0,0),2)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(image,'Checking Bbox - IMG:',(20,100), font, 1,(255,0,0),2,cv2.LINE_AA)
    cv2.putText(image,img_num,(20,130), font, 1,(255,125,110),2,cv2.LINE_AA)
    
    img_array.append(image)

out = cv2.VideoWriter('project.avi',cv2.VideoWriter_fourcc(*'DIVX'), 1, size)
 
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()
