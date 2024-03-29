def add_time(start, duration, start_day=None):
# Parse start time
start_time, period = start.split()
start_hour, start_minute = map(int, start_time.split(':'))
if period == 'PM':
    start_hour += 12

# Parse duration
duration_hour, duration_minute = map(int, duration.split(':'))

# Calculate total minutes
total_minutes = start_hour * 60 + start_minute + duration_hour * 60 + duration_minute

# Calculate new time
new_hour = total_minutes // 60 % 24
new_minute = total_minutes % 60

# Determine period (AM or PM) and adjust hour if necessary
if new_hour >= 12:
    new_period = 'PM'
    if new_hour > 12:
        new_hour -= 12
else:
    new_period = 'AM'
    if new_hour == 0:
        new_hour = 12

# Calculate number of days later
days_later = total_minutes // (24 * 60)

# Determine the day of the week if provided
if start_day:
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    start_day_index = days_of_week.index(start_day.lower().capitalize())
    new_day_index = (start_day_index + days_later) % 7
    new_day = days_of_week[new_day_index]
    if days_later == 0:
        result = f"{new_hour}:{new_minute:02d} {new_period}, {new_day}"
    elif days_later == 1:
        result = f"{new_hour}:{new_minute:02d} {new_period}, {new_day} (next day)"
    else:
        result = f"{new_hour}:{new_minute:02d} {new_period}, {new_day} ({days_later} days later)"
else:
    if days_later == 0:
        result = f"{new_hour}:{new_minute:02d} {new_period}"
    elif days_later == 1:
        result = f"{new_hour}:{new_minute:02d} {new_period} (next day)"
    else:
        result = f"{new_hour}:{new_minute:02d} {new_period} ({days_later} days later)"

return result