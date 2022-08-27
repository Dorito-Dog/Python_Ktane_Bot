from . import solverSpeech

redOccurrences = [["charlie"],["bravo"],["alpha"],["alpha","charlie"],["bravo"],["alpha","charlie"],["alpha","bravo","charlie"],["alpha","bravo"],["bravo"]]
blueOccurrences = [["bravo"],["alpha","charlie"],["bravo"],["alpha"],["bravo"],["bravo","charlie"],["charlie"],["alpha","charlie"],["alpha"]]
blackOccurrences = [["alpha","bravo","charlie"],["alpha","charlie"],["bravo"],["alpha","charlie"],["bravo"],["bravo","charlie"],["alpha","charlie"],["charlie"],["charlie"]]

def solve_wiresequences(bomb, gram):
    print("Black count = {0}, Blue count = {1}, Red count = {2}".format(bomb.wire_sequences_black_count, bomb.wire_sequences_blue_count, bomb.wire_sequences_red_count))
    (bomb.wire_sequences_moves).clear()
    if(bomb.wire_sequences_black_count + bomb.wire_sequences_blue_count + bomb.wire_sequences_red_count == 9):
        bomb.wire_sequences_black_count = 0
        bomb.wire_sequences_blue_count = 0
        bomb.wire_sequences_red_count = 0
    
    sequenceText = ""
    sequenceText = solverSpeech.CollectText(sequenceText, gram)
    sequenceText = sequenceText.split(" ")
    del sequenceText[-1]
    sequenceText = (' '.join(sequenceText)).split(" next ")

    for pairs in sequenceText:
        match pairs.split(" ")[0]:
            case "black":
                if pairs.split(" ")[1] in blackOccurrences[bomb.wire_sequences_black_count]:
                    solverSpeech.SpeakText("cut")
                else:
                    solverSpeech.SpeakText("don't cut")
                bomb.wire_sequences_moves.append("black")
                bomb.wire_sequences_black_count += 1
            case "blue":
                if pairs.split(" ")[1] in blueOccurrences[bomb.wire_sequences_blue_count]:
                    solverSpeech.SpeakText("cut")
                else:
                    solverSpeech.SpeakText("don't cut")
                bomb.wire_sequences_moves.append("blue")
                bomb.wire_sequences_blue_count += 1
            case "red":
                if pairs.split(" ")[1] in redOccurrences[bomb.wire_sequences_red_count]:
                    solverSpeech.SpeakText("cut")
                else:
                    solverSpeech.SpeakText("don't cut")
                bomb.wire_sequences_moves.append("red")
                bomb.wire_sequences_red_count += 1
            case _:
                return

def undo_last_sequence(bomb):
    bomb.wire_sequences_black_count -= (bomb.wire_sequences_moves).count("black")
    bomb.wire_sequences_blue_count -= (bomb.wire_sequences_moves).count("blue")
    bomb.wire_sequences_red_count -= (bomb.wire_sequences_moves).count("red")   