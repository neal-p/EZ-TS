#!/bin/bash
cd /home/$USER/autots
git reset --hard
git pull origin
bash init.sh
echo "AUTOTS up to date"
