import time
from naoqi import ALProxy
import jstyleson


def is_positive(word, positive, negative):
    # sorting responses
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
    IP = "pepper.local"  # use the alias for pepper's IP
    tts = ALProxy("ALTextToSpeech", IP, 9559)  # initiates text to speech functionality
    asr = ALProxy("ALSpeechRecognition", IP, 9559)  # initiates speech recognition functionality
    memory = ALProxy("ALMemory", IP, 9559)
    tablet = ALProxy("ALTabletService", IP, 9559)  # initialise tablet functionality

    asr.setLanguage("English")

    positive = ["good", "great", "yes", "okay", "hello", "hi"]  # can be expanded
    negative = ["bad", "sad", "no"]  # can be expanded
    vocab = positive + negative

    asr.pause(0)  # pause the ASR engine to be able to call `setVocabulary()`
    asr.setVocabulary(vocab, False)  # sets what pepper understands
    asr.pause(1)  # restart the ASR engine

    #tablet initialisation 
    url = "url of gif"      # url of the gif, I have uploaded gif to be used to the github repo
    tablet.preLoadImage(url)
    
    with open('./script.json') as f:    # load script from the file
        script = jstyleson.load(f)

    state = '1'

    # start the speech recognition engine with user nao
    asr.subscribe("nao")  # pepper start to listens, eyes turns blue

    while True:
        if state == '6':            # start gif at start of breathing exercise
            tablet.showImage(url)
        elif state == '8':          # stop gif at end of breathing
            tablet.hideImage(url)

        tts.say(script[state]['content'].encode('ascii', 'ignore'))  # convert from unicode to ascii for compatibility
        time.sleep(5)           # delay to allow user time to reply
        
        response = memory.getData("WordRecognized")  # retrieve response
        print('response: ' + str(response) + '\n')
        print('state: ' + state)
        
        feedback = is_positive(response[-2], positive, negative)    # sort response
        
        if feedback == -1 or state == '-1':  # Detect if the user says 'quit'
            break  # Break from loop
        try:
            state = script[state]['next'][feedback]  # switch state of conversation
        except IndexError:
            state = script[state]['next'][0]    # for if only one state listed in "next"

        previousResponse = response         # save the previous entry, could be useful for detecting if user has not responded

    asr.unsubscribe("nao")  # end listening


if __name__ == "__main__":
    fsm()
