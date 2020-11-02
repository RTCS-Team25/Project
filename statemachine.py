import time
from naoqi import ALProxy
import jstyleson

def is_positive():
    response = memory.getData("WordRecognized") # retrieve response
    
    # sorting responses
    positive = ["good", "great", "not bad"]     #temporary
    negative = ["bad", "sad"]                   #temporary
    if reponse[-2] in positive:
        return 0                # return appropriate index for next state
    elif response[-2] in negative:
        return 1
    elif respose[-2] == 'quit':
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
    vocab = ["good", "bad", "quit"]         # temporary vocab list - will be adapted foro script
    asr.pause(0)  # pause the ASR engine to be able to call `setVocabulary()`
    asr.setVocabulary(vocab, False)  # sets what pepper understands
    asr.pause(1)  # restart the ASR engine
  
    with open('./script.json') as f:    # load script from the file
        script = jstyleson.load(f)

    state = '1'

    # start the speech recognition engine with user nao
    asr.subscribe("nao")  # pepper start to listens, eyes turns blue

    asr.unsubscribe("nao") # end listening