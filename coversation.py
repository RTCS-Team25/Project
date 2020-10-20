#! /usr/bin/env python2

import time
from naoqi import ALProxy


def repeat_test():
    '''
    test code - pepper repeats word back to user
    '''
    IP = "whatever the IP is"
    tts = ALProxy("ALTextToSpeech", IP, 9559)  # initiates text to speech functionality
    asr = ALProxy("ALSpeechRecognition", IP, 9559)  # initiates speech recognition functionality
    memory = ALProxy("ALMemory")

    asr.setlanguage("English")
    vocab = ["good", "bad"]
    asr.setVocabulary(vocab, False)  # sets what pepper understands

    # start the speech recognition engine with user Test_ASR
    # FIXME: not sure if this 'user' should be the username in the NAOqi system
    asr.subscribe("Test_ASR")  # pepper listens

    # get data
    # FIXME: words understood go in WordRecognized key stored in ALMemory - how to access?
    # retrieve list of understood phrases from ALMemory (maybe???)
    heard = memory.getData("WordRecognized")
    tts.say("You said")
    tts.say(heard[0])  # repeat first word said back to user

    # sorting responses
    positive = ["good", "great", "not bad"]
    negative = ["bad", "sad"]
    if heard[0] in positive:
        tts.say("That's good")
    elif heard[0] in negative:
        tts.say("I'm sorry to hear that")

    # stop the speech recognition engine with user Test_ASR
    asr.unsubscribe("Test_ASR")


if __name__ == "__main__":
    repeat_test()
