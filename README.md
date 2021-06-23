# glints_form_automation
As part of Glints Academy Bootcamp activities, the participants must fill out a form daily. The activity turns out to be a chore, so I decided to automate the process.
This process is not fully automated, a user password (for sudo operation, the Python module `keyboard` requires it) and input are required at the start and end of the automatic filling out process.

## Installation
The program runs on Python and requires `keyboard` module.
- Install pip3: `sudo apt install pip3`
- Install keyboard: `sudo pip3 install keyboard`

## How to Use
1. Clone (but fork first!) this repo to your machine.
2. Navigate to the directory: `cd glints_form_automation`
3. Change shell permission for ./run.sh: `chmod +x run.sh`
4. Edit the config.json to your personal detail
5. Run the shell script: `./run.sh`
6. The browser will open, wait until the terminal prompts 'Go to the browser, then press Ctrl+Shift+S to start...'
7. Open the GA Survey tab on the browser, press Ctrl+Shift+S.
