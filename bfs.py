from node import TreeNode
from inputReader import  InputReader
import copy

#A set of gloabal variables to use in the whole program

#Variables to read the input
maxHeight = []
initialConfiguration = []
goalState = []

#Variables to store visited nodes and the list of nodes to expand
visitedNodes = []
nodesToExpand = []

#To know if the goal state was found
success = []

def searchingByBFS():
    #Pointing to the global variables
    global initialConfiguration
    global goalState
    global visitedNodes
    global nodesToExpand
    global success
    global stacksDoesntMatter
    #At the begin our current state is null
    actualNode = TreeNode(None, None, None, 0)
    
    #Creating the node for the initial configuration
    initialConfiguration = TreeNode(None, initialConfiguration, None, 0)
    
    #Initial state will be the first node to expand
    nodesToExpand.append(initialConfiguration)

    #Adding the first node to expand to the visited list
    visitedNodes.append(initialConfiguration.state)
    
    #Iterate while there are nodes to expand and the goal state has been not reached
    while (nodesToExpand and not(success)):  
        actualNode = nodesToExpand.pop(0)  
        visitedNodes.append(actualNode.state);
        if (isFinalState(actualNode.state)):                           
            success = actualNode
            return True
        #For the actual node, we need to expande it and check all the possible combinations
        for originStack in range(len(actualNode.state)):
            for destinationStack in range(len(actualNode.state)):
                expandedActualNode = copy.deepcopy(actualNode.state)  
                #If origin is not empty, the origin and destination are different and the height in the destination is the correct
                #We can make a movement
                if (expandedActualNode[originStack] and originStack != destinationStack and len(expandedActualNode[destinationStack]) < maxHeight):  
                    #Remove from origin stack
                    expandedActualNode[originStack].pop(0) 
                    #Add to destination stack
                    expandedActualNode[destinationStack].append(actualNode.state[originStack][0])  
                    #If the new state has not been visited
                    if (not (visitedNodes.count(expandedActualNode))):
                        #Calculate cost
                        newCost = 1 + abs(originStack - destinationStack) + actualNode.cost
                        #Create the new node
                        newNode = TreeNode(actualNode, expandedActualNode, [originStack, destinationStack], newCost)
                        #Add it as the list for expansion
                        nodesToExpand.append(newNode)  
                        #Add it to the visited list
                        #visitedNodes.append(newNode.state)  
    return False

#Checks if a state of a node is the goal state        
def isFinalState(nodeState):
        for i, stack in enumerate(nodeState):
            if goalState[i] != ['X']:
                if stack != goalState[i]:
                    return False
        return True
#Transfors the priority queue into an array of strings
def adaptSolution(node):
    path = []
    finalCost = node.cost
    while node.parentNode:
        path.append("(" + str(node.movement[0]) + ", " + str(node.movement[1]) + "); ")
        node = node.parentNode
    return finalCost, path

#Read the input file
reader = InputReader()
data = reader.read()
#print data

#Store the reading results in the global variables
maxHeight = data[0]
initialConfiguration = data[1]
goalState = data[2]

cost = 0
path = []
#Search
if searchingByBFS():
    cost, path = adaptSolution(success)
#Print solution
if len(path) > 0:
    print (len(visitedNodes))
    print(cost)
    print(''.join(item for item in path))
else:
    print("No solution found")
