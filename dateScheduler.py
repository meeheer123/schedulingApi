import datetime

def schedule_interviews(candidate_data):
    # Initialize variables for scheduling
    current_date = datetime.date.today()
    start_time = datetime.time(9, 0)  # Start interviews at 9:00 AM
    end_time = datetime.time(17, 0)    # End interviews at 5:00 PM
    interview_duration = datetime.timedelta(hours=2)  # Interview duration is 2 hours
    break_duration = datetime.timedelta(minutes=30)    # Break duration is 30 minutes

    scheduled_interviews = []

    # Iterate through candidate data and schedule interviews
    while candidate_data:
        # If it's a weekend, move to the next Monday
        while current_date.weekday() >= 5:  # Saturday is 5, Sunday is 6
            current_date += datetime.timedelta(days=1)

        # Calculate available time slots for the day
        current_datetime = datetime.datetime.combine(current_date, start_time)
        available_slots = []
        while current_datetime + interview_duration <= datetime.datetime.combine(current_date, end_time):
            available_slots.append(current_datetime)
            current_datetime += interview_duration + break_duration

        # Schedule interviews for the day
        while available_slots and candidate_data:
            start_datetime = available_slots.pop(0)
            end_datetime = start_datetime + interview_duration
            candidate = candidate_data.pop(0)
            scheduled_interviews.append({
                'candidate': candidate,
                'date': current_date.strftime('%Y-%m-%d'),
                'start_time': start_datetime.strftime('%H:%M'),
                'end_time': end_datetime.strftime('%H:%M')
            })

        # Move to the next available day
        current_date += datetime.timedelta(days=1)

    return scheduled_interviews

# Example usage:
candidate_data = ["Candidate 1", "Candidate 2", "Candidate 3", "Candidate 4", "Candidate 5",
                  "Candidate 6", "Candidate 7", "Candidate 8", "Candidate 9", "Candidate 10"]
scheduled_interviews = schedule_interviews(candidate_data)
for interview in scheduled_interviews:
    print(interview)
