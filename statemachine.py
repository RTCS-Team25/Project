import time
import os
from naoqi import ALProxy
import jstyleson


def is_positive(word, positive, negative):
    # sorting responses
    if word in positive:
        return 0                # return appropriate index for next state
    elif word in negative:
        return 1
    elif word == 'quit':
        return -1               # exit condition


def fsm():
    '''
    conversation fsm
    '''
    IP = "pepper.local"  # use the alias for pepper's IP
    tts = ALProxy("ALTextToSpeech", IP, 9559)       # initiates text to speech functionality
    asr = ALProxy("ALSpeechRecognition", IP, 9559)  # initiates speech recognition functionality
    memory = ALProxy("ALMemory", IP, 9559)

    asr.setLanguage("English")

    positive = ["good", "great", "yes", "okay", "hello", "hi", "of course", 'happy', 'thank you']  # can be expanded
    negative = ["bad", "sad", "no", 'terrible']                             # can be expanded
    exit_command = ["quit"]                                     # command pepper understands to exit the program
    vocab = positive + negative + exit_command

    asr.pause(0)  # pause the ASR engine to be able to call `setVocabulary()`
    asr.setVocabulary(vocab, False)  # sets what pepper understands
    asr.pause(1)  # restart the ASR engine

    with open('./script.json') as f:    # load script from the file
        script = jstyleson.load(f)

    state = '1'

    # start the speech recognition engine with user nao
    asr.subscribe("nao")  # pepper start to listens, eyes turns blue

    while True:

        tts.say(script[state]['content'].encode('ascii', 'ignore'))  # convert from unicode to ascii for compatibility

        # state specific operations
        if state == '99':           # exit after saying "Goodbye" at final state
            break
        elif state == '6':              # start of meditation
            for n in range(2):          # breathe in and out twice
                tts.say("breathe in")
                for i in [1, 2, 3]:
                    tts.say(str(i))     # count breathing
                    time.sleep(1)     # appropriate delay between counting
                tts.say("and breathe out")
                for i in [1, 2, 3]:
                    tts.say(str(i))     # count breathing
                    time.sleep(0.7)     # appropriate delay between counting
            state = '7'                 # move to next state (only one outcome from meditation)
            continue                    # execute loop for state 7, no response needed from user

        time.sleep(3)               # delay to allow user time to reply

        response = memory.getData("WordRecognized")         # retrieve response
        print('response: ' + str(response) + '\n')
        print('state: ' + state)

        while response[-1] < 0.2 or response == []:         # if pepper is not confident or nothing has been said
            tts.say("Sorry, I didn't quite catch that")     # ask to repeat, dont change state
            time.sleep(3)                                   # wait another 5 seconds for response
            response = memory.getData("WordRecognized")     # retrieve response again
            print('response: ' + str(response) + '\n')
            print('state: ' + state)

        # once pepper is confident in correct response, change state accordingly
        feedback = is_positive(response[-2], positive, negative)    # sort response

        if feedback == -1 or state == '-1':  # Detect if the user says 'quit'
            break  # Break from loop
        try:
            state = script[state]['next'][feedback]  # switch state of conversation
        except IndexError:
            state = script[state]['next'][0]    # for if only one state listed in "next"

    asr.unsubscribe("nao")  # end listening


if __name__ == "__main__":
    fsm()
