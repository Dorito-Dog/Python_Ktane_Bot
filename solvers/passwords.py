from . import solverSpeech

passwords = ["about", "after", "again", "below", "could", 
             "every", "first", "found", "great", "house", 
             "large", "learn", "never", "other", "place",
             "plant", "point", "right", "small", "sound",
             "spell", "still", "study", "their", "there",
             "these", "thing", "think", "three", "water",
             "where", "which", "world", "would", "write"]

def solve_password(bomb, gram):
    solverSpeech.SpeakText("Column {}".format(bomb.password_num))
    passText = ""
    passText = solverSpeech.CollectText(passText, gram)
    passText = passText.split(" ")
    passText = passText[:-1]
    solverSpeech.SpeakText(passText)

    letters = []
    for i in passText:
        letters.append(i[0])
    options = []

    #debug print statements
    print(letters)
    print(bomb.password_options)
    print(bomb.password_num)
    
    if bomb.password_num == 1:
        bomb.password_options = passwords

    for i in bomb.password_options:
        if i[bomb.password_num - 1] in letters:
            options.append(i)
    bomb.password_options = options

    if len(bomb.password_options) == 1:
        solverSpeech.SpeakText("Your word is {}".format(bomb.password_options))
        bomb.password_num = 1
        return
    elif len(bomb.password_options) < 1 or bomb.password_num == 5:
        solverSpeech.SpeakText("Error, no word found, please try again.")
        bomb.password_num = 1
        return
    else:
        bomb.password_num += 1
        solve_password(bomb, gram)