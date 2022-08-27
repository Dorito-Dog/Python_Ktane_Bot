from . import solverSpeech

morseDict = {
    "dot dash":"a",
    "dash dot dot dot":"b",
    "dash dot dash dot":"c",
    "dash dot dot":"d",
    "dot":"e",
    "dot dot dash dot":"f",
    "dash dash dot":"g",
    "dot dot dot dot":"h",
    "dot dot":"i",
    "dot dash dash dash":"j",
    "dash dot dash":"k",
    "dot dash dot dot":"l",
    "dash dash":"m",
    "dash dot":"n",
    "dash dash dash":"o",
    "dot dash dash dot":"p",
    "dash dash dot dash":"q",
    "dot dash dot":"r",
    "dot dot dot":"s",
    "dash":"t",
    "dot dot dash":"u",
    "dot dot dot dash":"v",
    "dot dash dash":"w",
    "dash dot dot dash":"x",
    "dash dot dash dash":"y",
    "dash dash dot dot":"z"
}

frequencyDict = {
    "shell":505,
    "halls":515,
    "slick":522,
    "trick":532,
    "boxes":535,
    "leaks":542,
    "strobe":545,
    "bistro":552,
    "flick":555,
    "bombs":565,
    "break":572,
    "brick":575,
    "steak":582,
    "sting":592,    
    "vector":595,
    "beats":600
}

def solve_morse(bomb, gram):
    solverSpeech.SpeakText("Letter {}".format(bomb.morse_num))
    morseText = ""
    morseText = solverSpeech.CollectText(morseText, gram)
    morseText = morseText.split("done")
    morseText = morseText[:-1]

    letter = morseDict[morseText[0].strip()]
    solverSpeech.SpeakText(letter)
    options = []

    if morseText == []:
        solverSpeech.SpeakText("Escaping")
        return

    if bomb.morse_num == 1:
        bomb.morse_options = list(frequencyDict.keys())

    for i in bomb.morse_options:
        if i[bomb.morse_num - 1] == letter:
            options.append(i)
    bomb.morse_options = options

    if len(bomb.morse_options) == 1:
        solverSpeech.SpeakText("Your frequency is three point {}".format(frequencyDict[bomb.morse_options[0]]))
        bomb.morse_num = 1
        return
    elif len(bomb.morse_options) < 1:
        solverSpeech.SpeakText("Error, no word found, please try again.")
        bomb.morse_num = 1
        return
    else:
        bomb.morse_num += 1
        solve_morse(bomb, gram)