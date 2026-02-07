# Smart AI Wildlife Detection System

## Features
- Real-time wildlife detection using YOLOv8
- Email notifications for dangerous animals
- SQLite database for alert logging
- Streamlit web dashboard for monitoring

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Configure email in `config.py`:
   - Set your Gmail address
   - Generate App Password: https://myaccount.google.com/apppasswords
   - Set receiver email

3. Run detection system:
```bash
python app.py
```

4. Run web dashboard (in separate terminal):
```bash
streamlit run dashboard.py
```

## Email Setup (Gmail)
1. Go to Google Account settings
2. Enable 2-Factor Authentication
3. Generate App Password for "Mail"
4. Use that password in `config.py`

## Dashboard Access
Open browser: http://localhost:8501

## Database
- File: `wildlife_alerts.db`
- View alerts, statistics, and charts in dashboard
