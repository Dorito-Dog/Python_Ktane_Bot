from nodrawpyamaze import maze
from aStar import aStar
from . import solverSpeech
from word2number import w2n

maze1 = [[2,1],[3,6], './solvers/mazes/maze1.csv']
maze2 = [[2,5],[4,2], './solvers/mazes/maze2.csv']
maze3 = [[4,4],[4,6], './solvers/mazes/maze3.csv']
maze4 = [[1,1],[1,4], './solvers/mazes/maze4.csv']
maze5 = [[3,5],[6,4], './solvers/mazes/maze5.csv']
maze6 = [[1,5],[5,3], './solvers/mazes/maze6.csv']
maze7 = [[1,2],[6,2], './solvers/mazes/maze7.csv']
maze8 = [[1,4],[4,3], './solvers/mazes/maze8.csv']
maze9 = [[2,3],[5,1], './solvers/mazes/maze9.csv']

mazes = [maze1,maze2,maze3,
         maze4,maze5,maze6,
         maze7,maze8,maze9]

numbers = ["one", "two", "three", "four", "five", "six"]

def solve_mazes(gram):
    m = maze()
    solution = ""
    mazesText = ""
    solverSpeech.SpeakText("Circle 1")
    mazesText = solverSpeech.CollectText(mazesText, gram)
    solverSpeech.SpeakText("Circle 2")
    mazesText += ' ' + solverSpeech.CollectText(mazesText, gram)
    solverSpeech.SpeakText("Red triangle")
    mazesText += ' ' + solverSpeech.CollectText(mazesText, gram)
    solverSpeech.SpeakText("White light")
    mazesText += ' ' + solverSpeech.CollectText(mazesText, gram) 
    #mazesText = ("row two column five done row four column two done row one column one done row six column six done")
    mazesText = mazesText.split(" ")
    mazesNumbers = []

    for i in mazesText:
        if i in numbers:
            mazesNumbers.append(w2n.word_to_num(i))

    print(mazesNumbers)
    mazeSelection = identifyMaze(mazesNumbers[0], mazesNumbers[1], mazesNumbers[2], mazesNumbers[3])

    m.CreateMaze(loadMaze=mazeSelection[2])
    path = aStar(m,mazesNumbers[4], mazesNumbers[5],mazesNumbers[6], mazesNumbers[7])

    for i, j in path.items():
        if i[0] > j[0]:
            solution += "Down, "
        elif i[0] < j[0]:
            solution += "Up, "
        elif i[1] > j[1]:
            solution += "Right, "
        elif i[1] < j[1]:
            solution += "Left, "

    solverSpeech.SpeakText(solution)

def identifyMaze(ypos1, xpos1, ypos2, xpos2):
    for i in mazes:
        if [ypos1, xpos1] in i and [ypos2, xpos2] in i:
            return i
    else:
        solverSpeech.SpeakText("Unable to find maze, please try again")