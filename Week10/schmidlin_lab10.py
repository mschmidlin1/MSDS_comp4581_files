# Finds ALL ways to place n nonattacking queens on a n x n board
# : State[i] is the row for the queen on Column i
# : There are solutions for n>3
# Stack ADT with list implementation from Lab 5
class MyStack(object):
    def __init__(self, type): # Creates an empty list
        self.elemType = type
        self.state = [] # Empty list
    def __str__(self): # for print
        return str(self.state)
    def empty(self):
        return len(self.state) == 0
    def push(self, elem): # Adds an element to the top of a stack
        assert type(elem) == self.elemType
        self.state.append(elem)
    def pop(self): # Removes an element from the top of the stack
        if self.empty():
            raise ValueError("Requested top of an empty stack")
        else:
            return self.state.pop()
    def top(self): # Returns the top of a nonempty stack
        if self.empty():
            raise ValueError("Requested top of an empty stack")
        else:
            return self.state[-1]

def nQueens(n):
    # Each state will include only the queens that have been placed so far
    initialState = [] # Initial empty state
    s = MyStack(list) # For a depth first search
    s.push(initialState) # Push the initial state onto the Stack
    # While we still have states to explore
    while not s.empty():
        currentState = s.pop() # Grab the next state
        currentCol = len(currentState)
        # See if we found a solved state at a leaf node
        # That is, we have filled in every column with a queen
        if currentCol == n:
            print(currentState) # Display the solution
        else:
            # Produce the state's children (if they are feasible)
            # Note children are produced backward so they come off the
            # stack later left to right
            for currentRow in range(n,0,-1):
            # Check horizontal and both diagonals of previous queens
                feasible = True
                for previousCol in range(currentCol):
                    if (currentState[previousCol] == currentRow) or abs(currentState[previousCol]-currentRow) == (currentCol - previousCol):
                        feasible = False
                        break
                if feasible:
                    # Create child by making a copy and appending new col
                    childState = currentState.copy()
                    childState.append(currentRow)
                    s.push(childState) # Push child onto data structure

def graphColoring(graph, colors):
    # Each state is only the nodes that have been colored so far
    initialState = [] # Initial empty state
    s = MyStack(list) # For a depth first search
    s.push(initialState) # Push the initial state onto the Stack
    # While we still have states to explore
    n = len(graph)
    while not s.empty():
        currentState = s.pop() # Grab the next state
        currentNode = len(currentState)
        # See if we found a solved state at a leaf node
        # That is, we have all the nodes colored in the graph.
        if currentNode == n:
            print(currentState)
            return currentState
        else:
            # Produce the state's children (if they are feasible)
            # Note children are produced backward so they come off the
            # stack later left to right

            possibleColoredNeighbors=graph[currentNode][:currentNode]

            for color in reversed(colors):
                if currentNode==0:
                    childState = currentState.copy()
                    childState.append(color)
                    s.push(childState)
                    continue
                feasible=True
                for i in range(currentNode):
                    if possibleColoredNeighbors[i] & (currentState[i]==color):
                        feasible=False
                        break
                if feasible:
                    childState = currentState.copy()
                    childState.append(color)
                    s.push(childState) 


def main():
    # Testing code (check 4,5,6,7)
    # for n in range(4,8):
    #     nQueens(n)

    graph = [[False, True, False, False, False, True ],
            [True, False, True, False, False, True ],
            [False, True, False, True, True, False],
            [False, False, True, False, True, False],
            [False, False, True, True, False, True ],
            [True, True, False, False, True, False]]

    colors = ['r', 'g', 'b']

    graphColoring(graph, colors)


if __name__=="__main__":
    main()