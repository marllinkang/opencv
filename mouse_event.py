
import cv2
import numpy as np

img = np.ones((512,512,3), np.uint8)

def  draw_circle(event,x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN: #마우스 왼쪽 누르며 안에 색이 차있는 원이 만들어진다 bgr 이므로 블루
        cv2.circle(img,(x,y),30,(50,50,200),-1)
    if event == cv2.EVENT_RBUTTONDOWN: #마우스 오른쪽 누르며 안에 색이 차있는 원이 만들어진다 bgr 이므로 레드
        cv2.circle(img,(x,y),30,(200,50,50),-1)
cv2.namedWindow(winname='my_first_drawing')
cv2.setMouseCallback('my_first_drawing',draw_circle, img)

while True:
    cv2.imshow('my_first_drawing',img)

    if cv2.waitKey(10) == 27:
        break
        
cv2.destroyAllWindows()


