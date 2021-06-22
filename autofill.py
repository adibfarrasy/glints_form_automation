# BUSINESS RULES
# 1. Choose random time between 1600 to 1700 to fill out the form
# 2. Open browser, then open the form link
# 3. Fill out the form by simulating keyboard presses, slightly randomize the answer
# 4. Submit the form manually
# 5. Once program is done, write a log for backtracing

# TESTING
# Create a test form : DONE
# Developer test : DONE
# Use on GA form : DONE


import time
from datetime import date, datetime
import webbrowser
import keyboard
import json
from random import seed, random, choice

# INITIAL CONFIGURATION
with open('./config.json') as infile:
    config = json.load(infile)

ENTRY = config['id'] #name number 9 is Muhammad Adib Farrasy
NUM_OF_SCALE_QNS = config['num_of_scale_qns'] #10 bullet points in GA survey
SCORE_LIST = config['score_list']

# 3. Fill out the form by simulating keyboard presses, slightly randomize the answer
# INITIATE
print('Go to the browser, then press Ctrl+Shift+S to start...')
keyboard.wait('ctrl+shift+s')
time.sleep(0.3)
keyboard.press_and_release('tab')
time.sleep(0.1)
keyboard.press_and_release('enter')
time.sleep(0.3)

# FILL OUT NAME
for i in range(ENTRY):
    keyboard.press_and_release('down')
    time.sleep(0.03)
keyboard.press_and_release('enter')
time.sleep(0.5)

# FILL OUT DATE
today = date.today()
keyboard.press_and_release('tab')
time.sleep(0.03)
keyboard.press_and_release('space')
time.sleep(0.03)
keyboard.press_and_release('tab')
time.sleep(0.03)
keyboard.press_and_release('enter')
time.sleep(0.5)
keyboard.press_and_release('tab')
time.sleep(0.5)
keyboard.press_and_release('tab')

# FILL OUT THE LINEAR SCALE QNS
SCORE_LIST = SCORE_LIST[1:3] # ONLY GIVE GOOD REVIEW.
for i in range(NUM_OF_SCALE_QNS):
    keyboard.press_and_release('tab') 
    for i in range(choice(SCORE_LIST)-1):
        keyboard.press_and_release('left')
        time.sleep(0.1)

# FILL OUT THE BULLET POINT QN
keyboard.press_and_release('tab, space')
for i in range(12):
    keyboard.press_and_release('tab')
    time.sleep(0.1)

# FILL OUT THE LAST QUESTION
time.sleep(0.5)
keyboard.write("good work")

# 4. Submit the form manually

# 5. Once program is done, write a log for backtracing
with open('log.txt', 'a') as f:
    now = datetime.now()
    date_str = now.strftime("%Y/%m/%d %H:%M:%S")
    f.write('\n')
    json.dump(date_str, f)

print("Program exited.")