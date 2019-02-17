# /usr/bin/python3
from random import sample
from color import Color

def validKeyCode(keycode):
    print('Validate keycode')
    print(keycode)
    print('25 keycodes={}'.format(len(keycode)==25))
    print('9 green ={}'.format(keycode.count(Color.GREEN) == 9))
    print('3 black ={}'.format(keycode.count(Color.BLACK) == 3))
    print('13 grey ={}'.format(keycode.count(Color.GRAY) == 13))
    return
#--------------------------------------------------------------------------------
def getKeyCodes():
    order = sample(range(25), 25)
    keycode1 = [Color.GRAY for i in range(25)]
    keycode2 = keycode1.copy()
    keycodes=((keycode1, keycode2), (keycode2,keycode1))
    # 3 green in same place
    for i in range(3):
        idx = order.pop()
        keycode1[idx] = Color.GREEN
        keycode2[idx] = Color.GREEN
        idxBlack = order.pop()
    for list1, list2 in keycodes:
        list1[idxBlack] = Color.BLACK
        for color in [Color.GREEN, Color.GRAY]:
            idx = order.pop()
            list1[idx] = Color.BLACK
            list2[idx] = color
    for aList in (keycode1, keycode2):
        for i in range(5):
            idx = order.pop()
            aList[idx] = Color.GREEN
    validKeyCode(keycode1)
    validKeyCode(keycode2)
    return tuple(zip(keycode1, keycode2))
# --------------------------------------------------
def main():
    keycodes = getKeyCodes()
    print(keycodes)
    return


# -------------------------------------------------
if __name__ == "__main__":
    main()
