import solvers.solverSpeech as solverSpeech
from word2number import w2n

def initialize_bomb(bomb, gram):
    initWords = ""
    initWords = solverSpeech.CollectText(initWords, gram)
    initWords = initWords.split(" ")
    match(initWords[0]):
        case "batteries":
            bomb.battery_count = w2n.word_to_num(initWords[1])
            solverSpeech.SpeakText("{} battery".format(initWords[1]))
        case "digit":
            if initWords[1] == "odd":
                bomb.final_digit_odd = True
                solverSpeech.SpeakText("Odd")
            else:
                bomb.final_digit_odd = False
                solverSpeech.SpeakText("Even")
        case "vowel":
            if initWords[1] == "yes":
                bomb.vowel = True
                solverSpeech.SpeakText("Vowel")
            else:
                bomb.vowel = False
                solverSpeech.SpeakText("No vowel")
        case "car":
            if initWords[1] == "yes":
                bomb.indicator_car = True
                solverSpeech.SpeakText("Car")
            else:
                bomb.indicator_car = False
                solverSpeech.SpeakText("No car")
        case "freak":
            if initWords[1] == "yes":
                bomb.indicator_frk = True
                solverSpeech.SpeakText("Freak")
            else:
                bomb.indicator_frk = False
                solverSpeech.SpeakText("No freak")
        case "parallel":
            if initWords[1] == "yes":
                bomb.parallel_port = True
                solverSpeech.SpeakText("Parallel port")
            else:
                bomb.parallel_port = False
                solverSpeech.SpeakText("No parallel port")
        case "skip":
            return
    if initWords == "skip":
        return
    elif bomb.battery_count == None or bomb.vowel == None or bomb.final_digit_odd == None or bomb.indicator_frk == None or bomb.indicator_car == None or bomb.parallel_port == None:
        initialize_bomb(bomb, gram)
    else:
        return