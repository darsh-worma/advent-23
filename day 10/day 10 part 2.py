north = ['|', 'L', 'J']
south = ['|', '7', 'F']
west = ['-', 'J', '7']
east = ['-', 'L', 'F']


def main():
    file = open("data.txt", 'r')
    lines = file.readlines()
    tile_matrix = []
    for line in lines:
        line_to_add = [*line]
        line_to_add.pop(-1)
        tile_matrix.append(line_to_add)
    #print(matrix)
    path_matrix = get_path_matrix(tile_matrix)
    
    enclosed_tiles = 0
    for i in range(len(path_matrix)):
        for j in range(len(path_matrix)):
            if(path_matrix[i][j] == None):
                parity = get_parity_count(tile_matrix, path_matrix, i, j)
                if (parity % 2 == 1):
                    enclosed_tiles += 1

    print(enclosed_tiles)



    
    
def get_path_matrix(tile_matrix):
    path_matrix = []
    for i in range(len(tile_matrix)):
        path_matrix.append([])
        for j in range(len(tile_matrix)):
            path_matrix[i].append(None)
    #return path_matrix
    
    count = 0
    current_row = get_start_row(tile_matrix)
    current_col = get_start_col(tile_matrix)
    current_tile = 'S'
    path_matrix[current_row][current_col] = count
    is_start_path_found = False
    while(not(is_start_path_found)):
        if (is_valid_move(tile_matrix[current_row - 1][current_col], "n")):
            is_start_path_found = True
            current_tile = tile_matrix[current_row - 1][current_col]
            current_row -= 1
            count += 1
            path_matrix[current_row][current_col] = count

        elif (is_valid_move(tile_matrix[current_row][current_col + 1], "e")):
            is_start_path_found = True
            current_tile = tile_matrix[current_row][current_col + 1]
            current_col += 1
            count += 1
            path_matrix[current_row][current_col] = count

        elif (is_valid_move(tile_matrix[current_row + 1][current_col], "s")):
            is_start_path_found = True
            current_tile = tile_matrix[current_row + 1][current_col]
            current_row += 1
            count += 1
            path_matrix[current_row][current_col] = count

        elif (is_valid_move(tile_matrix[current_row][current_col - 1], "w")):
            is_start_path_found = True
            current_tile = tile_matrix[current_row][current_col - 1]
            current_col -= 1
            count += 1
            path_matrix[current_row][current_col] = count

    #return current_tile, current_row, current_col
    

    while (current_tile != 'S'):
        if (path_matrix[current_row][current_col] > 1 and 
            ( (current_row > 0) and current_tile in north and (path_matrix[current_row - 1][current_col] == 0) or 
             ((current_col + 1 < len(path_matrix)) and current_tile in east and path_matrix[current_row][current_col + 1] == 0) or 
             ((current_row + 1 < len(path_matrix)) and current_tile in south and path_matrix[current_row + 1][current_col] == 0) or 
             ((current_col > 0) and current_tile in west and path_matrix[current_row][current_col - 1] == 0))):
            break

        elif ((current_row > 0) and 
              current_tile in north and
              path_matrix[current_row - 1][current_col] == None and 
              is_valid_move(tile_matrix[current_row - 1][current_col], "n")):
            current_tile = tile_matrix[current_row - 1][current_col]
            current_row -= 1
            count += 1
            path_matrix[current_row][current_col] = count

        elif ((current_col + 1 < len(path_matrix)) and 
              current_tile in east and
              path_matrix[current_row][current_col + 1] == None and 
              is_valid_move(tile_matrix[current_row][current_col + 1], "e")):
            current_tile = tile_matrix[current_row][current_col + 1]
            current_col += 1
            count += 1
            path_matrix[current_row][current_col] = count

        elif ((current_row + 1 < len(path_matrix)) and 
              current_tile in south and
              path_matrix[current_row + 1][current_col] == None and 
              is_valid_move(tile_matrix[current_row + 1][current_col], "s")):
            current_tile = tile_matrix[current_row + 1][current_col]
            current_row += 1
            count += 1
            path_matrix[current_row][current_col] = count

        elif ((current_col > 0) and 
              current_tile in west and
              path_matrix[current_row][current_col - 1] == None and 
              is_valid_move(tile_matrix[current_row][current_col - 1], "w")):
            current_tile = tile_matrix[current_row][current_col - 1]
            current_col -= 1
            count += 1
            path_matrix[current_row][current_col] = count

    return path_matrix

def is_inside(path_matrix, r, c):
    count = 0
    #before_row
    for i in range(c):
        if(isinstance(path_matrix[r][i], int)):
            count += 1
            break
    #after_row
    for i in range(len(path_matrix)):
        if (isinstance(path_matrix[r][i], int)):
            count += 1
            break

    #before_col
    for i in range(r):
        if (isinstance(path_matrix[i][c], int)):
            count += 1
            break
    
    #after_col
    for i in range(len(path_matrix)):
        if (isinstance(path_matrix[i][c], int)):
            count += 1
            break
    
    if (count == 4):
        return True
    return False


def get_parity_count(tile_matrix, path_matrix, r, c):
    parity = 0
    for i in range(c):
        if (path_matrix[r][i] != None and tile_matrix[r][i] == '|'):
            parity += 1
        elif (path_matrix[r][i] != None and tile_matrix[r][i] == 'F'):
            if(i + 1 < c):
                for j in range(i+1, c):
                    if (tile_matrix[r][j] != '-' and tile_matrix[r][j] != 'J'):
                        break
                    elif(tile_matrix[r][j] == 'J'):
                        parity += 1
                        break

        elif(path_matrix[r][i] != None and tile_matrix[r][i] == 'L'):
            if(i + 1 < c):
                for j in range(i+1, c):
                    if (tile_matrix[r][j] != '-' and tile_matrix[r][j] != '7'):
                        break
                    elif(tile_matrix[r][j] == '7'):
                        parity += 1
                        break
            
    return parity

def is_valid_move(tile, pos):
    if ( (pos == "n" and tile in south) or 
        (pos == "e" and tile in west) or 
        (pos == "s" and tile in north) or
        (pos == "w" and tile in east)):
        return True
    return False

def get_start_row(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if (matrix[i][j] == 'S'):
                return i
            
def get_start_col(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if (matrix[i][j] == 'S'):
                return j

if __name__ == "__main__":
    main()