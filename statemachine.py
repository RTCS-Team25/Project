import time
from naoqi import ALProxy
import jstyleson

def fsm():
    '''
    conversation fsm
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
  
    with open('./script.json') as f:    # load script from the file
        script = jstyleson.load(f)

    state = '1'

    # start the speech recognition engine with user nao
    asr.subscribe("nao")  # pepper start to listens, eyes turns blue

    asr.unsubscribe("nao") # end listening