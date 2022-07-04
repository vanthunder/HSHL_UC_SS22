from recognition import hand_detector


# class __init__():

# def __init__ (self):
# self.hand_detector = hand_detector
# self.gesture_detector = gesture_detector
# self.handlist = hand_detector.hand_detector.handlist


def main():
    hand = hand_detector
    list = hand.hand_detector.handList
    print('INIT LISTE: ', hand_detector.hand_detector.handList)
    hand.hand_detector.main(self=hand)
    print('INIT LISTE: ', hand_detector.hand_detector.handList, list)


if __name__ == "__main__":
    main()
