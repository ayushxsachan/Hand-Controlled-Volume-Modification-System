import cv2
import numpy as np
import math
import hand_tracking_module as htm
from pycaw.pycaw import AudioUtilities

# Webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

# Hand Detector
detector = htm.HandDetector()

# Volume Setup (FIXED)
devices = AudioUtilities.GetSpeakers()
volume = devices.EndpointVolume

volMin, volMax = volume.GetVolumeRange()[:2]

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img)

    if len(lmList) != 0:
        # Thumb tip
        x1, y1 = lmList[4][1], lmList[4][2]
        # Index tip
        x2, y2 = lmList[8][1], lmList[8][2]

        # Draw circles
        cv2.circle(img, (x1, y1), 10, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 10, (255, 0, 255), cv2.FILLED)

        # Draw line
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

        # Distance
        length = math.hypot(x2 - x1, y2 - y1)

        # Convert to volume
        vol = np.interp(length, [30, 200], [volMin, volMax])
        volBar = np.interp(length, [30, 200], [400, 150])
        volPer = np.interp(length, [30, 200], [0, 100])

        volume.SetMasterVolumeLevel(vol, None)

        # UI
        cv2.rectangle(img, (50, 150), (85, 400), (0, 255, 0), 3)
        cv2.rectangle(img, (50, int(volBar)), (85, 400), (0, 255, 0), cv2.FILLED)

        cv2.putText(img, f'{int(volPer)} %', (40, 450),
                    cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

        # Optional: visual feedback when fingers close
        if length < 30:
            cv2.circle(img, (int((x1+x2)/2), int((y1+y2)/2)),
                       15, (0, 255, 0), cv2.FILLED)

    cv2.imshow("Volume Control", img)

    if cv2.waitKey(1) & 0xFF == 27:
        break