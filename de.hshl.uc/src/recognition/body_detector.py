import cv2
import mediapipe as mp
import numpy as np


class body_detector():

    def __init__(self, mode=False, complex=1, smooth_landmarks=True, segmentation=True, smooth_segmentation=True,
                 detectionCon=0.5, trackCon=0.5):

        self.mode = mode
        self.complex = complex
        self.smooth_landmarks = smooth_landmarks
        self.segmentation = segmentation
        self.smooth_segmentation = smooth_segmentation
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpDraw = mp.solutions.drawing_utils
        self.mpDrawStyle = mp.solutions.drawing_styles
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(self.mode, self.complex, self.smooth_landmarks, self.segmentation,
                                     self.smooth_segmentation, self.detectionCon, self.trackCon)

    def findPose(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)

        width = 1280
        height = 750

        black_image = np.zeros((height, width, 3), np.uint8)

        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(black_image, self.results.pose_landmarks,
                                           self.mpPose.POSE_CONNECTIONS,
                                           self.mpDraw.DrawingSpec(color=(245, 117, 66), thickness=5, circle_radius=2),
                                           self.mpDraw.DrawingSpec(color=(245, 66, 230), thickness=5, circle_radius=2))
        return black_image
