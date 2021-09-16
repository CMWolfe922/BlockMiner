#!/Crypto/BlockCoin python3.9
# Code for BlockCoin Mining
import PySimpleGUI as sg
import logging
from guiSettings import gameLayout, gameWindow
from guiSettings import data, universalTheme, universalFont
from guiSettings import postGameLayout, postGameWindow
from guiSettings import MAX_ROWS

#================================================#
BlockCoin = 'BlockCoin.txt'
# Logging setup to send one format of logs to a log file and one to stdout:
logging.basicConfig(
    level=logging.DEBUG,
    format='%(name)s, %(asctime)s, [%(levelname)s], %(message)s',
    filename=BlockCoin,
    filemode='a')

ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
ch.setFormatter(logging.Formatter('%(name)s, [%(levelname)s], %(message)s'))
logging.getLogger('').addHandler(ch)
#================================================#

count = 0
selected = set()
total = 0
zero_count = 0


while True:
    event, values = gameWindow.read()
    if event == sg.WIN_CLOSED:
        break
    elif isinstance(event, tuple):
        if event in selected:
            continue
        selected.add(event)
        i, j = event
        v = data[i*MAX_ROWS+j]
        gameWindow[event].update(text=str(v), button_color=('white', 'black'))
        # NEW
        count += 1
        total += v

        if v == 0:
            zero_count += 1
            if zero_count == 15:
                gameWindow.close()

        gameWindow['SUM'].update(value=f"Total {total:>4d}")
        logging.info("Dig Num:"+" | "+str(count)+" | " +
                     str(event)+" | "+str(v)+" | "+str(total))

postGameFrame = sg.Frame("FINISHED DIGGING: ", [[sg.Text(event)], [sg.Text(
    total)]], 'TITLE_LOCATION_TOP_LEFT', "RELIEF_RAISED", size=(200, 200), key="-FRAME-")

event, values = postGameWindow.read()
if event == '-MINE-':
    start_mining()

postGameWindow.close()
