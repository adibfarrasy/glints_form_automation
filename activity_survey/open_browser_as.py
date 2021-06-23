# BUSINESS RULES
# 
# 1. Open browser, then open the form link
# 2. Fill out the form by simulating keyboard presses, slightly randomize the answer
# 3. Submit the form
# 4. Once submitted, write a log for backtracing

import time
from datetime import date, datetime
import webbrowser
import keyboard
import json
from random import seed, random, choice

# INITIAL CONFIGURATION
with open('./config_as.json') as infile:
    config = json.load(infile)

LINK = config['link'] #https://airtable.com/shrwvRFqrdQmvkzR7
BROWSER = config['browser'] #firefox, google-chrome

# 1. Open browser, then open the form link
webbrowser.get(BROWSER).open(LINK)