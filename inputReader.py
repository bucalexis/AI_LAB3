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
