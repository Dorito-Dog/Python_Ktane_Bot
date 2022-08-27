from . import solverSpeech

wireColors = ["blue","black","red","white","yellow"]

def solve_wires(bomb, gram):
    wireText = ""
    wireText = solverSpeech.CollectText(wireText, gram)
    wireText = wireText.split(" ")
    print(wireText)

    #Removing all words other than the colors of the wire
    for words in wireText:
        if words not in wireColors:
            wireText.remove(words)

    solverSpeech.SpeakText(wireText)

    match len(wireText):
        case 3:
            if "red" not in wireText:
                solverSpeech.SpeakText("CUT THE SECOND WIRE")
                return
            elif wireText[-1] == "white":
                solverSpeech.SpeakText("CUT THE LAST WIRE")
                return
            elif wireText.count("blue") > 1:
                solverSpeech.SpeakText("CUT THE LAST BLUE WIRE")
                return
            else:
                solverSpeech.SpeakText("CUT THE LAST WIRE")
                return
        case 4:
            if wireText.count("red") > 1 and bomb.final_digit_odd == None:
                bomb.spontaneous_final_digit_check()
    
            if wireText.count("red") > 1 and bomb.final_digit_odd == True:
                solverSpeech.SpeakText("CUT THE LAST WIRE")
                return
            elif wireText[-1] == "yellow" and wireText.count("red") == 0:
                solverSpeech.SpeakText("CUT THE FIRST WIRE")
                return
            elif wireText.count("blue") == 1:
                solverSpeech.SpeakText("CUT THE FIRST WIRE")
                return
            elif wireText.count("yellow") > 1:
                solverSpeech.SpeakText("CUT THE LAST WIRE")
                return
            else:
                solverSpeech.SpeakText("CUT THE SECOND WIRE")
                return
        case 5:
            if wireText[-1] == "black" and bomb.final_digit_odd == None:
                bomb.spontaneous_final_digit_check()

            if wireText[-1] == "black" and bomb.final_digit_odd == True:
                solverSpeech.SpeakText("CUT THE FOURTH WIRE")
                return
            elif wireText.count("red") == 1 and wireText.count("yellow") > 1:
                solverSpeech.SpeakText("CUT THE FIRST WIRE")
                return
            elif wireText.count("black") == 0:
                solverSpeech.SpeakText("CUT THE SECOND WIRE")
                return
            else:
                solverSpeech.SpeakText("CUT THE FIRST WIRE")
                return
        case 6:
            if wireText.count("yellow") == 0 and bomb.final_digit_odd == None:
                bomb.spontaneous_final_digit_check()

            if wireText.count("yellow") == 0 and bomb.final_digit_odd == True:
                solverSpeech.SpeakText("CUT THE THIRD WIRE")
                return
            elif wireText.count("yellow") == 1 and wireText.count("yellow") > 1:
                solverSpeech.SpeakText("CUT THE FOURTH WIRE")
                return
            elif wireText.count("red") == 0:
                solverSpeech.SpeakText("CUT THE LAST WIRE")
                return
            else:
                solverSpeech.SpeakText("CUT THE FOURTH WIRE")
                return
        case _:
            return