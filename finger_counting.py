import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
cap.set(4, 720)
cap.set(3, 1280)

detector = HandDetector(detectionCon=0.8, maxHands=2)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)

    # Detect hands without automatic drawing
    hands, img = detector.findHands(img, draw=False, flipType=True)

    if hands:
        for hand in hands:
            lmList = hand["lmList"]  # Landmark points
            connections = detector.mpHands.HAND_CONNECTIONS  # Hand connections

            # Draw hand connections
            for conn in connections:
                pt1, pt2 = lmList[conn[0]][:2], lmList[conn[1]][:2]
                cv2.line(img, pt1, pt2, (255, 255, 255), 2)

            # Draw landmarks
            for lm in lmList:
                cv2.circle(img, tuple(lm[:2]), 5, (0, 0, 255), -1)  # Red landmarks

        hand1 = hands[0]
        lmList1 = hand1["lmList"]
        fingers1 = detector.fingersUp(hand1)
        connections = detector.mpHands.HAND_CONNECTIONS

        if len(hands) == 2:
            hand2 = hands[1]
            lmList2 = hand2["lmList"]
            fingers2 = detector.fingersUp(hand2)
            cv2.putText(img, f"Number of Fingers Up: {str(fingers1.count(1) + fingers2.count(1))}", (50, 150), cv2.FONT_HERSHEY_COMPLEX, 1, (43, 25, 100), 2)
        else:
            cv2.putText(img, f"Number of Fingers Up: {str(fingers1.count(1))}", (50, 150), cv2.FONT_HERSHEY_COMPLEX, 1, (43, 25, 100), 2)
    else:
        cv2.putText(img, "Number of Fingers Up: None", (50, 150), cv2.FONT_HERSHEY_COMPLEX, 1, (43, 25, 100), 2)

    cv2.imshow("Counting Fingers", img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
