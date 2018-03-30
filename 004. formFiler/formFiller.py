# formFiller.py - Automatically fills in the form.

import pyautogui, time

# Set these to the correct coordinates for your computer.your
nameFiled =(674, 342)
submitButton = (659, 819)
submitButtonColor = (74, 139, 245)
submitAnotherLink = (761, 258)

formData = [{'name': 'Alice', 'fear': 'eavesdroppers', 'source': 'wand',
  'robocop': 4, 'comments': 'Tell Bob I said hi.'},
  {'name': 'Bob', 'fear': 'bees', 'source': 'amulet', 'robocop': 4,
  'comments': 'n/a'},
  {'name': 'Carol', 'fear': 'puppets', 'source': 'crystal ball', 
  'robocop': 1, 'comments': 'Please take the puppets out of the\
  break room.'},
  {'name': 'Alex Murphy', 'fear': 'ED-209', 'source': 'money',
  'robocop': 5, 'comments': 'Protect the innocent. Serve the public\
  trust. Uphold the law.'},
  ]

pyautogui.PAUSE = 0.5

for person in formData:
    # Give the user a chancee to kill the script.
    print('>>> 5 SECOND PAUSE TO LET USER PRESS CTRL-C <<<')
    time.sleep(1)

    # Wait until the form page has loaded.
    while not pyautogui.pixelMatchesColor(submitButton[0], submitButton[1],
        submitButtonColor):
        time.sleep(0.5)

    print('Enter %s info...' % (person['name']))
    pyautogui.click(nameFiled[0], nameFiled[1]) # 让浏览器获得焦点
    pyautogui.click(nameFiled[0], nameFiled[1]) # 让Name输入栏获得焦点

    # Fill out the Name field.
    pyautogui.typewrite(person['name'] + '\t')

    # Fill out the Freatest Fear(s) field. 
    pyautogui.typewrite(person['fear'] + '\t')

    # Fill out the Source of Wizard Powers field. 
    if person['source'] == 'wand':
        pyautogui.typewrite(['down', 'down', 'enter', '\t'])
    elif person['source'] == 'amulet':
        pyautogui.typewrite(['down', 'down', 'down', 'enter', '\t'])
    elif person['source'] == 'crystal ball':
        pyautogui.typewrite(['down', 'down', 'down', 'down', 'enter', '\t']) 
    elif person['source'] == 'money':
        pyautogui.typewrite(['down', 'down', 'down', 'down', 'down', 'enter', '\t'])

    # Fill out the RoboCop field
    if person['robocop'] == 1:
        pyautogui.typewrite([' ', '\t'])
    elif person['robocop'] == 2:
        pyautogui.typewrite(['right', '\t'])
    elif person['robocop'] == 3:
        pyautogui.typewrite(['right', 'right', '\t'])
    elif person['robocop'] == 4:
        pyautogui.typewrite(['right', 'right', 'right', '\t'])
    elif person['robocop'] == 5:
        pyautogui.typewrite(['right', 'right', 'right', 'right', '\t'])

    # Fill out the Additional Comments field. 
    pyautogui.typewrite(person['comments'] + '\t')

    # Click Submit. 
    pyautogui.press('enter')

    # Wait until form page has loaded. 
    print('Clicked Submit.')
    time.sleep(5)

    # Click the Submit another response link.
    pyautogui.click(submitAnotherLink[0], submitAnotherLink[1])
    