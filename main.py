from speech import *
import speech_recognition as sr
import requests
from getch import getch
import os
import sys

module_path = os.sep + ".." + os.sep + ".." + os.sep
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + module_path)
import wolk


if __name__ == "__main__":
    total = 0
    node_ip = input("Enter node IP:")
    r = sr.Recognizer()
    list_microphones()
    device = wolk.Device(key="4upvzcqmjdoatxw9", password="0c19526c-467c-40ca-98c2-e1ada607d872")

    wolk_device = wolk.WolkConnect(device, host="demo.wolkabout.com")

    # Establish a connection to the WolkAbout IoT Platform
    print("Connecting to WolkAbout IoT Platform")
    try:
        wolk_device.connect()
    except RuntimeError as e:
        print(str(e))
        sys.exit(1)

    wolk_device.add_sensor_reading("S1", " ")
    wolk_device.add_sensor_reading("S2", " ")
    wolk_device.add_sensor_reading("S3", " ")
    wolk_device.add_sensor_reading("S4", " ")
    wolk_device.add_sensor_reading("S5", " ")
    wolk_device.publish()

    for i in range(5):
        while True:
            print("PRESS ANYTHING TO RECORD")
            getch()
            print("RECORDING")
            with sr.Microphone(device_index=5) as source:
                audio = r.listen(source, phrase_time_limit = 10)
            sentence = ""
            try:
                sentence = recognize_voice(r, audio)
            except TimeoutError:
                print("TIMEOUT ERROR")
            except sr.UnknownValueError:
                print("SPEECH ERROR")
            #except:
            #    print("UNKNOWN ERROR")
            print("sentence: %s" % sentence)
            result = classify_sentence(sentence)
            if result == SENTANCE_SAD:
                text = "SAD"
                total += 1
            elif result == SENTANCE_JOYFUL:
                text = "JOYFUL"
                total += 1
            elif result == SENTANCE_FUNNY:
                text = "FUNNY"
                total += 3
            elif result == SENTANCE_SERIOUS:
                text = "SERIOUS"
                total += 1
            else:
                print("unknown result, assuming SERIOUS")
                text = "SERIOUS"
                result = SENTANCE_SERIOUS
            print("result: %s" % text)
            print("<s> to send, <r> to repeat")
            ch = getch()
            if ch == 's' or ch == 'S':
                print("SENDING DATA %d" % i)
                print(requests.get("http://%s/%d" % (node_ip, result)))
                wolk_device.add_sensor_reading("S%d" % (i + 1), text)
                wolk_device.publish()
                break
            else:
                print("REPEAT")
        
    print(total % 3)