#! /usr/bin/env python2

import time
from naoqi import ALProxy


def repeat_test():
    '''
    test code - pepper repeats word back to user
    '''
    IP = "192.168.1.107"
    tts = ALProxy("ALTextToSpeech", IP, 9559)  # initiates text to speech functionality
    asr = ALProxy("ALSpeechRecognition", IP, 9559)  # initiates speech recognition functionality
    memory = ALProxy("ALMemory", IP, 9559)

    asr.setLanguage("English")
    vocab = ["good", "bad", "quit"]
    asr.pause(0)  # pause the ASR engine to be able to call `setVocabulary()`
    asr.setVocabulary(vocab, False)  # sets what pepper understands
    asr.pause(1)  # restart the ASR engine

    # start the speech recognition engine with user nao
    asr.subscribe("nao")  # pepper start to listens, eyes turns blue

    while True:
        # get data
        # retrieve list of understood phrases from ALMemory
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
        elif heard[0] == 'quit':
            break

    # stop the speech recognition engine with user Test_ASR
    asr.unsubscribe("nao")


if __name__ == "__main__":
    repeat_test()
