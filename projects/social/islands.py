def island_counter(islands):
    matrix = [[cell for cell in row] for row in islands]
    components = 0
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if matrix[y][x] == 0:
                continue
            elif matrix[y][x] == 1:
                components += 1
                stack = [(y, x)]
                while stack:
                    row, cell = stack.pop()
                    matrix[row][cell] = 2
                    # above
                    if row > 0 and matrix[row - 1][cell] == 1:
                        matrix[row - 1][cell] == 2
                        stack.append((row - 1, cell))
                    # below
                    if row < len(matrix) - 1 and matrix[row + 1][cell] == 1:
                        matrix[row + 1], [cell] == 2
                        stack.append((row + 1, cell))
                    # left
                    if cell > 0 and matrix[row][cell - 1] == 1:
                        matrix[row][cell - 1] == 2
                        stack.append((row, cell - 1))
                    # right
                    if cell < len(matrix[row]) - 1 and matrix[row][cell + 1] == 1:
                        matrix[row][cell + 1] == 2
                        stack.append((row, cell + 1))

                # for row in matrix:
                #     print(row)
    return components
                    
               



islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

print(island_counter(islands))

islands_2 = [[1, 0, 0, 1, 1, 0, 1, 1, 0, 1],
             [0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
             [0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
             [0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
             [0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
             [0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
             [0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
             [1, 0, 1, 1, 0, 0, 0, 1, 1, 0],
             [0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
             [0, 0, 1, 1, 0, 1, 0, 0, 1, 0]]

print(island_counter(islands_2))