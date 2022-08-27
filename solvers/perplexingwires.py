from . import solverSpeech
from word2number import w2n

def solve_perplexingwires(bomb, gram, arrowgram):
    perplexingLeds = ""
    perplexingStars = ""
    perplexingWires = ""
    perplexingArrows = ""

    """ perplexingLeds = "light off on on done"
    perplexingStars = "stars black white white white done"
    perplexingWires = "wires blue two black four blue three green four orange four blue one done"
    perplexingArrows = "arrows green down purple down green right red left green right blue left done"
 """
    solverSpeech.SpeakText("l e d, top to bottom")
    perplexingLeds = solverSpeech.CollectText(perplexingLeds, gram)  
    solverSpeech.SpeakText("stars, black or white")
    perplexingStars = solverSpeech.CollectText(perplexingStars, gram)
    solverSpeech.SpeakText("Wires, color then star position")
    perplexingWires = solverSpeech.CollectText(perplexingWires, gram)
    solverSpeech.SpeakText("arrows, color then direction")
    perplexingArrows = solverSpeech.CollectText(perplexingArrows, arrowgram)
 
    perplexingLeds = perplexingLeds.split(" ")
    perplexingStars = perplexingStars.split(" ")
    perplexingWires = perplexingWires.split(" ")
    perplexingArrows = perplexingArrows.split(" ")

    perplexingLeds = perplexingLeds[1:]
    perplexingStars = perplexingStars[1:]
    perplexingWires = perplexingWires[1:]
    perplexingArrows = perplexingArrows[1:]

    del perplexingLeds[-1]
    del perplexingStars[-1]
    del perplexingWires[-1]
    del perplexingArrows[-1]

    print("Lights: {0}\nStars: {1}\nWires: {2}\nArrows: {3}".format(perplexingLeds,perplexingStars,perplexingWires,perplexingArrows))

    vennResults = vennLetter(perplexingStars, perplexingWires, perplexingArrows)

    final = []
    cutOrder = []
    print(vennResults)
    for num, wire in enumerate(vennResults):
        match wire:
            case ([1, 0, 1, 0, 0] | [1, 0, 1, 0, 1]):
                cutOrder.append(num)
            case ([0, 0, 1, 1, 1] | [1, 0, 0, 1, 0]):
                cutOrder.insert(0, num)
            case ([0, 0, 0, 0, 0] | [0, 1, 0, 1, 0]):
                final.append(num)
            case ([0, 0, 0, 0, 1] | [1, 1, 0, 0, 1]):
                if perplexingLeds.count("on") > perplexingLeds.count("off"):
                    cutOrder.append(num)
            case ([0, 1, 0, 0, 0] | [1, 1, 0, 1, 1]):
                if perplexingLeds[0] == "on":
                    cutOrder.append(num)
            case ([0, 1, 1, 0, 0] | [1, 0, 0, 0, 1]):
                if perplexingArrows[(num*2) + 1] in ["up", "down"]:
                    print(perplexingArrows[(num*2) + 1])
                    cutOrder.append(num)
            case ([0, 0, 0, 1, 0]):
                if perplexingArrows[(num*2) + 1] in ["right", "down"]:
                    cutOrder.append(num)
            case ([1, 0, 1, 1, 0] | [1, 0, 1, 1, 1]):
                if perplexingWires.count(perplexingWires[(num*2) + 1]) > 1:
                    cutOrder.append(num)
            case ([0, 0, 1, 0, 1] | [1, 1, 1, 0, 1]):
                if bomb.port_count == None:
                    bomb.spontaneous_port_count_check()
                if bomb.port_count == (num + 1):
                    cutOrder.append(num)
            case ([0, 1, 1, 1, 1] | [1, 1, 1, 0, 0]):
                if bomb.battery_count == None:
                    bomb.spontaneous_battery_check()
                if bomb.battery_count == (num + 1):
                    cutOrder.append(num)
            case ([0, 0, 1, 0, 0] | [0, 0, 1, 1, 0] | [1, 0, 0, 0, 0]):
                if bomb.indicator_count == None:
                    bomb.spontaneous_indicator_count_check()
                if bomb.indicator_count == (num + 1):
                    cutOrder.append(num)
            case ([1, 1, 0, 0, 0] | [1, 1, 1, 1, 0]):
                if perplexingWires.count(perplexingWires[num*2]) == 1:
                    cutOrder.append(num)
            case ([0, 1, 1, 1, 0] | [1, 1, 0, 1, 0]):
                if num == 0:
                    if perplexingWires[(num*2) + 2] in ["purple", "orange"]:
                        cutOrder.append(num)
                elif num == len(vennResults) - 1:
                    if perplexingWires[(num*2) - 2] in ["purple", "orange"]:
                        cutOrder.append(num)
                elif perplexingWires[(num*2) + 2] in ["purple", "orange"] or perplexingWires[(num*2) - 2] in ["purple", "orange"]:
                    cutOrder.append(num)
            case ([0, 0, 0, 1, 1] | [0, 1, 0, 0, 1]):
                if bomb.usb_port == None:
                    bomb.spontaneous_usb_check()
                if bomb.vowel == None:
                    bomb.spontaneous_vowel_check()
                if bomb.usb_port == True or bomb.vowel == True:
                    cutOrder.append(num)
            case ([0, 1, 0, 1, 1] | [1, 0, 0, 1, 1]):
                if perplexingArrows.count(perplexingArrows[(num*2) + 1]) == 1:
                    cutOrder.append(num)
            case ([0, 1, 1, 0, 1] | [1, 1, 1, 1, 1]):
                pass
    
    if final != []:
        cutOrder.append(final)
    
    cutOrder = [x+1 for x in cutOrder]
    solverSpeech.SpeakText(cutOrder)


def vennLetter(stars, wire, arrow):
    allWires = []
    for color, number in zip(range(0, len(wire), 2), range(1, len(wire), 2)):
        venn = [0]*5
        if wire[color] in ["red", "yellow", "blue", "white"]:
            venn[0] = 1
        if wire[color] == arrow[color]:
            venn[1] = 1
        if stars[w2n.word_to_num(wire[number])-1] == "black":
            venn[2] = 1
        if ((color/2) + 1)%2 == 0:
            venn[3] = 1
        for x, y in zip(range(0, len(wire), 2), range(1, len(wire), 2)):
            if (color < x) and (w2n.word_to_num(wire[number]) > w2n.word_to_num(wire[y])):
                venn[4] = 1
            if (color > x) and (w2n.word_to_num(wire[number]) < w2n.word_to_num(wire[y])):
                venn[4] = 1
        allWires.append(venn)
    return allWires