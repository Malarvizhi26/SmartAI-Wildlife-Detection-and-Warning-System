# Smart AI Wildlife Detection and Warning System

## Overview

The Smart AI Wildlife Detection and Warning System is an AI-based real-time surveillance system designed to detect wildlife using deep learning and computer vision techniques. The system helps reduce human–wildlife conflicts by automatically detecting animals and sending instant alerts to forest officers or nearby people.

This project is highly useful in forest borders, rural areas, highways near wildlife zones, and protected areas.

## Features

🧠 Real-time wildlife detection using YOLOv8

📷 Live camera / video feed processing

⚠️ Automatic email alerts for dangerous animals

🗂️ SQLite database for alert logging

📊 Streamlit dashboard for real-time monitoring

🌙 Works in different lighting and environmental conditions

## Tech Stack

Programming Language: Python

Deep Learning Model: YOLOv8

Computer Vision: OpenCV

Web Dashboard: Streamlit

Database: SQLite

Notification: SMTP (Email)

## Project Structure
Smart-AI-Wildlife-Detection/
│
├── app.py                 # Main real-time detection script
├── dashboard.py           # Streamlit dashboard
├── config.py              # Email configuration
├── requirements.txt       # Python dependencies
├── wildlife_alerts.db     # SQLite database
├── models/                # YOLOv8 trained model
├── assets/                # Sample images/videos
└── README.md              # Project documentation

## Installation
Step 1: Clone the Repository
git clone https://github.com/your-username/Smart-AI-Wildlife-Detection.git
cd Smart-AI-Wildlife-Detection

Step 2: Install Dependencies
pip install -r requirements.txt

## Email Configuration (Gmail)

Update config.py with the following:

Sender Gmail address

App Password (not normal password)

Receiver email address

## Generate App Password:
``` https://vizhifr2003@gmail.com/apppasswords ```

## Running the Project
Run Wildlife Detection
``` python app.py ```

Run Dashboard (New Terminal)
streamlit run dashboard.py

## Dashboard Access

Open your browser and go to:
```
http://localhost:8501
```

The dashboard shows:

### Detected animals output
![WhatsApp Image 2026-02-05 at 3 28 33 PM (1)](https://github.com/user-attachments/assets/d211ea45-cb80-44d4-b322-595efcb93507)


### Alert history output
<img width="578" height="460" alt="{498BA5BE-504E-4D32-B887-98E6990D5C3A}" src="https://github.com/user-attachments/assets/c5c23920-9fba-4ab4-9ad8-8d2121c9664b" />

Detection statistics and charts

##  Database Details

Database: wildlife_alerts.db

Stores:

Animal type

Detection time

Alert status

Used for monitoring and analytics

## Use Cases

Forest border monitoring

Wildlife intrusion detection

Accident prevention near highways

Smart surveillance systems

Wildlife conservation projects

## Future Enhancements

SMS & mobile app notifications

GPS-based animal tracking

Drone & IoT sensor integration

Cloud deployment

Multi-animal classification
