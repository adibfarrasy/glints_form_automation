# BUSINESS RULES
# 1. Choose random time between 1600 to 1700 to fill out the form
# 2. Open browser, then open the form link
# 3. Fill out the form by simulating keyboard presses, slightly randomize the answer
# 4. Submit the form
# 5. Once submitted, write a log for backtracing

# TESTING
# Create a test form : DONE
# Developer test for 3 days
# Use on GA form for 3 days
# Ask GA (Alvin) if it works

import time
from datetime import date, datetime
import webbrowser
import keyboard
import json
from random import seed, random, choice

# INITIAL CONFIGURATION
with open('./config.json') as infile:
    config = json.load(infile)

LINK = config['link'] #sim: https://forms.gle/CD8ioQ7iu9MRUUtH9, real: https://forms.gle/KWfM9Ga63nQzc4qd8
MAX_DELAY = config['max_delay'] #ceiling waiting time, in seconds. 3600 is for 3600 seconds
BROWSER = config['browser'] #firefox, google-chrome

# 1. Choose random time between 1600 to 1700 to fill out the form
# BR1 WILL BE HANDLED IN TANDEM WITH AN OUTSIDE SCHEDULER
# BR1 RANDOMIZE EXECUTION TIME WITHIN 1 HOUR OF THIS CODE EXECUTING
seed(1)
time.sleep(random()*MAX_DELAY)

# 2. Open browser, then open the form link
webbrowser.get(BROWSER).open(LINK)