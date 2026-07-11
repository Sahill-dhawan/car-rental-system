#!/bin/bash
git branch backup-june

# Get the list of June commits from oldest to newest
commits=$(git log --since="2026-06-01" --until="2026-06-30" --format="%H" --reverse)

# Reset main to before June
git reset --hard 4f9e4cc

# Loop over the commits and cherry-pick randomly
for commit in $commits; do
  # 30% chance to keep the commit, 70% chance to skip
  if [ $((RANDOM % 10)) -lt 3 ]; then
    git cherry-pick --allow-empty $commit
  fi
done

echo "Done cherry-picking. Pushing to GitHub..."
git push -f origin main
