from datetime import datetime

def get_time():
    now = datetime.now()
    return f"Current time: {now.strftime('%I:%M %p')}"

def get_date():
    now = datetime.now()
    return f"Today is {now.strftime('%A, %B %d, %Y')}"
