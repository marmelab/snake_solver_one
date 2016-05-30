import numpy

neighbors = [(0,1),(0,-1),(1,0),(-1,0)]

def h(a, b):
    return (b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2

def Astar(start, end, grid):
    array = numpy.array(grid)

    open_list = []
    close_list = set()
    came_from = {}

    gscore = {start:0}
    fscore = {start:h(start, end)}
    open_list.append((fscore[start], start))

    while open_list:

        minf = min(open_list, key=lambda o:o[0])
        current = minf[1]
        open_list.remove(minf)

        if current == end:
            data = []
            while current in came_from:
                data.append(list(current))
                current = came_from[current]
            return data[::-1]

        close_list.add(current)
        for i, j in neighbors:
            neighbor = current[0] + i, current[1] + j
            tentative_g_score = gscore[current] + h(current, neighbor)
            if 0 <= neighbor[0] < array.shape[0]:
                if 0 <= neighbor[1] < array.shape[1]:
                    if array[neighbor[0]][neighbor[1]] == 1:
                        continue
                else:
                    continue
            else:
                continue

            if neighbor in close_list and tentative_g_score >= gscore.get(neighbor, 0):
                continue

            if tentative_g_score > gscore.get(neighbor, 0) or neighbor not in [i[1]for i in open_list]:
                came_from[neighbor] = current
                gscore[neighbor] = tentative_g_score
                fscore[neighbor] = tentative_g_score + h(neighbor, end)
                open_list.append((fscore[neighbor], neighbor))

    return False
