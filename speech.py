import speech_recognition as sr
import random

JSON_PATH = r"hardsoftapplication-52182c5dd661.json"

SENTANCE_SAD = 0
SENTANCE_JOYFUL = 1
SENTANCE_FUNNY = 2
SENTANCE_SERIOUS = 3

def list_microphones():
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

def recognize_voice(r, audio):
    with open(JSON_PATH) as f:
        credentials = f.read()
        text = r.recognize_google_cloud(audio, credentials_json= credentials)
        return text.upper()

def classify_sentence(sentence):
    if "NOVI SAD" in sentence or "NOVISAD" in sentence or "TIMISOARA" in sentence or "SKOPJE" in sentence or "COCHLEA" in sentence or "SCOPELY" in sentence or 'TELEFLORA' in sentence:
        return SENTANCE_SERIOUS
    elif "SERBIA" in sentence or "SERVIA" in sentence or "MACEDONIA" in sentence or "ROMANIA" in sentence:
        return SENTANCE_SAD
    elif "JAVA" in sentence or "C PLUS PLUS" in sentence or "C SHARP" in sentence or "C-SHARP" in sentence:
        return SENTANCE_FUNNY
    elif "WORK ABOUT" in sentence or "MICRO ELECTRONIC" in sentence or "CONTINENTAL" in sentence or "MIKRO" in sentence or "ELEKTRONIKA" in sentence or "WOKE ABOUT":
        return SENTANCE_JOYFUL
    elif "PLUS PLUS" in sentence:
        return SENTANCE_FUNNY
    elif "NOVI" in sentence:
        return SENTANCE_SERIOUS
    elif "SHARP" in sentence:
        return SENTANCE_FUNNY
    elif "NORTH" in sentence or "DERBY" in sentence:
        return SENTANCE_SAD
    elif "MICRO" in sentence or "ELECTRONIC" in sentence:
        return SENTANCE_JOYFUL
    elif "SCOPE" in sentence or "STAPLES" in sentence or "SCRUPLES" in sentence or "SCOPIA" in sentence:
        return SENTANCE_SERIOUS
    elif "WALK" in sentence or "WORK" in sentence or "ABOUT" in sentence or "WOKE" in sentence:
        return SENTANCE_JOYFUL
    elif "ROKU" in sentence or "BOUTS" in sentence or "CABANA" in sentence or "WORLD" in sentence or "WELL" in sentence:
        return SENTANCE_JOYFUL
    elif "SAD" in sentence or "SOARA" in sentence or "SORA" in sentence:
        return SENTANCE_SERIOUS
    else:
        return random.choice([SENTANCE_SAD, SENTANCE_JOYFUL, SENTANCE_FUNNY, SENTANCE_SERIOUS])
    