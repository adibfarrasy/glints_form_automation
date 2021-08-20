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

import webbrowser

LINK = "https://forms.gle/heRJKBHjAraDr1Qt6"
BROWSER = 'google-chrome'

# 1. Open browser, then open the form link
webbrowser.get(BROWSER).open(LINK)