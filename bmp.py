import serial
import time


def getbmp():
    pulse_sum=0
    dataarray = []
    ser=serial.Serial('/dev/****',9600)
    time.sleep(5)
    start_time = time.time()
    while True:
        ser_bmp=ser.readline()
        ser_bmp=ser_bmp.strip()
        decoded_bmp=ser_bmp.decode("utf-8")
        bmp=int(decoded_bmp)
        dataarray.append(bmp)
        if int(time.time() - start_time) >= 60:
            break
        else:
            print(int(time.time() - start_time))
    for i in dataarray:
        pulse_sum = pulse_sum + i
    avg = pulse_sum / len(dataarray)
    return int(avg)
