import test2 as test
import bmp

def female_check(pulse):
    if pulse <= 52:
        level = 3
    elif 53 <= pulse <= 67:
        level = 2
    elif 68 <= pulse <= 80:
        level = 1
    elif 81 <= pulse <= 89:
        level = 2
    elif 90 <= pulse <= 100:
        level = 3
    else:
        level = 4

    return level

def male_check(pulse):
    if pulse <= 50:
        level = 3
    elif 51 <= pulse <= 66:
        level = 2
    elif 67 <= pulse <= 80:
        level = 1
    elif 81 <= pulse <= 84:
        level = 2
    elif 85 <= pulse <= 100:
        level = 3
    else:
        level = 4
        
    return level

sexial = test.start_emotion()
if sexial == "female":
    print(female_check(bmp.getbmp()))
else:
   print(male_check(bmp.getbmp()))




