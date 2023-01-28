import cv2
import numpy
from pyzbar.pyzbar import decode

print(cv2.__version__)


# img = cv2.imread('frame.png')

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

tentativas = 0
myNewData = ''
myData = ''

while tentativas < 5:

    success, img = cap.read()
    for barcode in decode(img):
        # print(barcode.data)
        # print(myNewData)
        myData = barcode.data.decode('utf-8')
        # print(myData)

        pts = numpy.array([barcode.polygon], numpy.int32)
        pts = pts.reshape((-1, 1, 2))

        # pts = pts.r((-1, 1, 2))
        cv2.polylines(img, [pts], True, (255, 0, 255), 5)
        pts2 = barcode.rect
        cv2.putText(img, myData, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 255), 2)
        
        if myNewData == myData:
            tentativas += 1
            print(myData + ' ' + str(tentativas))
            
        myNewData = myData

    cv2.imshow('Result', img)
    cv2.waitKey(1)
    # print('foi ate aqui')
