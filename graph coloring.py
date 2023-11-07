def printConfiguration(colorArray):
    print("The assigned colors are as follows:")
    for i in range(4):
        print("Vertex:", i, "Color:", colorArray[i])

def isSafe(graph, colorArray, vertex, color):
    # Check if it's safe to color 'vertex' with 'color'
    for i in range(4):
        if graph[vertex][i] and colorArray[i] == color:
            return False
    return True

def graphColoringAlgorithm(graph, m, vertex, colorArray):
    # If all vertices are colored, print the configuration
    if vertex == 4:
        printConfiguration(colorArray)
        return True

    # Try coloring the current vertex with different colors
    for color in range(1, m + 1):
        if isSafe(graph, colorArray, vertex, color):
            colorArray[vertex] = color

            # Recursively color the next vertex
            if graphColoringAlgorithm(graph, m, vertex + 1, colorArray):
                return True

            # Backtrack if coloring with this color didn't work
            colorArray[vertex] = 0

    return False

if __name__ == '__main__':
    graph = [
        [0, 1, 1, 1],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [1, 0, 1, 0],
    ]
    m = 3
    colorArray = [0] * 4  # Initialize the color array with 0

    if graphColoringAlgorithm(graph, m, 0, colorArray):
        print("Coloring is possible!")
    else:
        print("Coloring is not possible!")
