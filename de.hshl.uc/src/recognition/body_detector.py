import cv2
import mediapipe as mp
import numpy as np

from recognition.hand_detector import hand_detector


class body_detector():

    def __init__(self, mode=False, complex=1, smooth_landmarks=True, segmentation=True, smooth_segmentation=True,
                 detectionCon=0.5, trackCon=0.5):
        # Mitgelieferte Parameter in lokale Variablen speichern
        self.mode = mode
        self.complex = complex
        self.smooth_landmarks = smooth_landmarks
        self.segmentation = segmentation
        self.smooth_segmentation = smooth_segmentation
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        # Zeichnungsinformationen bekommen und in Variablen speichern
        self.mpDraw = mp.solutions.drawing_utils
        self.mpDrawStyle = mp.solutions.drawing_styles
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(self.mode, self.complex, self.smooth_landmarks, self.segmentation,
                                     self.smooth_segmentation, self.detectionCon, self.trackCon)
        # Hand detector erstellen
        self.hd = hand_detector()

    def findPose(self, img, draw=True):
        # Muss auf RGB umgewandelt werden
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # Von Kamerabild die Position erfassen
        self.results = self.pose.process(imgRGB)
        # Fenstergröße festlegen
        width = 1280
        height = 750
        # Schwarzes Bild erstellen
        black_image = np.zeros((height, width, 3), np.uint8)
        # Schwarzem Bild die Landmarks für die Hand zeichnen
        black_image= self.hd.findHandsAB(img, black_image)

        # Wenn landmarks von pose vorhanden sind, dann soll gezeichnet werden.
        if self.results.pose_landmarks:
            if draw:
                # Auf dem schwarzem Bild die syluette zeichnen
                self.mpDraw.draw_landmarks(black_image, self.results.pose_landmarks,
                                           self.mpPose.POSE_CONNECTIONS,
                                           # Farbe und Dicke sowie die Punktenradius zeichnen und festlegen, für Linien und anschließend für die Punkte
                                           self.mpDraw.DrawingSpec(color=(245, 117, 66), thickness=5, circle_radius=2),
                                           self.mpDraw.DrawingSpec(color=(245, 66, 230), thickness=5, circle_radius=2))
        return black_image
