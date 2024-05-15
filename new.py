"""comment3"""

import os

counter, sum_ = 0, 0
with open('numbers', 'r+') as fp:
    
    while (line := fp.readline().rstrip()) != '0':
        counter += 1
        sum_ += int(line)

    fp.seek(0, os.SEEK_END)
    fp.write(f'{counter}')

    """ my comment"""
    """ my comment2"""