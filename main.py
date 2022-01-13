import pyautogui
import pytesseract as tess
import array
import keyboard
import win32api, win32con
from pyautogui import *
from PIL import Image, ImageGrab
from time import sleep

#the location of your tesseract.exe file
tess.pytesseract.tesseract_cmd = r'Tesseract-OCR\tesseract.exe'

pyautogui.PAUSE = 0.1
pyautogui.FAILSAFE = True

print(pyautogui.size())
print(pyautogui.position())

sleep(0.1)
pyautogui.hotkey('alt', 'tab')

sleep(0.3)
while True:
    image = ImageGrab.grab(bbox=(1142, 917, 1263, 975))
    image.save('decimal.png')
    dec_image = Image.open('decimal.png')
    dec_num_str = tess.image_to_string(dec_image)

    one = (6, 53, 74)
    zero = (23, 75, 106)
    zero2 = (0, 80, 115)

    l_image1 = ImageGrab.grab(bbox=(387, 915, 457, 976))
    l_image1.save('binary1.png')
    l_image2 = ImageGrab.grab(bbox=(478, 918, 546, 976))
    l_image2.save('binary2.png')
    l_image3 = ImageGrab.grab(bbox=(566, 915, 636, 976))
    l_image3.save('binary3.png')
    l_image4 = ImageGrab.grab(bbox=(656, 915, 727, 976))
    l_image4.save('binary4.png')
    l_image5 = ImageGrab.grab(bbox=(745, 915, 816, 976))
    l_image5.save('binary5.png')
    l_image6 = ImageGrab.grab(bbox=(836, 915, 906, 976))
    l_image6.save('binary6.png')
    l_image7 = ImageGrab.grab(bbox=(925, 915, 1006, 976))
    l_image7.save('binary7.png')
    l_image8 = ImageGrab.grab(bbox=(1016, 915, 1085, 976))
    l_image8.save('binary8.png')

    digits = array.array('i', [0, 0, 0, 0, 0, 0, 0, 0])
    values = array.array('i', [128, 64, 32, 16, 8, 4, 2, 1])
    # ----------------------------------------------------------
    if l_image1.getpixel((36, 30)) == one:
        digits[0] = 1
    else:
        digits[0] = 0
    # ----------------------------------------------------------
    if l_image2.getpixel((35, 27)) == one:
        digits[1] = 1
    else:
        digits[1] = 0
    # ----------------------------------------------------------
    if l_image3.getpixel((36, 31)) == one:
        digits[2] = 1
    else:
        digits[2] = 0
    # ----------------------------------------------------------
    if l_image4.getpixel((36, 31)) == one:
        digits[3] = 1
    else:
        digits[3] = 0
    # ----------------------------------------------------------
    if l_image5.getpixel((36, 31)) == one:
        digits[4] = 1
    else:
        digits[4] = 0
    # ----------------------------------------------------------
    if l_image6.getpixel((36, 31)) == one:
        digits[5] = 1
    else:
        digits[5] = 0
    # ----------------------------------------------------------
    if l_image7.getpixel((36, 31)) == one:
        digits[6] = 1
    else:
        digits[6] = 0
    # ----------------------------------------------------------
    if l_image8.getpixel((33, 33)) == one:
        digits[7] = 1
    else:
        digits[7] = 0

    coordinates = (422, 940)
    count = 0

    # 0 case
    if image.getpixel((93, 28)) == (255, 255, 255) and image.getpixel((92, 28)) == (163, 255, 255) and image.getpixel((91, 28)) == (0, 80, 153):
        for i in range(0, 8):
            if digits[i] != 0:
                pyautogui.moveTo(coordinates)
                pyautogui.click()
            coordinates = (coordinates[0] + 90, 940)
    # 1 case
    elif image.getpixel((90, 22)) == (255, 255, 227) and image.getpixel((91, 22)) == (118, 103, 115) and image.getpixel((92, 22)) == (0, 80, 115) and image.getpixel((76, 15)) == (255, 255, 255):
        for i in range(0, 8):
            if digits[i] != 0:
                pyautogui.moveTo(coordinates)
                pyautogui.click()
            if i == 7 and digits[i] != 1:
                pyautogui.moveTo(coordinates)
                pyautogui.click()

            coordinates = (coordinates[0] + 90, 940)
            print(i, coordinates)
    # 2 case
    elif image.getpixel((88, 22)) == (255, 234, 197) and image.getpixel((89, 22)) == (77, 101, 127) and image.getpixel((90, 22)) == (22, 94, 125) and image.getpixel((91, 22)) == (10, 83, 126) and image.getpixel((92, 22)) == (102, 210, 255) and image.getpixel((81, 27)) == (255, 255, 255):
        for i in range(0, 8):
            if digits[i] != 0:
                pyautogui.moveTo(coordinates)
                pyautogui.click()
            if i == 6 and digits[i] != 1:
                pyautogui.moveTo(coordinates)
                pyautogui.click()

            coordinates = (coordinates[0] + 90, 940)
            print(i, coordinates)
    # 5 case
    elif image.getpixel((91, 15)) == (255, 201, 161) and image.getpixel((91, 16)) == (213, 162, 135) and image.getpixel((91, 17)) == (157, 126, 115) and image.getpixel((91, 28)) == (18, 87, 117) and image.getpixel((76, 15)) == (255, 255, 255):
        for i in range(0, 8):
            if digits[i] != 0:
                pyautogui.moveTo(coordinates)
                pyautogui.click()

            if i == 5 and digits[i] != 1 or i == 7 and digits[i] != 1:
                pyautogui.moveTo(coordinates)
                pyautogui.click()

            coordinates = (coordinates[0] + 90, 940)
            print(i, coordinates)

    # 3 case
    elif image.getpixel((88, 22)) == (255, 255, 235) and image.getpixel((89, 22)) == (175, 158, 163) and image.getpixel((90, 22)) == (82, 120, 136) and image.getpixel((91, 22)) == (22, 90, 119) and image.getpixel((92, 22)) == (70, 186, 252) and image.getpixel((81, 27)) == (255, 255, 255):
        for i in range(0, 8):
            if digits[i] != 0:
                pyautogui.moveTo(coordinates)
                pyautogui.click()
            if i == 6 and digits[i] != 1 or i == 7 and digits[i] != 1:
                pyautogui.moveTo(coordinates)
                pyautogui.click()

            coordinates = (coordinates[0] + 90, 940)
            print(i, coordinates)


    coordinates = (422, 940)
    if dec_num_str != '':
        dec_num = int(dec_num_str)
        for i in range(0, 8):
            if (dec_num > values[i]) and (digits[i] == 0):
                pyautogui.moveTo(coordinates)
                pyautogui.click()
                dec_num = dec_num - values[i]
            # elif (dec_num < values[i]) and (digits[i] == 0):
            #     continue
            elif dec_num > values[i] and digits[i] == 1:
                dec_num = dec_num - values[i]
            elif dec_num < values[i] and digits[i] == 1:
                pyautogui.moveTo(coordinates)
                pyautogui.click()
            elif dec_num == values[i] and digits[i] == 0:
                pyautogui.moveTo(coordinates)
                pyautogui.click()
                dec_num = dec_num - values[i]
            elif dec_num == values[i] and digits[i] == 1:
                dec_num = dec_num - values[i]
                print('exe')

            coordinates = (coordinates[0] + 90, 940)
            print(dec_num)
            count += 1
            if dec_num <= 0:
                break


        for i in range(count, 8):
            print(i, digits)

            if digits[i] != 0:
                pyautogui.moveTo(coordinates)
                pyautogui.click()

            coordinates = (coordinates[0] + 90, 940)
    else:
        dig_res = 0;
        for i in range(0, 8):
            if digits[i] == 1:
                dig_res += values[i]

        pyautogui.moveTo(1211, 941);
        pyautogui.click()
        pyautogui.typewrite(str(dig_res), interval=0.1)
        pyautogui.press('enter')


    sleep(1.7)

pyautogui.hotkey('alt', 'tab')
