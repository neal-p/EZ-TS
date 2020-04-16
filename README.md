# AUTOTS
Automatic Azoarene Transition State Screening
git clone https://github.com/neal-p/AUTOTS.git
enter directory and run the ./init.sh to make autots tools easily accessible 

To setup workflow, in a directory of optimized log files, run 'autots-setup'
This will create the workflow architecture and set up all calculations with the default parameters set in /home/USER/autots/config.py
You can edit the default config, 
or change the settings of a particular workflow by editing the config file in the /someworkflow/utilities/config.py
To update input files in a workflow directory based on the /someworkflow/utilities/config.py file, run 're-configure'

To submit the workflow simply execute the start.sh script in the base workflow directory './start.sh'
