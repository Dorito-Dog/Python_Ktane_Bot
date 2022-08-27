from . import solverSpeech

def solve_button(bomb, gram):
    buttonText = ""
    buttonText = solverSpeech.CollectText(buttonText, gram)
    solverSpeech.SpeakText(buttonText)
    buttonColor = buttonText.split(" ")[0]
    buttonWord = buttonText.split(" ")[1]

    if buttonWord == "abort" and buttonColor == "blue":
        hold_button()
        return
    
    if buttonWord == "detonate" and bomb.battery_count == None:
        bomb.spontaneous_battery_check()
    if buttonWord == "detonate" and bomb.battery_count > 1:
        press_button()
        return
    
    if buttonColor == "white" and bomb.indicator_car == None:
        bomb.spontaneous_indicator_car_check
    if buttonColor == "white" and bomb.indicator_car == True:
        hold_button()
        return

    if bomb.indicator_frk == None:
        bomb.spontaneous_indicator_freak_check
    if bomb.battery_count == None:
        bomb.spontaneous_battery_check
    if bomb.indicator_frk == True and bomb.battery_count > 2:
        press_button()
        return
    
    if buttonColor == "yellow":
        hold_button()
        return
    
    if buttonWord == "hold" and buttonColor == "red":
        press_button()
        return

    hold_button()
    return
    
    
def press_button():
    solverSpeech.SpeakText("Press the button")

def hold_button():
    stripeColor = ""
    solverSpeech.SpeakText("Hold the button. Stripe color?")
    stripeColor = solverSpeech.CollectText(stripeColor, "./grammars/buttonstripe.gram")
    match stripeColor:
        case "blue":
            solverSpeech.SpeakText("Timer on four")
        case "yellow":
            solverSpeech.SpeakText("Timer on five")
        case _:
            solverSpeech.SpeakText("Timer on one")