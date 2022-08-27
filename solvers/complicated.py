from . import solverSpeech

def solve_complicated(bomb, gram):
    #solverSpeech.SpeakText("Begin wires")

    complicatedText = ""
    complicatedText = solverSpeech.CollectText(complicatedText, gram)

    #Split wires by "next" keyword and remove "done" finisher
    complicatedText = complicatedText.split(" ")
    del complicatedText[-1]
    complicatedText = (' '.join(complicatedText)).split(" next ")

    print(complicatedText)
    solverSpeech.SpeakText(complicatedText)

    #Take each element and sort all words alphabetically within the element
    for y in range (0, len(complicatedText) - 1):
        alph = complicatedText[y].split(" ")
        alph.sort()
        complicatedText[y] = ' '.join(alph)
    
    print(complicatedText)

    directions = [0] * (len(complicatedText))
    
    for i in range(0, len(complicatedText)):   
        directions[i] = cuts(complicatedText[i], bomb)

    print(directions)
    solverSpeech.SpeakText(directions)
    return

def cuts(wire, bomb):
    match wire:
        case ("nothing" | "star" | "red star"):
            return "cut"

        case("light" | "blue light star red" | "blue star"):
            return "no cut"

        case("red" | "blue" | "blue red" | "blue light red"):
            if bomb.final_digit_odd == None:
                bomb.spontaneous_final_digit_check()
            if bomb.final_digit_odd == False:
                return "cut"
            else:
                return "no cut"
                    
        case("blue light" | "blue red star" | "blue light star"):
            if bomb.parallel_port == None:
                bomb.spontaneous_parallel_port_check()
            if bomb.parallel_port == True:
                return "cut"
            else:
                return "no cut"
                
        case("light red" | "light star" | "light red star"):
            if bomb.battery_count == None:
                bomb.spontaneous_battery_check()
            if bomb.battery_count >= 2:
                return "cut"  
            else:
                return "no cut"

        case _:
            return