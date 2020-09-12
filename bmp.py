import serial
import time


def getbmp():
    pulse_sum=0
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
            pulse_sum = pulse_sum + i
        # print("sum: " + str(sum))
        # print("count: " + str(len(dataarray)))
        print("avg: " + str(pulse_sum / len(dataarray)))
        avg = sum / len(dataarray)
        #return dataarray
        return avg

    except:
        print("No Arduino connected")



getbmp()
