from ultralytics import YOLO
import cv2
import numpy as np
from alert import send_alert
import winsound
import os
from database import init_db

# ---------------- INITIALIZE DATABASE ----------------
init_db()

# ---------------- STATES ----------------
sound_playing = False
alert_sent = False

# ---------------- LOAD MODEL ----------------
model = YOLO("yolov8n.pt")

# ---------------- DANGEROUS ANIMALS ----------------
DANGEROUS_ANIMALS = [
    "elephant", "bear", "zebra", "giraffe", "cow", "horse"
]

# ---------------- REAL-TIME CAMERA ----------------
cap = cv2.VideoCapture(0)  # 🔴 0 = default webcam

if not cap.isOpened():
    print("❌ Error: Camera not accessible")
    exit()

# ---------------- SIREN FILE ----------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SIREN_FILE = os.path.join(BASE_DIR, "siren.wav")

if not os.path.exists(SIREN_FILE):
    print("❌ siren.wav not found in project folder!")

confidence_threshold = 0.6

print("✅ REAL-TIME Wildlife Detection Started")
print("🎥 Camera ON")
print("➡ Press ESC to stop")

# ---------------- MAIN LOOP ----------------
while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Camera frame not received")
        break

    danger_detected = False

    # YOLO detection (real-time)
    results = model(frame, stream=True)

    for r in results:
        boxes = r.boxes
        names = r.names

        for box in boxes:
            cls_id = int(box.cls[0])
            conf = float(box.conf[0])

            if conf < confidence_threshold:
                continue

            label = names[cls_id]
            x1, y1, x2, y2 = map(int, box.xyxy[0])

            color = (0, 0, 255) if label in DANGEROUS_ANIMALS else (0, 255, 0)
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)

            cv2.putText(
                frame,
                f"{label} {conf:.2f}",
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                color,
                2
            )

            # ---------------- DANGER DETECTED ----------------
            if label in DANGEROUS_ANIMALS:
                danger_detected = True

                cv2.putText(
                    frame,
                    "⚠️ WARNING: DANGEROUS ANIMAL!",
                    (40, 50),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 0, 255),
                    3
                )

                # 🔊 START CONTINUOUS SIREN
                if not sound_playing and os.path.exists(SIREN_FILE):
                    winsound.PlaySound(
                        SIREN_FILE,
                        winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP
                    )
                    sound_playing = True

                # 📩 SEND ALERT ONLY ONCE
                if not alert_sent:
                    send_alert(label, conf)
                    alert_sent = True

    # ---------------- STOP SIREN ----------------
    if sound_playing and not danger_detected:
        winsound.PlaySound(None, winsound.SND_PURGE)
        sound_playing = False
        alert_sent = False

    cv2.imshow("Smart AI Wildlife Detection (REAL-TIME)", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC
        break

# ---------------- CLEANUP ----------------
cap.release()
cv2.destroyAllWindows()
winsound.PlaySound(None, winsound.SND_PURGE)
