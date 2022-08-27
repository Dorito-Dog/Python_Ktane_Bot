from word2number import w2n

starss = ["black","black","white","white"]
wiress = ["red", "three", "green", "one", "black", "three", "purple", "four", "white", "two", "orange", "two"]
arrowss = ["purple", "left", "blue", "up", "green", "right", "purple", "right", "purple", "left", "green", "down"]

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

vennResults = vennLetter(starss, wiress, arrowss)


final = []
cutOrder = []

for num, wire in enumerate(wires):
    match wire:
        case ([1, 0, 1, 0, 0] | [1, 0, 1, 0, 0]):
            cutOrder.append(num)
        case ([0, 0, 1, 1, 1] | [1, 0, 0, 1, 0]):
            cutOrder.insert(0, num)
        case ([0, 0, 0, 0, 0] | [0, 1, 0, 1, 0]):
            final.append(num)
        case ([0, 0, 0, 0, 1] | [1, 1, 0, 0, 1]):

        case t:
        case u:
        case m:
        case h:
        case p:
        case b:
        case i:
        case q:
        case j:
        case v:
        case r:
        case d:


x = vennLetter(starss, wiress, arrowss)
print(x)

for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                for e in range(2):
                    print("[{0}, {1}, {2}, {3}, {4}]".format(a,b,c,d,e))