# /usr/bin/python3
from collections import namedtuple
from random import sample, choice, randint

Square = namedtuple('Square', 'word color selected')
# pick 25 words from a dictionary
COLORS = ['green', 'gray', 'black']
color_left = [8, 8, 7, 1]
theBoard = list()

def validKeyCode(keycode):
    print('Validate keycode')
    print(keycode)
    print('25 keycodes={}'.format(len(keycode)==25))
    print('9 green ={}'.format(keycode.count('green') == 9))
    print('3 black ={}'.format(keycode.count('black') == 3))
    print('13 grey ={}'.format(keycode.count('gray') == 13))
    return
#--------------------------------------------------------------------------------
def initKeyCodes():
    order = sample(range(25), 25)
    keycode1 = ['gray' for i in range(25)]
    keycode2 = keycode1.copy()
    keycodes=((keycode1, keycode2), (keycode2,keycode1))
    # 3 green in same place
    for i in range(3):
        idx = order.pop()
        keycode1[idx] = 'green'
        keycode2[idx] = 'green'
        idxBlack = order.pop()
    for list1, list2 in keycodes:
        list1[idxBlack] = 'black'
        for color in ['green', 'gray']:
            idx = order.pop()
            list1[idx] = 'black'
            list2[idx] = color
    for list1 in (keycode1, keycode2):
        for i in range(5):
            idx = order.pop()
            list1[idx] = 'green'
    validKeyCode(keycode1)
    validKeyCode(keycode2)
# --------------------------------------------------
def main():
    initKeyCodes()
    return


# -------------------------------------------------
if __name__ == "__main__":
    main()