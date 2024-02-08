"""
Converts appointments from Calendar (macOS) to simple text format (German).

For more info see README.md

"""

from datetime import datetime

# Example input from Calendar (macOS)
# For import as TextExpander snippet, change the following line to:
# input_schedule = """"""%pasteboard""""""

input_schedule = """
Testtermin
Scheduled: 14. Feb 2024 at 10:45 to 11:45, CET

Testtermin
Scheduled: 15. Feb 2024 at 15:00 to 16:00, CET

Testtermin
Scheduled: 15. Feb 2024 at 17:00 to 18:00, CET
"""


scheduled_lines = [
    line for line in input_schedule.split("\n") if line.startswith("Scheduled:")
]

converted_schedule = []
for entry in scheduled_lines:
    # Extracting the date and time
    date_time_str = entry.split("Scheduled: ")[1].split(" to ")[0].strip()
    # Converting to datetime object
    date_time_obj = datetime.strptime(date_time_str, "%d. %b %Y at %H:%M")
    # Converting to German format
    german_format = date_time_obj.strftime("%A, %d.%m.%y, %H:%M Uhr")
    # Translate day to German
    german_days = {
        "Monday": "Montag",
        "Tuesday": "Dienstag",
        "Wednesday": "Mittwoch",
        "Thursday": "Donnerstag",
        "Friday": "Freitag",
        "Saturday": "Samstag",
        "Sunday": "Sonntag",
    }
    for eng_day, ger_day in german_days.items():
        german_format = german_format.replace(eng_day, ger_day)
    converted_schedule.append(german_format)


for item in converted_schedule:
    print(item)
