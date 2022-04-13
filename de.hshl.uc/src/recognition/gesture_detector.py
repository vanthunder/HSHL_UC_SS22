from src.recognition.hand_detector import hand_detector


class gesture_detector(hand_detector):

    def __init__(self):
        hand = hand_detector()
        hand.findPosition()
