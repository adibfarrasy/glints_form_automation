# BUSINESS RULES
# 
# 1. Open browser, then open the form link
# 2. Fill out the form by simulating keyboard presses, slightly randomize the answer
# 3. Submit the form
# 4. Once submitted, write a log for backtracing

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
BROWSER = config['browser'] #firefox, google-chrome

# 1. Open browser, then open the form link
webbrowser.get(BROWSER).open(LINK)