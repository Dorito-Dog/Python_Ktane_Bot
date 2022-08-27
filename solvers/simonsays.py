from . import solverSpeech

flashes = {
    "red": [["blue", "yellow", "green"], ["blue", "red", "yellow"]],
    "blue": [["red", "green", "red"], ["yellow", "blue", "green"]],
    "green": [["yellow", "blue", "yellow"], ["green", "yellow", "blue"]],
    "yellow": [["green", "red", "blue"], ["red", "green", "red"]]
}

def solve_simonsays(bomb, gram):
    simonText = ""
    simonText = solverSpeech.CollectText(simonText, gram)

    presses = []

    simonText = simonText.split(" ")
    del simonText[-1]
    
    print(simonText)
    solverSpeech.SpeakText(' '.join(simonText))

    if bomb.vowel == None:
        bomb.spontaneous_vowel_check()

    for color in simonText:
        if bomb.vowel == True:
            presses.append(flashes[color][0][bomb.strikes])
        else:
            presses.append(flashes[color][1][bomb.strikes])
    
    solverSpeech.SpeakText(' '.join(presses))