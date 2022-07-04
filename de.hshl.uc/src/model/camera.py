import numpy as np

import cv2


class Camera:
    def __init__(self, cam_num):
        self.cam_num = cam_num
        self.cap = cv2.VideoCapture(0)
        self.last_frame = np.zeros((1, 1))

    # Init Camera
    def initialize(self):
        self.cap = cv2.VideoCapture(self.cam_num)

    # Capture Loop
    def acquire_movie(self, num_frames):
        movie = []
        for i in range(num_frames):
            movie.append(self.get_frame())
        return movie

    # Set Brightens
    def set_brightness(self, value):
        self.cap.set(cv2.CAP_PROP_BRIGHTNESS, value)

    # Get the Brightness
    def get_brightness(self):
        return self.cap.get(cv2.CAP_PROP_BRIGHTNESS)

    # Close the camera stream
    def close_camera(self):
        self.cap.release()

    def __str__(self):
        return 'OpenCV Camera {}'.format(self.cam_num)


if __name__ == '__main__':
    cam = Camera(0)
    cam.initialize()
    print(cam)
    cam.close_camera()
