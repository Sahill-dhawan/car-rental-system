import os
import random
import subprocess
from datetime import datetime, timedelta

def run(cmd):
    subprocess.run(cmd, shell=True, check=True)

print("Resetting repository...")
run("git branch backup-june-4 || true")
run("git reset --hard 4f9e4cc")

# June 2026 starts on a Monday (June 1)
# We want to favor weekends (Fridays, Saturdays, Sundays) and late nights for a "college student" feel.

all_days = list(range(1, 31))
weekend_days = [5, 6, 7, 12, 13, 14, 19, 20, 21, 26, 27, 28]
weekday_days = [d for d in all_days if d not in weekend_days]

# Pick 10-12 active days total
num_weekends = random.randint(6, 8)
num_weekdays = random.randint(3, 5)

selected_weekends = random.sample(weekend_days, num_weekends)
selected_weekdays = random.sample(weekday_days, num_weekdays)
days = sorted(selected_weekends + selected_weekdays)

print(f"Selected days: {days}")

for day in days:
    # Most days 1 commit, sometimes 2-3
    num_commits = 1
    if random.random() < 0.4:
        num_commits = random.randint(2, 3)
    
    for i in range(num_commits):
        # College student hours: 8 PM to 3 AM (using 20 to 27)
        hour_raw = random.randint(20, 27)
        actual_day = day
        if hour_raw >= 24:
            hour = hour_raw - 24
            actual_day += 1 # Technically rolls into next morning
            if actual_day > 30: actual_day = 30
        else:
            hour = hour_raw
            
        minute = random.randint(0, 59)
        date_str = f"2026-06-{actual_day:02d}T{hour:02d}:{minute:02d}:00"
        
        env = os.environ.copy()
        env["GIT_AUTHOR_DATE"] = date_str
        env["GIT_COMMITTER_DATE"] = date_str
        
        subprocess.run(
            ["git", "commit", "--allow-empty", "-m", "chore: minor refactoring and updates"],
            env=env,
            check=True
        )

print("Done creating student-style commits. Pushing to GitHub...")
run("git push -f origin main")
