import fileinput
import operator
import copy
import sys
from node import TreeNode 
from inputReader import InputReader 

#Variables to read the input
maxHeight = []
initialConfiguration = []
goalState = []

#Variables to store visited nodes and the list of nodes to expand
visitedNodes = []
nodesToExpand = []

#Heuristic: the number of blocks that are incorrectly placed in each stack
def heuristicCost(state):
	
    cost = 0
    for i, stack in enumerate(state):
        for j, block in enumerate(stack):
            try:
                if block != goalState[i][j]:
				    cost += 1
            except IndexError:
                cost += 1
	return cost

#Calculates the cost of moving the block from one stack to another
def movementCost(fromStack, toStack):
    return 1 + abs(fromStack - toStack)

#Moves the block on the top from one stack to another
def moveBlock(state, fromStack, toStack):
    originalState = copy.deepcopy(state)
    block = state[fromStack][-1]
    del state[fromStack][-1]
    state[toStack].append(block)
    cost = movementCost(fromStack, toStack) + heuristicCost(state)
    return state, cost

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
        path.insert(0, "(" + str(node.movement[0]) + ", " + str(node.movement[1]) + "); ")
        finalCost -= heuristicCost(node.state)
        node = node.parentNode
    return finalCost, path

#Searching 
def aStar():
    path = []
    finalCost = 0
    while nodesToExpand:
        node = nodesToExpand.pop()
        #Result found
        if isFinalState(node.state):
           finalCost, path = adaptSolution(node)
           return finalCost, path
        visitedNodes.append(node.state)
        for i, stack in enumerate(node.state):
            for j, new_stack in enumerate(node.state):
                auxState = copy.deepcopy(node.state)
                if i != j and len(stack) > 0 and len(new_stack) < maxHeight:
                    newState, newStateCost = moveBlock(auxState, i, j)
                    newNode = TreeNode(node, newState, [i, j], newStateCost + node.cost)
                    
                    #if the new node has not been visited, it is added to the visited list
                    if newNode.state not in visitedNodes and not any(n.state == newNode.state for n in nodesToExpand):
                        nodesToExpand.append(newNode)
                        nodesToExpand.sort(key = operator.attrgetter('cost'), reverse = True)
                    #if the node was visited before, we verify if the node's cost is higher than the new one
                    else:
                        for n in nodesToExpand:
                            if n.state == newNode.state and n.cost > newNode.cost:
                                nodesToExpand.remove(n)
                                nodesToExpand.append(newNode)
                                nodesToExpand.sort(key = operator.attrgetter('cost'), reverse = True)
    return finalCost, path

#Read the input file
reader = InputReader()
data = reader.read()

#Store the reading results in the global variables
maxHeight = data[0]
initialConfiguration = data[1]
goalState = data[2]

nodesToExpand = [TreeNode(None, initialConfiguration, None, 0)]
#Search
cost, path = aStar()
#Print solution
if len(path) > 0:
   # print len(visitedNodes)
    print(cost)
    print(''.join(item for item in path)[:-1][:-1])
else:
    print("No solution found")