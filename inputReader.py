import fileinput
class InputReader():

    def read(self):
        input = fileinput.input()
        numberOfLine = 1
        for line in input:
            if numberOfLine == 1:
                maxHeight = int(line)
            elif numberOfLine == 2:
                initialConfiguration = line.strip().replace(" ", "").replace("(", "").replace(")", "").split(";")
                for i, element in enumerate(initialConfiguration):
                    initialConfiguration[i] = element.split(",")
                    if (initialConfiguration[i] == ['']):
                        initialConfiguration[i].pop()
            elif numberOfLine == 3:
                goalState = line.strip().replace(" ", "").replace("(", "").replace(")", "").split(";")
                for i, element in enumerate(goalState):
                    goalState[i] = element.split(",")
                    if (goalState[i] == ['']):
                        goalState[i].pop()
            numberOfLine += 1
        return maxHeight, initialConfiguration, goalState

    def readDFS(self):
        input = fileinput.input() #Input
        i = 0
        for line in input:  #Read line by line
            i += 1
            if i == 1:  #Reads first line (maximum stack height)
                maxHeight = int(line.strip())
            elif i == 2:  #Reads second line (intial state)
                initialConfiguration = line.strip()
                initialConfiguration = initialConfiguration.replace(" ", "")
                initialConfiguration = initialConfiguration.replace("(", "")
                initialConfiguration = initialConfiguration.replace(")", "")
                initialConfiguration = initialConfiguration.split(';')
                for i, element in enumerate(initialConfiguration):
                    initialConfiguration[i] = element.split(",")
                    if (initialConfiguration[i] == ['']):
                        initialConfiguration[i].pop()
            else:  #Reads the third line (end state)
                goalState = line.strip()
                goalState = goalState.replace(" ", "")
                goalState = goalState.replace("(", "")
                goalState = goalState.replace(")", "")
                goalState = goalState.replace("X", "")
                goalState = goalState.split(';')
                for i, element in enumerate(goalState):
                    goalState[i] = element.split(",")
                    if (goalState[i] == ['']):
                        goalState[i].pop()
                break
        return  maxHeight, initialConfiguration, goalState