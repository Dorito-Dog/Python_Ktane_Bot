from . import solverSpeech

def solve_knobs(gram):
    knobText = ""
    knobText = solverSpeech.CollectText(knobText, gram)

    match knobText:
        case ("down down both down up both" | "up down both none both down"):
            solverSpeech.SpeakText("Up")
        case ("down both both down none both" | "up down up none up down"):
            solverSpeech.SpeakText("Down")
        case ("down none none down both down" | "none none none down both none"):
            solverSpeech.SpeakText("Left")
        case ("both down both up both up" | "both down both up down none"):
            solverSpeech.SpeakText("Right")