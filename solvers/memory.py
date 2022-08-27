from . import solverSpeech
from word2number import w2n

def solve_memory(bomb, gram):
    solverSpeech.SpeakText("Round {}".format(bomb.memory_round))
    memoryText = ""
    memoryText = solverSpeech.CollectText(memoryText, gram)
    memoryText = memoryText.split(" ")
    solverSpeech.SpeakText("Display {0}, numbers {1}".format(memoryText[1], ' '.join(memoryText[2:])))
    display = memoryText[1]
    mubers = memoryText[2:]

    #debug print statements
    print("Round: {}".format(bomb.memory_round))
    print("Display number for round: {}".format(display))
    print("Sequence of numbers: {}".format(mubers))
    print("Saved positions: {}".format(bomb.memory_positions))
    print("Saved labels: {}".format(bomb.memory_labels))
    
    match(bomb.memory_round):
        case 1:
            match(display):
                case ("one" | "two"):
                    bomb.memory_positions[0] = 2
                    bomb.memory_labels[0] = mubers[1]
                    solverSpeech.SpeakText("Label {}.".format(mubers[1]))
                    bomb.memory_round = 2
                    return
                case "three":
                    bomb.memory_positions[0] = 3
                    bomb.memory_labels[0] = mubers[2]
                    solverSpeech.SpeakText("Label {}".format(mubers[2]))
                    bomb.memory_round = 2
                    return
                case "four":
                    bomb.memory_positions[0] = 4
                    bomb.memory_labels[0] = mubers[3]
                    solverSpeech.SpeakText("Label {}".format(mubers[3]))
                    bomb.memory_round = 2
                    return
        case 2:
            match(display):
                case "one":
                    bomb.memory_positions[1] = mubers.index("four") + 1
                    bomb.memory_labels[1] = "four"
                    solverSpeech.SpeakText("Label 4")
                    bomb.memory_round = 3
                    return
                case ("two" | "four"):
                    bomb.memory_positions[1] = bomb.memory_positions[0]
                    bomb.memory_labels[1] = mubers[bomb.memory_positions[0] - 1]
                    solverSpeech.SpeakText("Label {}.".format(mubers[bomb.memory_positions[0] - 1]))
                    bomb.memory_round = 3
                    return
                case "three":
                    bomb.memory_positions[1] = 1
                    bomb.memory_labels[1] = mubers[0]
                    solverSpeech.SpeakText("Label {}".format(mubers[0]))
                    bomb.memory_round = 3
                    return
        case 3:
            match(display):
                case "one":
                    bomb.memory_positions[2] = mubers.index(bomb.memory_labels[1]) + 1
                    bomb.memory_labels[2] = bomb.memory_labels[1]
                    solverSpeech.SpeakText("Label {}.".format(w2n.word_to_num(bomb.memory_labels[1])))
                    bomb.memory_round = 4
                    return
                case "two":
                    bomb.memory_positions[2] = mubers.index(bomb.memory_labels[0]) + 1
                    bomb.memory_labels[2] = bomb.memory_labels[0]
                    solverSpeech.SpeakText("Label {}.".format(w2n.word_to_num(bomb.memory_labels[0])))
                    bomb.memory_round = 4
                    return
                case "three":
                    bomb.memory_positions[2] = 3
                    bomb.memory_labels[2] = mubers[2]
                    solverSpeech.SpeakText("Label {}".format(mubers[2]))
                    bomb.memory_round = 4
                    return
                case "four":
                    bomb.memory_positions[2] = mubers.index("four") + 1
                    bomb.memory_labels[2] = "four"
                    solverSpeech.SpeakText("Label 4")
                    bomb.memory_round = 4
                    return
        case 4:
            match(display):
                case "one":
                    bomb.memory_positions[3] = bomb.memory_positions[0]
                    bomb.memory_labels[3] = mubers[bomb.memory_positions[0] - 1]
                    solverSpeech.SpeakText("Label {}.".format(mubers[bomb.memory_positions[0] - 1]))
                    bomb.memory_round = 5
                    return
                case "two":
                    bomb.memory_positions[3] = 1
                    bomb.memory_labels[3] = mubers[0]
                    solverSpeech.SpeakText("Label {}".format(mubers[0]))
                    bomb.memory_round = 5
                    return
                case ("three" | "four"):
                    bomb.memory_positions[3] = bomb.memory_positions[1]
                    bomb.memory_labels[3] = mubers[bomb.memory_positions[1] - 1]
                    solverSpeech.SpeakText("Label {}.".format(mubers[bomb.memory_positions[1] - 1]))
                    bomb.memory_round = 5
                    return
        case 5:
            match(display):
                case "one":
                    solverSpeech.SpeakText("Label {}.".format(bomb.memory_labels[0]))
                    bomb.memory_round = 1
                    return
                case "two":
                    solverSpeech.SpeakText("Label {}.".format(bomb.memory_labels[1]))
                    bomb.memory_round = 1
                    return
                case "three":
                    solverSpeech.SpeakText("Label {}.".format(bomb.memory_labels[3]))
                    bomb.memory_round = 1
                    return
                case "four":
                    solverSpeech.SpeakText("Label {}.".format(bomb.memory_labels[2]))
                    bomb.memory_round = 1
                    return