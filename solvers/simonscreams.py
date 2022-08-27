from . import solverSpeech

colorDict = {
    "red": ["ffc","ahf","ded","hce","cah","eda"],
    "orange": ["ceh","dfc","ecf","ada","fhd","hae"],
    "yellow": ["haf","ech","fhe","cfd","dda","aec"],
    "green": ["ecd","cde","haa","dhh","aec","fff"],
    "blue": ["dde","fea","afh","eac","hcf","chd"],
    "purple": ["aha","had","cdc","fef","efe","dch"]
}

orderDict = {
    "a": "ypogrb",
    "c": "oygbpr",
    "d": "grboyp",
    "e": "rbpyog",
    "f": "borpgy",
    "h": "pgyrbo"
}

def solve_simonscreams(bomb, gram):
    colorOrder = ""
    simonScreamsText = ""

    if bomb.simon_screams_round == 1:
        solverSpeech.SpeakText("colors in clockwise order")
        colorOrder = solverSpeech.CollectText(colorOrder, gram)
        solverSpeech.SpeakText("flashes")
        simonScreamsText = solverSpeech.CollectText(simonScreamsText, gram)

        colorOrder = colorOrder.split(" ")
        simonScreamsText = simonScreamsText.split(" ")

        del colorOrder[-1]
        del simonScreamsText[-1]

        bomb.simon_screams_color_order = colorOrder
        bomb.simon_screams_sequence = simonScreamsText
    else:
        solverSpeech.SpeakText("new colors")
        simonScreamsText = solverSpeech.CollectText(simonScreamsText, gram)

        bomb.simon_screams_sequence += simonScreamsText.split(" ")[:-1]

    miniCol = ""

    if sliding_window(bomb.simon_screams_sequence, bomb.simon_screams_color_order, 3) == True:
        miniCol = colorDict[bomb.simon_screams_sequence[bomb.simon_screams_round - 1]][0][bomb.simon_screams_round - 1]
    elif back_and_forth(bomb.simon_screams_sequence, bomb.simon_screams_color_order) == True:
        miniCol = colorDict[bomb.simon_screams_sequence[bomb.simon_screams_round - 1]][1][bomb.simon_screams_round - 1]
    elif bomb.simon_screams_sequence.count("red") + bomb.simon_screams_sequence.count("blue") + bomb.simon_screams_sequence.count("yellow") <= 1:
        miniCol = colorDict[bomb.simon_screams_sequence[bomb.simon_screams_round - 1]][2][bomb.simon_screams_round - 1]
    elif opposite_check(bomb.simon_screams_sequence, bomb.simon_screams_color_order) == True:
        miniCol = colorDict[bomb.simon_screams_sequence[bomb.simon_screams_round - 1]][3][bomb.simon_screams_round - 1]
    elif sliding_window(bomb.simon_screams_sequence, bomb.simon_screams_color_order, 2) == True:
        miniCol = colorDict[bomb.simon_screams_sequence[bomb.simon_screams_round - 1]][4][bomb.simon_screams_round - 1]
    else:
        miniCol = colorDict[bomb.simon_screams_sequence[bomb.simon_screams_round - 1]][5][bomb.simon_screams_round - 1]

    print("Colors: {0}\nFlashes: {1}\nRound: {2}\nLetter chosen: {3}".format(bomb.simon_screams_color_order, bomb.simon_screams_sequence, bomb.simon_screams_round, miniCol))
    
    # CHECKING TIME
    if bomb.indicator_count == None:
        bomb.spontaneous_indicator_count_check()
    if bomb.port_count == None:
        bomb.spontaneous_port_count_check()
    if bomb.digit_serial_count == None:
        bomb.spontaneous_serial_digit_count_check()
    if bomb.battery_count == None:
        bomb.spontaneous_battery_check()
    if bomb.battery_holder_count == None:
        bomb.spontaneous_battery_holder_count_check()

    final = ""
    presses = []

    if bomb.indicator_count >= 3:
        final += orderDict[miniCol][0]
    if bomb.port_count >= 3:
        final += orderDict[miniCol][1]
    if bomb.digit_serial_count > 3:
        final += orderDict[miniCol][2]
    elif bomb.digit_serial_count == 3:
        final += orderDict[miniCol][2]
        final += orderDict[miniCol][3]
    elif bomb.digit_serial_count < 3:
        final += orderDict[miniCol][3]
    if bomb.battery_count >= 3:
        final += orderDict[miniCol][4]
    if bomb.battery_holder_count >= 3:
        final += orderDict[miniCol][5]

    letter_to_word(final, presses)

    solverSpeech.SpeakText(' '.join(presses))
    
    if bomb.simon_screams_round == 3:
        bomb.simon_screams_round = 1
    else:
        bomb.simon_screams_round += 1

def letter_to_word(letters, solution):
    for i in letters:
        match i:
            case "b":
                solution.append("blue")
            case "g":
                solution.append("green")
            case "o":
                solution.append("orange")
            case "p":
                solution.append("purple")
            case "r":
                solution.append("red")
            case "y":
                solution.append("yellow")

def sliding_window(elements, comparator, window_size):
    for i in range(len(elements) - window_size + 1):
        if ''.join(elements[i:i+window_size]) in ''.join(comparator+comparator):
            return True
    else: 
        return False

def back_and_forth(elements, comparator): # checks if a color flashed, then an adjacent color, then the first again
    adjacentFlashes = []
    for i in range(len(elements) - 3):
        if ''.join(elements[i:i+2]) in ''.join(comparator+comparator): # TODO: add a check for counter clockwise adjacency
            adjacentFlashes.append(i)
    for j in adjacentFlashes:
        if elements[j] == elements[j+2]:
            return True
    else: 
        return False

def opposite_check(elements, comparator):
    for i in range(3):
        if comparator[i] not in elements and comparator[i+3] not in elements:
            return True
    else:
        return False