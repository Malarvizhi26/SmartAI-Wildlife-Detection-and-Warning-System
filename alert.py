import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from database import save_alert
import config

def send_email(animal_name, confidence, timestamp):
    if not config.EMAIL_ENABLED:
        return False
    
    try:
        msg = MIMEMultipart()
        msg['From'] = config.SENDER_EMAIL
        msg['To'] = config.RECEIVER_EMAIL
        msg['Subject'] = f"⚠️ WILDLIFE ALERT: {animal_name.upper()} Detected!"
        
        body = f"""
        WILDLIFE DETECTION ALERT
        
        Animal Detected: {animal_name.upper()}
        Confidence Level: {confidence:.2%}
        Detection Time: {timestamp}
        
        Immediate action may be required!
        
        - Smart AI Wildlife Detection System
        """
        
        msg.attach(MIMEText(body, 'plain'))
        
        server = smtplib.SMTP(config.SMTP_SERVER, config.SMTP_PORT)
        server.starttls()
        server.login(config.SENDER_EMAIL, config.SENDER_PASSWORD)
        server.send_message(msg)
        server.quit()
        
        print("✅ Email alert sent successfully")
        return True
    except Exception as e:
        print(f"❌ Email failed: {e}")
        return False

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
    
    # Send email notification
    email_sent = send_email(animal_name, confidence, time)
    
    # Save to database
    save_alert(animal_name, confidence, email_sent=1 if email_sent else 0)
