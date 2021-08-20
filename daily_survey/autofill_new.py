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
from datetime import datetime
import keyboard
import json
from random import randint


ENTRY = 30 #name number 30 is Muhammad Adib Farrasy
MESSAGE = 'keep up the good work'

def write_nonsense(input):
    keyboard.press_and_release('tab')
    time.sleep(0.03)
    keyboard.write(input)
    time.sleep(0.03)

def linear_scale_fill():
    keyboard.press_and_release('tab') 
    for i in range(randint(2,4)):
        keyboard.press_and_release('right')
        time.sleep(0.1)

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

# CHOOSE FINAL PROJECT TEAM
keyboard.press_and_release('tab')
time.sleep(0.03)
keyboard.press_and_release('space')
time.sleep(0.03)

# CHOOSE STACK CLASS
keyboard.press_and_release('tab')
time.sleep(0.03)
keyboard.press_and_release('down')
time.sleep(0.03)

# WRITE NONSENSE PT. 1
write_nonsense('to live a better life')

# WRITE NONSENSE PT. 2
write_nonsense('nothing. all good')

# WRITE NONSENSE PT. 3
write_nonsense('nothing. all good')

# FILL OUT THE LINEAR SCALE QN PT 2
linear_scale_fill()

# WRITE NONSENSE PT. 4
write_nonsense('approx. 3 hours')

# FILL OUT THE LINEAR SCALE QN PT 2
linear_scale_fill()

# FILL OUT THE LINEAR SCALE QN PT 3
linear_scale_fill()

# FILL OUT THE LINEAR SCALE QN PT 4
linear_scale_fill()

# FILL OUT THE LINEAR SCALE QN PT 5
linear_scale_fill()

# WRITE NONSENSE PT. 4
write_nonsense('keep doing good work')

# 4. Submit the form manually

# 5. Once program is done, write a log for backtracing
with open('log.txt', 'a') as f:
    now = datetime.now()
    date_str = now.strftime("%Y/%m/%d %H:%M:%S")
    f.write('\n')
    json.dump(date_str, f)


print("Program exited.")