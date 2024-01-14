#initially we need to find four points for both the camera to select spefic region like game board.

import json
f = open('database.json')
 
data = json.load(f)
print(data)

camera_in_front = data['front_wall_camera']
camera_near_wall = data['near_wall_camera']

class position_cal:
    import cv2
    import numpy as np
    
    def calculate(self):
        print("started")
        vd2 = self.cv2.VideoCapture(camera_in_front) # camera in front of wall
        vd1 = self.cv2.VideoCapture(camera_near_wall) # camera near wall
        ret2,image2 = vd2.read()
        
        f=1
        while f:
        
            ret1,image1 = vd1.read()               
            
            roi1= data['near_wall_roi']
            image1 = image1[int(roi1[1]):int(roi1[1]+roi1[3]),
                    int(roi1[0]):int(roi1[0]+roi1[2])]
            frame1 = self.cv2.cvtColor(image1,self.cv2.COLOR_BGR2HSV)
            mask = self.cv2.inRange(frame1,self.np.array([0,128,116]),self.np.array([12,255,255]))  #orange
            contours,heir = self.cv2.findContours(mask , self.cv2.RETR_EXTERNAL  ,self.cv2.CHAIN_APPROX_SIMPLE)  
            # self.cv2.imshow("dfd",mask)
            # self.cv2.waitKey(1)
            if len(contours)!=0:
                vd2 = self.cv2.VideoCapture(camera_in_front)
                ret2,image2 = vd2.read()
                f=0
                

        # while True:
        #     self.cv2.imshow(image2)
        #     self.cv2.waitKey(0)
                
        image2 = self.cv2.cvtColor(image2,self.cv2.COLOR_BGR2HSV)
        roi2=data['front_wall_roi']
        image2 = image2[int(roi2[1]):int(roi2[1]+roi2[3]),
                  int(roi2[0]):int(roi2[0]+roi2[2])]
        
        
        
        mask2 = self.cv2.inRange(image2,self.np.array([0,128,116]),self.np.array([12,255,255]))  #orange
        contours2,hei2 = self.cv2.findContours(mask2 , self.cv2.RETR_EXTERNAL  ,self.cv2.CHAIN_APPROX_SIMPLE)
        
        if contours2:
                for conts in contours2:
                    if self.cv2.contourArea(conts)>200:
                        self.cv2.drawContours(image2,conts,-1,(0,255,0),3)
                        x,y,w,h = self.cv2.boundingRect(conts)
                        self.cv2.rectangle(image2 ,(x,y) ,(x+w,y+h),(0,0,255) ,3)
                        a = len(image2)
                        b = len(image2[0])
                        if (x+w/2)<=(int(a/3)) and (y+h/2)<=(int(b/3)):
                                return  0
                        if ((x+w/2)>(int(a/3))and (x+w/2)<=(int(2*a/3))) and (y+h/2)<=(int(b/3)):
                                return  1
                        if (x+w/2)>(int(2*a/3)) and (y+h/2)<=(int(b/3)):
                                return  2

                        if (x+w/2)<=(int(a/3)) and ((y+h/2)>(int(b/3))and (y+h/2)<=(int(2*b/3))):
                                return  3
                        if ((x+w/2)>(int(a/3))and(x+w/2)<=(int(2*a/3)) )and ((y+h/2)>(int(b/3))and (y+h/2)<=(int(2*b/3))):
                                return  4
                        if (x+w/2)>(int(2*a/3)) and ((y+h/2)>(int(b/3))and (y+h/2)<=(int(2*b/3))):
                                return  5
                        if (x+w/2)<=(int(a/3)) and (y+h/2)>(int(2*b/3)):
                                return  6
                        if ((x+w/2)>(int(a/3))and(x+w/2)<=(int(2*a/3)) ) and (y+h/2)>(int(2*b/3)):
                                return  7
                        if (x+w/2)>(int(2*a/3)) and (y+h/2)>(int(2*b/3)):
                                return  8   
                        return 10
                        self.cv2.destroyAllWindows()
        else:
                return 10              


# mod = position_cal()
# print(mod.calculate())
