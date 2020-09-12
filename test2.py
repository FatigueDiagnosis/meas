import http.client, urllib.parse
import json
import sys
import cv2
import os
import numpy as np
import statistics
import math
import csv
#Import Arudino script
import bmp

#Start camera
#VideoCapture(0) is a built-in camera
cap = cv2.VideoCapture(0)

#Set the content sent to the API server
headers = {

    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': '971fac347c8543ea90fc45ccc2119b7f',
}

params = urllib.parse.urlencode({
    'returnFaceId': 'false',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender,emotion'
})

body_1 = ""
csv_contents = []
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
       sadness = (data[0]['faceAttributes']['emotion']['sadness'] * 100)
       neutral = (data[0]['faceAttributes']['emotion']['neutral'] * 100)
       contempt = (data[0]['faceAttributes']['emotion']['contempt'] * 100)
       disgust = (data[0]['faceAttributes']['emotion']['disgust'] * 100)
       anger = (data[0]['faceAttributes']['emotion']['anger'] * 100)
       surprise = (data[0]['faceAttributes']['emotion']['surprise'] * 100)
       fear = (data[0]['faceAttributes']['emotion']['fear'] * 100)
       happiness = (data[0]['faceAttributes']['emotion']['happiness'] * 100)
       print('悲しみ: ' + str(sadness) + "%")
       body_1 = ('悲しみ: ' + str(sadness)+ "%")
       csv_contents.append(sadness)
       print('中性: ' + str(neutral)+ "%")
       body_1 += ('中性: ' + str(neutral)+ "%")
       csv_contents.append(neutral)
       print('軽蔑: ' + str(contempt)+ "%")
       body_1 +=  ('軽蔑: ' + str(contempt)+ "%")
       csv_contents.append(contempt)
       print('嫌悪: ' + str(disgust)+ "%")
       body_1 += ('嫌悪: ' + str(disgust)+ "%")
       csv_contents.append(disgust)
       print('怒り: ' + str(anger) + "%")
       body_1 += ('怒り: ' + str(anger) + "%")
       csv_contents.append(anger)
       print('驚き: ' + str(surprise) + "%")
       body_1 += ('驚き: ' + str(surprise) + "%")
       csv_contents.append(surprise)
       print('恐れ: ' + str(fear) + "%")
       body_1 += ('恐れ: ' + str(fear) + "%")
       csv_contents.append(fear)
       print('幸福: ' + str(happiness) + "%")
       body_1 += ('幸福: ' + str(happiness) + "%")
       csv_contents.append(happiness)
       break


#Erase the png file(test.png) created on the local PC
os.remove('./test.png')
cap.release()
cv2.destroyAllWindows()

csv_contents.append(bmp.avg)
with open('/Users/maiko/Desktop/sample.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(csv_contents)

sys.exit()
