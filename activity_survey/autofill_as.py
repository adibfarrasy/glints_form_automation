# BUSINESS RULES
# 1. Choose random time between 1600 to 1700 to fill out the form
# 2. Open browser, then open the form link
# 3. Fill out the form by simulating keyboard presses, slightly randomize the answer
# 4. Submit the form manually
# 5. Once program is done, write a log for backtracing


import time
from datetime import date, datetime
import webbrowser
import keyboard
import json
from random import seed, random, choice

# INITIAL CONFIGURATION
with open('./config_as.json') as infile:
    config = json.load(infile)

NAME = config['name']
NUM_OF_SCALE_QNS = config['num_of_scale_qns'] #3 bullet points in GA activity survey
SCORE_LIST = config['score_list']
MESSAGE = config['message']

# 3. Fill out the form by simulating keyboard presses, slightly randomize the answer
# INITIATE
print("""
What activity is the survey for?
00 - All Hands
01 - Career Next Steps
02 - English Express
03 - P2P Career Support
04 - Friday Social
05 - Office Hour
06 - Computer Science Fundamental Class
07 - Alumni Office Hour
08 - Alumni Gathering
09 - Alumni Talkshow
10 - Saturday Tech Workshop
""")

# ASK THE ACTIVITY TO BE FILLED OUT
while True:
    try: 
        activity = int(input("Choose the option 00-10..."))
    except ValueError:
        print("Invalid option. Try again.")
        continue
    if activity not in range(11):
        print("Invalid option. Try again.")
        continue
    else:
        break

print('Go to the browser, then press Ctrl+Shift+S to start...')
keyboard.wait('ctrl+shift+s')
time.sleep(0.3)
keyboard.press_and_release('tab')
time.sleep(0.1)
keyboard.press_and_release('enter')
time.sleep(0.3)

# FILL OUT NAME
keyboard.write(NAME)
time.sleep(0.1)
keyboard.press_and_release('enter')
time.sleep(0.5)
keyboard.press_and_release('tab')
time.sleep(0.5)

# FILL OUT ACTIVITY
if activity == 0:
    keyboard.press_and_release('tab')
    time.sleep(0.1)
else:
    for i in range(activity):
        keyboard.press_and_release('down')
        time.sleep(0.1)
        
keyboard.press_and_release('tab')
time.sleep(0.03)

# FILL OUT DATE
today = date.today()
keyboard.press_and_release('tab')
time.sleep(0.03)
keyboard.press_and_release('down')
time.sleep(0.03)
for i in range(4):
    keyboard.press_and_release('tab')
    time.sleep(0.03)
keyboard.press_and_release('enter')
time.sleep(0.5)

# FILL OUT THE LINEAR SCALE QNS
SCORE_LIST = SCORE_LIST[2:5] # ONLY GIVE GOOD REVIEW.
for i in range(NUM_OF_SCALE_QNS):
    keyboard.press_and_release('tab') 
    for i in range(choice(SCORE_LIST)):
        keyboard.press_and_release('down')
        time.sleep(0.1)

# FILL OUT THE LAST QUESTION
keyboard.press_and_release('tab')
time.sleep(0.1)
keyboard.write(MESSAGE)

# 4. Submit the form manually

# 5. Once program is done, write a log for backtracing
with open('log.txt', 'a') as f:
    now = datetime.now()
    date_str = now.strftime("%Y/%m/%d %H:%M:%S")
    f.write('\n')
    json.dump(date_str, f)

print("Program exited.")