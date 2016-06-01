import numpy

neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def h(a, b):
    """Return distance between 2 points"""
    return (b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2

def Astar(start, end, grid):
    """Return path between 2 points

    example :

    grid = [
        [0, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 0],
    ]
    path = Astar((3,3), (0, 0), grid)
    """
    array = numpy.array(grid)

    open_list = [] # Nodes to analyze
    close_list = [] # Nodes already analyzed
    came_from = {} # List of parents

    # Add F score in open_list
    gscore = {start:0}
    fscore = {start:h(start, end)}
    open_list.append((fscore[start], start))

    while open_list:

        # Get min F value in open_list
        minf = min(open_list, key=lambda o: o[0])
        current = minf[1]
        open_list.remove(minf)

        # Return path
        if current == end:
            data = []
            while current in came_from:
                data.append(list(current))
                current = came_from[current]
            return data[::-1]

        # Add current node in close_list
        close_list.append(current)

        # For neighbors
        for i, j in neighbors:
            neighbor = current[0] + i, current[1] + j
            tentative_g_score = gscore[current] + h(current, neighbor)

            # Check neighbor value
            if 0 <= neighbor[0] < array.shape[0]:
                if 0 <= neighbor[1] < array.shape[1]:
                    if array[neighbor[0]][neighbor[1]] == 1:
                        continue
                else:
                    continue
            else:
                continue

            # Continue if neighbor is in close list
            if neighbor in close_list and tentative_g_score >= gscore.get(neighbor, 0):
                continue

            # If neighbor is not in open_list
            if tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1]for i in open_list]:
                came_from[neighbor] = current
                gscore[neighbor] = tentative_g_score
                fscore[neighbor] = tentative_g_score + h(neighbor, end)
                open_list.append((fscore[neighbor], neighbor))

    return False
