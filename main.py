
from datetime import datetime

def calculate_duration(start, end):
    try:
        start_time = datetime.strptime(start, "%H:%M")
        end_time = datetime.strptime(end, "%H:%M")
    except ValueError:
        print("Invalid time format. Please use HH:MM (e.g., 09:30)")
        return None

    if end_time <= start_time:
        print("End time must be after start time.")
        return None

    duration = end_time - start_time
    return duration.seconds // 60



def save_session(subject, minutes):
    with open("data.csv", "a") as file:
        file.write(f"{subject},{minutes}\n")

def is_valid_subject(subject):
    return bool(subject.strip()) and any(char.isalnum() for char in subject)

print("Smart Study Time Analyzer")

subject = input("Enter subject: ").strip()

if not is_valid_subject(subject):
    print("Subject name must contain letters or numbers.")
    exit()

start = input("Start time (HH:MM): ")
end = input("End time (HH:MM): ")

minutes = calculate_duration(start, end)
save_session(subject, minutes)



print(f"You studied {subject} for {minutes} minutes.")

