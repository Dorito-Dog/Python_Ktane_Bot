from queue import PriorityQueue
from nodrawpyamaze import maze

def h(cell1, cell2):
    x1, y1 = cell1
    x2, y2 = cell2

    return abs(x1-x2) + abs(y1-y2) #manhattan distance formula

def aStar(m, startx, starty, finx, finy):
    start = (startx, starty)
    finish = (finx, finy)
    g_score = {cell:float('inf') for cell in m.grid}
    g_score[start] = 0
    f_score = {cell:float('inf') for cell in m.grid}
    f_score[start] = h(start, finish)

    open = PriorityQueue()
    open.put((h(start, finish),h(start, finish),start))
    aPath={}
    while not open.empty():
        currCell=open.get()[2]
        if currCell==finish:
            break
        for d in 'ESNW':
            if m.maze_map[currCell][d]==True:
                if d=='E':
                    childCell=(currCell[0],currCell[1]+1)
                if d=='W':
                    childCell=(currCell[0],currCell[1]-1)
                if d=='N':
                    childCell=(currCell[0]-1,currCell[1])
                if d=='S':
                    childCell=(currCell[0]+1,currCell[1])

                temp_g_score = g_score[currCell] + 1
                temp_f_score = temp_g_score + h (childCell, finish)

                if temp_f_score < f_score[childCell]:
                    g_score[childCell] = temp_g_score
                    f_score[childCell] = temp_f_score
                    open.put((temp_f_score, h(childCell, finish), childCell))
                    aPath[childCell] = currCell
    fwdPath = {}
    cell = finish
    while cell!=start:
        fwdPath[aPath[cell]]=cell
        cell=aPath[cell]
    return fwdPath