import time

import cv2
import numpy as np
import mediapipe as mp

from recognition.hand_detector import hand_detector




class gesture_detector(hand_detector):

    def __init__(self, lmList: object = []) -> object:
        self.lmList = lmList

    def writeLmList(self, lmList):
        self.lmList = lmList

    def print(self):
        print("")

