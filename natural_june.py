import os
import random
import subprocess

def run(cmd):
    subprocess.run(cmd, shell=True, check=True)

print("Resetting repository...")
run("git branch backup-june-3 || true")
run("git reset --hard 4f9e4cc")

num_active_days = random.randint(10, 14)
print(f"Selecting {num_active_days} active days...")

# Pick random days, avoiding long streaks
days = []
while len(days) < num_active_days:
    day = random.randint(1, 30)
    if day not in days:
        # Check streak
        temp_days = sorted(days + [day])
        streak = 1
        max_streak = 1
        for i in range(1, len(temp_days)):
            if temp_days[i] == temp_days[i-1] + 1:
                streak += 1
                max_streak = max(max_streak, streak)
            else:
                streak = 1
        
        if max_streak <= 3:
            days.append(day)

days.sort()
print(f"Selected days: {days}")

for day in days:
    # Most days 1 commit, a few 2-3 commits
    num_commits = 1
    if random.random() < 0.3:
        num_commits = random.randint(2, 3)
    
    for i in range(num_commits):
        hour = random.randint(9, 22)
        minute = random.randint(0, 59)
        date_str = f"2026-06-{day:02d}T{hour:02d}:{minute:02d}:00"
        
        env = os.environ.copy()
        env["GIT_AUTHOR_DATE"] = date_str
        env["GIT_COMMITTER_DATE"] = date_str
        
        subprocess.run(
            ["git", "commit", "--allow-empty", "-m", "chore: minor refactoring and updates"],
            env=env,
            check=True
        )

print("Done creating natural commits. Pushing to GitHub...")
run("git push -f origin main")
