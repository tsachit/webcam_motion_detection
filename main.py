import cv2
import random
from datetime import datetime, timedelta
import simpleaudio as sa

# in seconds
alert_diff_limit=15
# to start from first
last_alert_time=datetime.now() - timedelta(seconds=alert_diff_limit)
baseline_image=None
change_in_frame=0
change_detected=False
video=cv2.VideoCapture(0)

def alert(type=None, rate=None):
    print('Intruder Alert')
    try:
        if(type == None):
            type = 'com.apple.speech.synthesis.voice.Alex'
        if(rate == None):
            rate = 200
        # Just for variation
        sound_file = 'sounds/Intruder Alert.wav'
        if(random.choice([True, False])):
            sound_file = 'sounds/Red Alert.wav'

        wave_object = sa.WaveObject.from_wave_file(sound_file)
        print('playing alarm sound using simpleaudio')

        # define an object to control the play
        play_object = wave_object.play()
        play_object.wait_done()

    except Exception as error:
        print( "<p>Error: %s</p>" % error )

while True:
    check, frame = video.read()
    gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray_frame=cv2.GaussianBlur(gray_frame,(25,25),0)

    if baseline_image is None:
        baseline_image=gray_frame
        continue

    delta=cv2.absdiff(baseline_image,gray_frame)
    threshold=cv2.threshold(delta, 30, 255, cv2.THRESH_BINARY)[1]
    (contours,_)=cv2.findContours(threshold,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) < 8000:
            change_in_frame -= 1
            continue

        print('Change Detected')
        change_in_frame=1
        (x, y, w, h)=cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 1)

    difference = (datetime.now() - last_alert_time).total_seconds()
    if change_in_frame > 0 and difference > alert_diff_limit:
        alert()
        change_in_frame=0
        last_alert_time=datetime.now()

    cv2.imshow("gray_frame Frame",gray_frame)
    cv2.imshow("Delta Frame",delta)
    cv2.imshow("Threshold Frame",threshold)
    cv2.imshow("Color Frame",frame)

    if cv2.waitKey(1)==ord('q'):
        break

#Clean up, Free memory
video.release()
cv2.destroyAllWindows