# PySimpleGUI FRAMES AND WINDOW LAYOUTS
from random import sample, shuffle
import PySimpleGUI as sg


def generate_data(rows, cols):
    v = sorted(sample(list(range(1, 1000)), 9))+[1000]
    data = [v[0]] + [v[i]-v[i-1] for i in range(1, 10)]+[0]*(rows*cols-10)
    shuffle(data)
    return data


# GAME THEME
universalTheme = sg.theme("DarkBlue3")
universalFont = sg.set_options(font=("Courier New", 12))

MAX_ROWS = MAX_COL = 10
data = generate_data(MAX_ROWS, MAX_COL)

# IN-GAME LAYOUT
gameLayout = [
    [sg.Button('#', size=(4, 2), key=(i, j)) for j in range(MAX_COL)] for i in range(MAX_ROWS)] + [
    [sg.Text(f"Total {0:>4d}", size=(10, 1), key='SUM')]]
gameWindow = sg.Window('Mining GUI', gameLayout)

# TODO: CREATE LAYOUT AND WINDOW FOR POST GAME

postGameLayout = [
    [sg.Button('Mine Coins', size=(12, 2), key='-MINE-')],
    [sg.Text(f"Total {0:>4d}", size=(10, 1), key='SUM')]
]
postGameWindow = sg.Window('Post Dig: ', postGameLayout)
# TODO: CREATE MINE BUTTON
