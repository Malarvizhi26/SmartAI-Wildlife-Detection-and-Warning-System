import datetime

def send_alert(animal_name, confidence):
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    message = f"""
WILDLIFE ALERT
Animal Detected: {animal_name}
Confidence: {confidence:.2f}
Time: {time}
"""

    print(message)

    # Save alert to log file
    with open("alerts_log.txt", "a", encoding="utf-8") as file:
        file.write(message + "\n")
