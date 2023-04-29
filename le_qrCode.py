import cv2
import numpy
from pyzbar.pyzbar import decode


class LeQrCode:

    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.cap.set(3, 640)
        self.cap.set(4, 480)
        self.pastData = ''
        self.myData = ''
        self.index = 0

    def inicia_captura(self):

        while self.index < 3:
            success, img = self.cap.read()
            for barcode in decode(img):
                # print(barcode.data)
                self.myData = barcode.data.decode('utf-8')
                self.pastData = self.myData
                pts = numpy.array([barcode.polygon], numpy.int32)
                pts = pts.reshape((-1, 1, 2))
                # pts = pts.r((-1, 1, 2))
                cv2.polylines(img, [pts], True, (255, 0, 255), 5)
                pts2 = barcode.rect
                cv2.putText(img, self.myData, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 255), 2)

                if self.myData == self.pastData:
                    self.index += 1
                    print(self.myData)

            cv2.imshow('Result', img)
            cv2.waitKey(1)

        return self.myData
