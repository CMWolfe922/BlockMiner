# TEST LOG READER
import os

location = 'I:\Crypto\BlockCoin'
filename = 'BlockCoin.log'


def read_logs(location, filename):
    """
    :param location: This is the complete file path
    :param filename: filename that needs to opened and read
    """
    loc = location
    f = filename
    for file in os.listdir(loc):
        if file == f:
            f = open(os.path.join(loc, f), "r")
            print(f.read())


read_logs(location, filename)

# TODO: CREATE A FILE READER FUNCTION FOR LOG FILE
#f = 'I:\Crypto\BlockCoin\BlockCoin.txt'

# with open(f, 'r'):
#     for line in f:
#         print(line)
# TODO: CREATE A FUNCTION FOR GRABBING DATA FROM LOG FILE

# TODO: INSERT PULLED DATA INTO BLOCKCHAIN FOR MINING

# TODO: CREATE A PROTOCOL TO HAVE THIS HAPPEN AFTER EACH GAME
