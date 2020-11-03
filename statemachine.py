import time
from naoqi import ALProxy
import jstyleson

def is_positive(word):
       
    # sorting responses
    positive = ["good", "great", "yes", "okay", "hello", "hi"]     # can be expanded
    negative = ["bad", "sad", "no"]                   
    if word in positive:
        return 0                # return appropriate index for next state
    elif word in negative:
        return 1
    elif word == 'quit':
        return -1            # exit condition

def fsm():
    '''
    conversation fsm
    '''
    IP = "192.168.1.107"
    tts = ALProxy("ALTextToSpeech", IP, 9559)  # initiates text to speech functionality
    asr = ALProxy("ALSpeechRecognition", IP, 9559)  # initiates speech recognition functionality
    memory = ALProxy("ALMemory", IP, 9559)

    asr.setLanguage("English")
    vocab = ["hi", "hello", "yes", "no", "good", "great", "sad", "bad", "okay", "quit"]     # can be expanded as needed
    asr.pause(0)  # pause the ASR engine to be able to call `setVocabulary()`
    asr.setVocabulary(vocab, False)  # sets what pepper understands
    asr.pause(1)  # restart the ASR engine
  
    with open('./script.json') as f:    # load script from the file
        script = jstyleson.load(f)

    state = '1'

    # start the speech recognition engine with user nao
    asr.subscribe("nao")  # pepper start to listens, eyes turns blue

    while True:
        tts.say(script[state]['content'])
        time.sleep(5)           # delay to allow user time to reply
        response = memory.getData("WordRecognized") # retrieve response
        feedback = is_positive(response[-2])    # sort response
        if feedback == -1: #Detect if the user says 'quit'
            break           #Break from loop
        try:
            state = script[state]['next'][feedback]  # switch state of conversation
        except:                                 # unsure of specific error which will be thrown - should be added
            state = script[state]['next'][0]    # for if only one state listed in "next"

    tts.say('Goodbye!')
    asr.unsubscribe("nao") # end listening

if __name__ == "__main__":
    fsm()
