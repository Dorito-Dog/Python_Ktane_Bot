from types import NoneType
from . import solverSpeech

symbols = [["q", "a t", "lambda", "z", "spider", "letter h", "c dot"],
           ["e dots", "q", "c dot", "curl", "white star", "letter h", "question mark"],
           ["copyright", "but", "curl", "j", "half three", "lambda", "white star"],
           ["russian b", "paragraph", "b t", "spider", "j", "question mark", "smiley"],
           ["sigh", "smiley", "b t", "c dot", "paragraph", "alien snake", "black star"],
           ["russian b", "e dots", "puzzle piece", "a e", "sigh", "nose ring", "omega"]]

def solve_keypads(gram):
    keypadsText = ""
    keypadsText = solverSpeech.CollectText(keypadsText, gram)
    keypadsText = keypadsText.split(" next ")

    keypadsText[-1] = keypadsText[-1][:-5]
    print(keypadsText)
    solverSpeech.SpeakText(keypadsText)
    column = determine_column(symbols, keypadsText)
    solution = ""

    if not isinstance(column, NoneType):
        for j in column:
            if j in keypadsText:
                solution += ' ' + j
    
    solverSpeech.SpeakText(solution)

def determine_column(symList, bombSym):
    for i in symList:
        if all(elem in i for elem in bombSym):
            return i
    else:
        solverSpeech.SpeakText("Unable to find a match, please try again.")