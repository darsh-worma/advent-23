def main():
    file = open("data.txt", 'r')
    lines = file.readlines()
    matrix = []
    for line in lines:
        line_to_add = [*line]
        line_to_add.pop(-1)
        matrix.append(line_to_add)

    #print(matrix)
    #print(len(matrix))
        
    #check which rows have no galaxies
    i = 0
    while (i < len(matrix)):
        if (not(is_galaxy_in_row(matrix, i))):
            matrix.insert(i+1, matrix[i]) #insert row of dots if no galaxy present
            i += 2
        else:
            i += 1
    #check which cols have no galaxies
    i = 0
    while(i < len(matrix[0])):
        if(not(is_galaxy_in_col(matrix, i))):
            for j in range(len(matrix)):
                matrix[j].insert(i + 1, '.')
            i += 2
        else:
            i += 1
    
    max_galaxies = get_total_galaxies(matrix)
    matrix = get_numbered_galaxies(matrix)

    print(get_sum(matrix, max_galaxies))


def is_galaxy_in_row(matrix, row):
    for i in range(len(matrix[row])):
        if (matrix[row][i] == '#'):
            return True
    return False

def is_galaxy_in_col(matrix, col):
    for i in range(len(matrix)):
        if (matrix[i][col] == '#'):
            return True
    return False

def get_numbered_galaxies(matrix):
    galaxies = 1
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if (matrix[i][j] == '#'):
                matrix[i][j] = str(galaxies)
                galaxies += 1
    return matrix

def get_total_galaxies(matrix):
    galaxies = 1
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if (matrix[i][j] == '#'):
                matrix[i][j] = str(galaxies)
                galaxies += 1
    return (galaxies - 1)

def get_shortest_distance(ri, ci, rf, cf):
    return (abs(rf - ri) + abs(cf - ci))

def get_sum(matrix, max_galaxies):
    sum = 0
    for i in range(1, max_galaxies):
        for j in range(i+1, max_galaxies + 1):
            for ri in range(len(matrix)):
                for ci in range(len(matrix[ri])):
                    if (matrix[ri][ci].isdigit() and int(matrix[ri][ci]) == i):
                        for rf in range(len(matrix)):
                            for cf in range(len(matrix[rf])):
                                if (matrix[rf][cf].isdigit() and int(matrix[rf][cf]) == j):
                                    sum += get_shortest_distance(ri, ci, rf, cf)
                                    #print("distance between galaxy " + str(i) + " and " + str(j) + " is " + str(get_shortest_distance(ri, ci, rf, cf)))
    return sum



if __name__ == "__main__":
    main()

