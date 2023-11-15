#!/bin/bash
git checkout dev
git add .
git commit -a -m $1
git push
git checkout main
git merge dev
git push
git checkout dev
