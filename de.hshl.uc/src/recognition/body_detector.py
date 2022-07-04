import cv2
import mediapipe as mp
import numpy as np

from recognition.hand_detector import hand_detector


class body_detector():

    def __init__(self, mode=False, complex=1, smooth_landmarks=True, segmentation=True, smooth_segmentation=True,
                 detectionCon=0.5, trackCon=0.5):
        # save the input variables in local ones
        self.mode = mode
        self.complex = complex
        self.smooth_landmarks = smooth_landmarks
        self.segmentation = segmentation
        self.smooth_segmentation = smooth_segmentation
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        # save the drawing information (from mediapipe)
        self.mpDraw = mp.solutions.drawing_utils
        self.mpDrawStyle = mp.solutions.drawing_styles
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(self.mode, self.complex, self.smooth_landmarks, self.segmentation,
                                     self.smooth_segmentation, self.detectionCon, self.trackCon)
        # create hand detector
        self.hd = hand_detector()

    def findPose(self, img, draw=True):
        # convert to RGB
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # position and sizeof camera stream
        self.results = self.pose.process(imgRGB)
        # Window size
        width = 1280
        height = 750
        # Black screen to draw the landmarks on
        black_image = np.zeros((height, width, 3), np.uint8)
        black_image= self.hd.findHandsAB(img, black_image)

        # draw silhouette only if landmarks are not null
        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(black_image, self.results.pose_landmarks,
                                           self.mpPose.POSE_CONNECTIONS,
                                           # Farbe und Dicke sowie die Punktenradius zeichnen und festlegen, für Linien und anschließend für die Punkte
                                           self.mpDraw.DrawingSpec(color=(245, 117, 66), thickness=5, circle_radius=2),
                                           self.mpDraw.DrawingSpec(color=(245, 66, 230), thickness=5, circle_radius=2))
        return black_image
