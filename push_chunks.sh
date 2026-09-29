#!/bin/bash
git reset HEAD~1
for d in */; do
  if [ -d "$d" ]; then
    echo "Pushing $d..."
    git add "$d"
    git commit -m "Add $d" || true
    git push || true
  fi
done
git add .
git commit -m "Add remaining files" || true
git push || true
