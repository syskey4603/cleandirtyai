import cv2 as cv

cam = cv.VideoCapture(0, cv.CAP_DSHOW)   
s, img = cam.read()
if s:
    cv.namedWindow("cam-test")
    cv.imshow("cam-test",img)
    cv.imwrite("filename.jpg",img)
else:
    print("No image detected. Please! try again")