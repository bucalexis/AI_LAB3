from node import TreeNode
from inputReader import  InputReader
import copy

def searchingRecursive(initialState, visitedNodes):
    node = initialState
    nodeInitialState = node.state
    stateLength = len(nodeInitialState)
    cost = node.cost
    if(nodeInitialState == goalState):
        return node
    else:
        for i in range(0, stateLength):
            for j in range(0, stateLength):
                if (i != j and (len(nodeInitialState[j])) > 0 and (len(nodeInitialState[i])) < maxHeight):
                    nstate = copy.deepcopy(nodeInitialState)
                   
                    #Put the last container j -> i 
                    nstate[i].append(nstate[j].pop())
                    if (not(visitedNodes.count(nstate))):
                        movements = [i, j]
                        
                        #New cost
                        #1 Picking up the container and Putting the container down + 1 for Moving the container one stack to the left or right + the accumulated cost of the path
                        newCost = 1 + abs(i - j) + cost
                        
                        #New node
                        newNode = TreeNode(node, nstate, movements, newCost)
                        
                        #Visited list
                        visitedNodes.append(nstate)

                        #Recursive call
                        auxDFS = searchingRecursive(newNode, visitedNodes)
                        if(auxDFS != None):
                            return auxDFS
    return None

def searchingByDFS():
    visitedNodes = []
    auxDFS = searchingRecursive(initialState, visitedNodes)
    if(auxDFS == None):
        return None
    else:
        return auxDFS

#Print the path
def path(node, count):
    actual = node
    steps = []
    if(node != None):
        print("Cost:",node.cost)
    while(actual != None):
        if(actual.parentNode != None):
            steps.append(actual.movement)
        actual = actual.parentNode
    while(len(steps) > 0):
        count += 1
        print(steps.pop()),
    return count    

#Read the input file
reader = InputReader()
data = reader.readDFS()
#print data

#Store the reading results in the global variables

#Creating the node for the initial configuration
initialConfiguration = TreeNode(None, data[1], None, 0)

#Pointing to the global variables
goalState = data[2]
maxHeight = data[0]
initialState = initialConfiguration

#Search
auxDFS = searchingByDFS()
if (auxDFS != None):
    count = 0;
    print("Total nodes:",path(auxDFS,count)) #Print solution
else:
    print ("No solution found")
