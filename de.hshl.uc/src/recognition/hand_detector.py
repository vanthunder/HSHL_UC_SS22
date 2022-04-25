import pathlib

import numpy as np
import pkg_resources
import cv2
import mediapipe as mp
import time
import keyboard
import os
from threading import Thread
from matplotlib import pyplot as plt
import random


class hand_detector:
    handlist = [1, 12]
    str = 'test'
    mode = False
    maxHands = 1
    detectionCon = 0.5
    modelComplex = 1
    trackCon = 0.5
    mpHands = mp.solutions.hands
    hands = mpHands.Hands(mode, maxHands, modelComplex, detectionCon, trackCon)
    mpDraw = mp.solutions.drawing_utils
    handList = [1, 2]

    def __init__(self, mode: object = False, maxHands: object = 1, detectionCon: object = 0.5, trackCon: object = 0.5,
                 modelComplexity: object = 1) -> object:
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.modelComplex = modelComplexity
        self.trackCon = trackCon
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.modelComplex, self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils
        self.handList = [1, 2]

    def findHands(self, img, draw=True):
        #print(img.dtype)
        img = np.uint8(img)
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        # print(self.results.multi_hand_landmarks)
        # print(self.results.multi_hand_world_landmarks)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img

    def intersection(self, lmList, x, y, start_Point, end_Point):
        # X Range
        x_wert = False
        y_wert = False

        for x in range(start_Point[0], end_Point[0]):
            if lmList[0].__getitem__(1) == x:
                x_wert = True
                break
            else:
                x_wert = False
        # Y Range
        for y in range(start_Point[1], end_Point[1]):
            if lmList[0].__getitem__(2) == y:
                y_wert = True
                break
            else:
                y_wert = False

        if (x_wert & y_wert):
            print("Intersection Y: True")
            print("Intersection X: True")
            return True

    def findPosition(self, img, handNo=0, draw=True):

        lmlist = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmlist.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 3, (255, 0, 255), cv2.FILLED)
        handlist = lmlist
        return lmlist

    def getLmlist(self):
        return self.lmList

    def circleLoadAnimation(img, ANGLE_DELTA):
        # Build it with rectangle?
        for angle in range(0, 360, ANGLE_DELTA):
            r = angle
            g = 0
            b = 0
            cv2.ellipse(img, (350, 350), (20, 20), 0, angle, angle + ANGLE_DELTA, (r, g, b), cv2.FILLED)

        return img

    def runloop(cap, detector):
        pTime = 0
        cTime = 0
        x = 300
        y = 200
        color = (255, 0, 0)
        thickness = 2
        first_time = True
        t1 = 0
        t2 = 0
        dt = 0
        seconds_until_click = 2
        counter = 0
        startPoint = (1000, 100)
        endPoint = (1400, 300)
        enabale_webcam = False
        video = ""
        print("Bitte wählen Sie '0' für Webcam und '1' für ein Testvideo!")
        input1 = input('Wahl: ')
        if input1 == '1':
            enabale_webcam = False
            video = "hands.mp4"
            startPoint = (1000, 100)
            endPoint = (1400, 300)
        elif input1 == '0':
            enable_wbacam = True
            video = 0
            startPoint = (100, 100)
            endPoint = (300, 300)
        cap = cv2.VideoCapture(video)
        print(input1)
        print(video)

        ANGLE_DELTA = 360 // 8

        img = np.zeros((700, 700, 3), np.uint8)
        img[::] = 255

        plt.gcf().set_size_inches((8, 8))
        plt.imshow(img)
        plt.show()

        # TO-DO: detector Klasse übergeben!
        # CV2 Operation ausführen
        # Lmlist
        while cap.isOpened():
            # success, img = cap.read()
            img = detector.findHands(img)
            img = cv2.rectangle(img, startPoint, endPoint, color, thickness)
            # TO-DO Loading animation Circle
            lmlist = detector.findPosition(img)
            # Setze Globale Liste!
            handlist = lmlist
            hand_detector.handlist = lmlist
            print("Liste")

            if lmlist != 0:
                center = (int(lmlist[0].__getitem__(1)), int(lmlist[0].__getitem__(2)))
                img = cv2.circle(img, center, 20, (255, 255, 0), 2)
                img = hand_detector.circleLoadAnimation(img, ANGLE_DELTA=360 // 8)
                # TO-DO: Implement Timer
                if detector.intersection(lmlist, x, y, startPoint, endPoint) == True:
                    counter += 1
                    color = (255, 255, 40)

                    t1 = time.time()

                    # print(dt)
                    if dt >= seconds_until_click:
                        color = (0, 0, 255)
                        cv2.circle(img, (400, 400), 30, (0, 0, 0), cv2.FILLED)
                        # send a message

                    if first_time:
                        first_time = False
                    else:
                        dt += t1 - t2

                    t2 = t1
                else:
                    first_time = True
                    dt = 0
                    color = (255, 0, 0)
                    counter = 0
                    t1 = 0
                    t2 = 0
                    dt = 0
                    first_time = True

            cTime = time.time()
            fps = 1 / (cTime - pTime)
            pTime = cTime

            cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
            cv2.putText(img, "Press ' q ' to exit!", (10, 200), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)
            # cv2.putText(img, "Testfield", (x, y), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)

            cv2.imshow("Image", img)
            cv2.waitKey(1)
            if keyboard.is_pressed('q'):
                cap.release()
                cv2.destroyAllWindows()
                break

    def hand_detector_run(detector, img):
        #img.flags.writable = False
        hdt = hand_detector()
        pTime = 0
        cTime = 0
        x = 300
        y = 200
        color = (255, 0, 0)
        thickness = 2
        first_time = True
        t1 = 0
        t2 = 0
        dt = 0
        seconds_until_click = 2
        counter = 0
        startPoint = (1000, 100)
        endPoint = (1400, 300)
        # img = np.zeros((700, 700, 3), np.uint8)
        # img[::] = 255
        # #plt.gcf().set_size_inches((8, 8))
        # plt.imshow(img)
        # plt.show()
        # TO-DO: detector Klasse übergeben!
        # CV2 Operation ausführen
        img = detector.findHands(hdt, img)

        img = cv2.rectangle(img, startPoint, endPoint, color, thickness)

        # TO-DO Loading animation Circle
        lmlist = detector.findPosition(hdt, img)
        # Setze Globale Liste!
        handlist = lmlist
        hand_detector.handlist = lmlist
        if len(lmlist) != 0:
            center = (int(lmlist[0].__getitem__(1)), int(lmlist[0].__getitem__(2)))
            img = cv2.circle(img, center, 20, (255, 255, 0), 2)
            #img = hand_detector.circleLoadAnimation(img, ANGLE_DELTA=360 // 8)
            # TO-DO: Implement Timer
            if detector.intersection(hdt, lmlist, x, y, startPoint, endPoint) == True:
                counter += 1
                color = (255, 255, 40)

                t1 = time.time()

                # print(dt)
                if dt >= seconds_until_click:
                    color = (0, 0, 255)
                    cv2.circle(img, (400, 400), 30, (0, 0, 0), cv2.FILLED)
                    # send a message

                if first_time:
                    first_time = False
                else:
                    dt += t1 - t2

                t2 = t1
            else:
                first_time = True
                dt = 0
                color = (255, 0, 0)
                counter = 0
                t1 = 0
                t2 = 0
                dt = 0
                first_time = True

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        print('FPS: ',fps)
        #cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
        #cv2.putText(img, "Press ' q ' to exit!", (10, 200), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)
        # cv2.putText(img, "Testfield", (x, y), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)


        return img
    def find_hands_on_image(self, img):
        # TO -DO Intersection außerhalb der While Methode
        #hdt = self.hand_detector()
        x = 300
        y = 200
        color = (255, 0, 0)
        thickness = 2
        counter = 0
        startPoint = (1000, 100)
        endPoint = (1400, 300)
        img = self.findHands(self, img)
        img = cv2.rectangle(img, startPoint, endPoint, color, thickness)
        lmlist = self.findPosition(self, img)
        handlist = lmlist
        hand_detector.handlist = lmlist
        if len(lmlist) != 0:
            center = (int(lmlist[0].__getitem__(1)), int(lmlist[0].__getitem__(2)))
            img = cv2.circle(img, center, 20, (255, 255, 0), 2)
            # img = hand_detector.circleLoadAnimation(img, ANGLE_DELTA=360 // 8)
            # TO-DO: Implement Timer
            if self.intersection(self, lmlist, x, y, startPoint, endPoint) == True:
                counter += 1
                color = (111,111,111)

        return img
def main(self):
    print("TRUE INI!!!!!!")
    detector = hand_detector()
    #cap = cv2.VideoCapture("hands.mp4")
    #success, img = cap.read()
   # detector.hand_detector_run(cap, img)




if __name__ == "__main__":
   main()
