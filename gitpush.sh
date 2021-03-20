#!/usr/bin/env fish

git add .

read commitMessage

git commit -m "$commitMessage"

git push
