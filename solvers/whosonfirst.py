from . import solverSpeech

dict = {
        "ready": ["yes", "okay", "what statement", "middle", "left", "press", "right", "blank", "ready"],
        "first": ["left", "okay", "yes", "middle", "no", "right", "nothing", "you three h", "wait", "ready", "blank", "what statement", "press", "first"],
        "no": ["blank", "you three h", "wait", "first", "what statement", "ready", "right", "yes", "nothing", "left", "press", "okay", "no"],
        "blank": ["wait", "right", "okay", "middle", "blank"],
        "nothing": ["you three h", "right", "okay", "middle", "yes", "blank", "no", "press", "left", "what statement", "wait", "first", "nothing"],
        "yes": ["okay", "right", "you three h", "middle", "first", "what statement", "press", "ready", "nothing", "yes"],
        "what statement": ["you three h", "what statement"],
        "you three h": ["ready", "nothing", "left", "what statement", "okay", "yes", "right", "no", "press", "blank", "you three h"],
        "left": ["right", "left"],
        "right": ["yes", "nothing", "ready", "press", "no", "wait", "what statement", "right"],
        "middle": ["blank", "ready", "okay", "what statement", "nothing", "press", "no", "wait", "left", "middle"],
        "okay": ["middle", "no", "first", "yes", "you three h", "nothing", "wait", "okay"],
        "wait": ["you three h", "no", "blank", "okay", "yes", "left", "first", "press", "what statement", "wait"],
        "press": ["right", "middle", "yes", "ready", "press"],
        "you": ["sure", "you are", "your possessive", "you're contraction", "next", "uh huh positive", "you are letters", "hold", "what question", "you"],
        "you are": ["your possessive", "next", "like", "uh huh positive", "what question", "done", "uh uh negative", "hold", "you", "letter you", "you're contraction", "sure", "you are letters", "you are"],
        "your possessive": ["uh uh negative", "you are", "uh huh positive", "your possessive"],
        "you're contraction": ["you", "you're contraction"],
        "you are letters": ["done", "letter you", "you are letters"],
        "letter you": ["uh huh positive", "sure", "next", "what question", "you're contraction", "you are letters", "uh uh negative", "done", "letter you"],
        "uh huh positive": ["uh huh positive"],
        "uh uh negative": ["you are letters", "letter you", "you are", "you", "done", "hold", "uh uh negative"],
        "what question": ["you", "hold", "you're contraction", "your possessive", "letter you", "done", "uh uh negative", "like", "you are", "uh huh positive", "you are letters", "next", "what question"],
        "done": ["sure", "uh huh positive", "next", "what question", "your possessive", "you are letters", "you're contraction", "hold", "like", "you", "letter you", "you are", "uh uh negative", "done"],
        "next": ["what question", "uh huh positive", "uh uh negative", "your possessive", "hold", "sure", "next"],
        "hold": ["you are", "letter you", "done", "uh uh negative", "you", "you are letters", "sure", "what question", "you're contraction", "next", "hold"],
        "sure": ["you are", "done", "like", "you're contraction", "you", "hold", "uh huh positive", "you are letters", "sure"],
        "like": ["you're contraction", "next", "letter you", "you are letters", "hold", "uh uh negative", "what question", "uh huh positive", "you", "like"]
    }

def solve_whosonfirst(gram):
    
    whosText = ""
    whosText = solverSpeech.CollectText(whosText, gram)
    whosText = whosText.split(" ")
    del whosText[0]
    del whosText[-1]
    whosText = (' '.join(whosText)).split(" then ")
    print(whosText)
    solverSpeech.SpeakText(whosText)
    displayWord = whosText[0]
    print(displayWord)
    buttonWords = whosText[1:]
    print(buttonWords[5])

    match displayWord:
        case ("you are letters"):
            search(dict, buttonWords[0], buttonWords)

        case ("yes" | "nothing" | "l e d" | "they are"):
            search(dict, buttonWords[1], buttonWords)
        
        case ("empty" | "they're contraction" | "reed" | "leed"):
            search(dict, buttonWords[2], buttonWords)

        case ("first" | "okay" | "letter see"):
            search(dict, buttonWords[3], buttonWords)

        case ("blank" | "read a book" | "red" | "you" | "your possessive" | "you're contraction" | "their possessive"):
            search(dict, buttonWords[4], buttonWords)
        
        case ("display" | "says" | "no" | "lead a country" | "hold on" | "you are" | "there" | "see" | "see word"):
            search(dict, buttonWords[5], buttonWords)
        case _:
            solverSpeech.SpeakText("Could not find display word")
            return

def search(mydict, keyword, keylist):
    for i in mydict[keyword]:
        if i in keylist:
            solverSpeech.SpeakText("Your word is {}".format(i))
            return
    else:
        solverSpeech.SpeakText("Could not find keyword")
        return