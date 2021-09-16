from random import sample, shuffle
import PySimpleGUI as sg
import logging

#================================================#
BlockCoin = 'BlockCoin.log'
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


def generate_data(rows, cols):
    v = sorted(sample(list(range(1, 1000)), 9))+[1000]
    data = [v[0]] + [v[i]-v[i-1] for i in range(1, 10)]+[0]*(rows*cols-10)
    shuffle(data)
    return data


#================================================#
# GAME THEME
sg.theme("DarkBlue3")
sg.set_options(font=("Courier New", 12))

MAX_ROWS = MAX_COL = 10
data = generate_data(MAX_ROWS, MAX_COL)

# IN-GAME LAYOUT
layout = [
    [sg.Button(' ', size=(4, 2), key=(i, j)) for j in range(MAX_COL)] for i in range(MAX_ROWS)] + [
    [sg.Text(f"Total {0:>4d}", size=(10, 1), key='SUM')]]
window = sg.Window('Mining GUI', layout)

# TODO: CREATE LAYOUT AND WINDOW FOR POST GAME

# TODO: CREATE MINE BUTTON

#================================================#
count = 0
selected = set()
total = 0
zero_count = 0

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif isinstance(event, tuple):
        if event in selected:
            continue
        selected.add(event)
        i, j = event
        v = data[i*MAX_ROWS+j]
        window[event].update(text=str(v), button_color=('white', 'black'))
        count += 1
        total += v

        if v == 0:
            zero_count += 1

            if zero_count == 15:
                # TODO: MAKE POST GAME WINDOW POPUP

                # TODO: CREATE MINE KEY FUNCTION
                break
        # TODO: CREATE ASYNC FUNC TO LIMIT GAME PLAY

        logging.info("Dig Num:"+" | "+str(count)+" | " +
                     str(event)+" | "+str(v)+" | "+str(total))
        window['SUM'].update(value=f"Total {total:>4d}")


window.close()
