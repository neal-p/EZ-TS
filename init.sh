#!/bin/bash
cp autots-setup.sh ~/bin/autots-setup
chmod 777 ~/bin/autots-setup
cp re-configure.sh ~/bin/re-configure
chmod 777 ~/bin/re-configure
cp autots-update.sh ~/bin/autots-update
chmod 777 ~/bin/autots-update
chmod 777 *sh
cp autots-clean.sh ~/bin/autots-clean
chmod 777 ~/bin/autots-clean
sed -i "/#local workflow variables/i user='$USER@husky.neu.edu'" config.py
