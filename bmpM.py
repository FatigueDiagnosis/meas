import serial
import time


def getbmp():
    pulse_sum=0
    pulse_max = 0
    pulse_min = 100
    dataarray = []
    try:
        ser=serial.Serial('/dev/cu.usbmodem14201',9600)
        time.sleep(5)
        while True:
            ser_bmp=ser.readline()
            ser_bmp=ser_bmp.strip()
            decoded_bmp=ser_bmp.decode("utf-8")
            bmp=int(decoded_bmp)
            print(bmp)
            dataarray.append(bmp)

            if len(dataarray) > 9:
                print("time's up")
                break
        print(dataarray)
        for i in dataarray:
            if i < pulse_min:
                pulse_min = i
            if i > pulse_max:
                pulse_max = i
        # print("sum: " + str(sum))
        # print("count: " + str(len(dataarray)))
        print("avg: " + str(pulse_sum / len(dataarray)))
        avg = int(pulse_min + (pulse_max - pulse_min) / 3)
        #return dataarray
        return avg

    except:
        print("No Arduino connected")



getbmp()
