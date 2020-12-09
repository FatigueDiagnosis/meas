import http.client, urllib.parse
import json
import sys
import cv2
import os
import numpy as np
import math
import csv
#Import Arudino script
#import bmp

#Start camera
#VideoCapture(0) is a built-in camera
cap = cv2.VideoCapture(0)

#Set the content sent to the API server
headers = {

    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': 'SUBSCRIPTION-KEY',
}

params = urllib.parse.urlencode({
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender,emotion'
})

def start_emotion():
    while True:
        _,img = cap.read()
        #Show window
        cv2.imwrite('test.png',img)

        if cv2.waitKey(1) == 13:
            break
        #Save photos as png files on your local pc
        with open('test.png', 'rb') as f:
            body = f.read()

        #The camera ends when you press Enter
        cv2.imshow('PUSH ENTER KEY', img)

        #Sending using Https
        conn = http.client.HTTPSConnection('test188.cognitiveservices.azure.com')
        conn.request("POST", "/face/v1.0/detect?%s" % params, body, headers)
        response = conn.getresponse()

        #Change the sent data to json format
        data = json.loads(response.read())

        #Shut down the system when only one face is recognized
        if len(data) == 1:
            sexial = (data[0]['faceAttributes']['gender'])
            sadness = (data[0]['faceAttributes']['emotion']['sadness'] * 100)
            neutral = (data[0]['faceAttributes']['emotion']['neutral'] * 100)
            contempt = (data[0]['faceAttributes']['emotion']['contempt'] * 100)
            disgust = (data[0]['faceAttributes']['emotion']['disgust'] * 100)
            anger = (data[0]['faceAttributes']['emotion']['anger'] * 100)
            surprise = (data[0]['faceAttributes']['emotion']['surprise'] * 100)
            fear = (data[0]['faceAttributes']['emotion']['fear'] * 100)
            happiness = (data[0]['faceAttributes']['emotion']['happiness'] * 100)
            break

    #Erase the png file(test.png) created on the local PC
    os.remove('./test.png')
    cap.release()
    cv2.destroyAllWindows()
    return sexial


'''
csv_contents.append(bmp.avg)

with open('/Users/maiko/Desktop/sample.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(csv_contents)
'''
