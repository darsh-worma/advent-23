north = ['|', 'L', 'J']
south = ['|', '7', 'F']
west = ['-', 'J', '7']
east = ['-', 'L', 'F']
test = "asdfsd"

def main():
    file = open("data.txt", 'r')
    lines = file.readlines()
    matrix = []
    for line in lines:
        line_to_add = [*line]
        line_to_add.pop(-1)
        matrix.append(line_to_add)
    #print(matrix)
    print(get_path_matrix(matrix))
    
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

    return (count + 1)//2

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