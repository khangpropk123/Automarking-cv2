import cv2
import matplotlib.pyplot as plt
import numpy as np


img = cv2.imread('./AAAA.jpg', 0)
blur = cv2.GaussianBlur(img, (5, 5), 0)
thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2) #Convert Image To Binary
horizal = thresh
vertical = thresh


#
scale_height = 40  #
scale_long = 30

long = int(img.shape[1] / scale_long)
height = int(img.shape[0] / scale_height)

horizalStructure = cv2.getStructuringElement(cv2.MORPH_RECT, (long, 1))
horizal = cv2.erode(horizal, horizalStructure, (-1, -1))
horizal = cv2.dilate(horizal, horizalStructure, (-1, -1))

verticalStructure = cv2.getStructuringElement(cv2.MORPH_RECT, (1, height))
vertical = cv2.erode(vertical, verticalStructure, (-1, -1))
vertical = cv2.dilate(vertical, verticalStructure, (-1, -1))

mask = vertical + horizal

#Get Answer Table
contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print(len(contours))

max = -1
secc=-1
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    if cv2.contourArea(cnt) > max:
        x_max, y_max, w_max, h_max = x, y, w, h
        max = cv2.contourArea(cnt)
for cnt in contours:
    if cv2.contourArea(cnt) > 100 :
            a,b,c,d = cv2.boundingRect(cnt)
            if (round(cv2.contourArea(cnt))>round(secc) & round(secc) < round(max)):
                    secc = cv2.contourArea(cnt)   
obj= img[b:b+d,a:a+c]
thresh = cv2.adaptiveThreshold(obj, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
plt.imshow(obj)
plt.show()


cropped_thresh_img = []
cropped_origin_img = []
countours_img = []
_rows = []
_NUM_ROW = 8# Number of row
_START_COL = 1
_h_col = round(d/_NUM_ROW)
_w_row = round(c/10)
for i in range(0,_NUM_ROW):
        col = obj[i*_h_col:(i+1)*_h_col, 0:c]
        _rows.append(col)
        

result_mssv_1=[]   
result_mssv_2=[]
for row in _rows:
        total =[]
        for i in range(0, 10):
                thresh = cv2.adaptiveThreshold(col, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
                thresh1 = thresh[ 0: _h_col,
                       (i*_w_row) :(i+1)*_w_row]
                contours_thresh1, hierarchy_thresh1 = cv2.findContours(thresh1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                origin = row[ 0: _h_col,
                       (i*_w_row) :(i+1)*_w_row]
                cropped_thresh_img.append(thresh1)
                cropped_origin_img.append(origin)
                countours_img.append(contours_thresh1)
                answer = cv2.threshold(origin, 240, 255, cv2.THRESH_BINARY_INV)[1]
                total.append(cv2.countNonZero(answer))
        


                
    
        nd = np.argmax(total)
        result_mssv_1.append(nd);
print(result_mssv_1)
        
        
        

    
        
total_conntuor = []
j=0
for i, countour_img in enumerate(countours_img):
    for cnt in countour_img:
        if cv2.contourArea(cnt) > 30:
            x, y, w, h = cv2.boundingRect(cnt)
            if x > cropped_origin_img[i].shape[1] * 0.1 and x < cropped_origin_img[i].shape[1] * 0.9:
                answer = cropped_origin_img[i][y:y + h, x:x + w]
                answer = cv2.threshold(answer,240 , 255, cv2.THRESH_BINARY_INV)[1]
                total_conntuor.append(cv2.countNonZero(answer))
                j=j+1
                if(j%10==0):
                        nd = np.argmax(total_conntuor)
                        result_mssv_2.append(nd)
                        total_conntuor = []
print(result_mssv_2)
        



table = img[y_max:y_max + h_max, x_max:x_max + w_max]
table1 = table[0: h_max, 0:round(w_max/2)]
thresh01 = cv2.adaptiveThreshold(table, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
table2 = table[0: h_max, round(w_max/2): w_max]
thresh02 = cv2.adaptiveThreshold(table, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
plt.imshow(table1)
plt.show()
y_max=0;
x_max=0;
h_table =h_max
w_table= round(w_max/2)
cropped_thresh_img_1 = []
cropped_origin_img_1= []
countours_img_1 = []
cropped_thresh_img_2 = []
cropped_origin_img_2= []
countours_img_2 = []
rows1 = []
rows2 = []
NUM_ROW = 22# Number of row
START_COL = 1
h_col = round(h_max/NUM_ROW)
w_row_max = round(w_max/12)
w_row = w_row_max
for i in range(1,NUM_ROW-1):
        col = table1[i*h_col:(i+1)*h_col, w_row_max:w_row_max*5]
        rows1.append(col)
        plt.imshow(col)
        plt.show()
for i in range(1,NUM_ROW-1):
        col = table2[i*h_col:(i+1)*h_col, w_row_max:w_row_max*5]
        rows2.append(col)
        

result_1=[]   
result_2=[]
for row in rows1:
        total =[]
        for i in range(0,4):
                thresh01 = cv2.adaptiveThreshold(col, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 7, 3)
                thresh1 = thresh01[ 0: h_col,
                       (i*w_row) :(i+1)*w_row]
                contours_thresh1, hierarchy_thresh1 = cv2.findContours(thresh1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                origin1 = row[ 0: h_col,
                       (i*w_row) :(i+1)*w_row]
                cropped_thresh_img_1.append(thresh1)
                cropped_origin_img_1.append(origin1)
                countours_img_1.append(contours_thresh1)
                answer = cv2.threshold(origin1, 240, 255, cv2.THRESH_BINARY_INV)[1]
                total.append(cv2.countNonZero(answer))
                

                
    
        nd = np.argmax(total)
        result_1.append(nd);
for row in rows2:
        total =[]
        for i in range(0,4):
                thresh02 = cv2.adaptiveThreshold(col, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 7, 3)
                thresh2 = thresh02[ 0: h_col,
                       (i*w_row) :(i+1)*w_row]
                contours_thresh2, hierarchy_thresh2 = cv2.findContours(thresh1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                origin2 = row[ 0: h_col,
                       (i*w_row) :(i+1)*w_row]
                cropped_thresh_img_2.append(thresh2)
                cropped_origin_img_2.append(origin2)
                countours_img_2.append(contours_thresh2)
                answer = cv2.threshold(origin2,240, 255, cv2.THRESH_BINARY_INV)[1]
                total.append(cv2.countNonZero(answer))
               

                
    
        nd = np.argmax(total)
        result_1.append(nd);
print(result_1)
        
        
        

    
        
total_conntuor = []
j=0
for i, countour_img in enumerate(countours_img_1):
    for cnt in countour_img:
        if cv2.contourArea(cnt) >30:
            x, y, w, h = cv2.boundingRect(cnt)
            if x > cropped_origin_img_1[i].shape[1] * 0 and x < cropped_origin_img_1[i].shape[1] * 0.99:
                answer = cropped_origin_img_1[i][y:y + h, x:x + w]
                answer = cv2.threshold(answer, 240, 255, cv2.THRESH_BINARY_INV)[1]
                
                total_conntuor.append(cv2.countNonZero(answer))
                j=j+1
                if(j%4==0):
                        nd = np.argmax(total_conntuor)
                        result_2.append(nd)
                        total_conntuor = []
j=0
for i, countour_img in enumerate(countours_img_2):
    for cnt in countour_img:
        if cv2.contourArea(cnt) >30:
            x, y, w, h = cv2.boundingRect(cnt)
            if x > cropped_origin_img_2[i].shape[1] *0  and x < cropped_origin_img_2[i].shape[1]*0.9 :
                answer = cropped_origin_img_2[i][y:y + h, x:x + w]
                answer = cv2.threshold(answer, 240, 255, cv2.THRESH_BINARY_INV)[1]
                
                total_conntuor.append(cv2.countNonZero(answer))
                j=j+1
                if(j%4==0):
                        nd = np.argmax(total_conntuor)
                        result_2.append(nd)
                        total_conntuor = []

print(result_2)

