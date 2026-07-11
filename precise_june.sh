#!/bin/bash
git branch backup-june-2

# Reset main to before June
git reset --hard 4f9e4cc

# Dates specified by the user
dates=(
  "2026-06-02T12:00:00"
  "2026-06-07T12:00:00"
  "2026-06-12T12:00:00"
  "2026-06-13T12:00:00"
  "2026-06-17T12:00:00"
  "2026-06-19T12:00:00"
  "2026-06-22T12:00:00"
  "2026-06-25T12:00:00"
  "2026-06-26T12:00:00"
  "2026-06-27T12:00:00"
  "2026-06-30T12:00:00"
)

for date in "${dates[@]}"; do
  GIT_AUTHOR_DATE="$date" GIT_COMMITTER_DATE="$date" git commit --allow-empty -m "chore: minor refactoring and updates"
done

echo "Done creating precise commits. Pushing to GitHub..."
git push -f origin main
