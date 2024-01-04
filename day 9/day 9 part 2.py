def main():
    file = open("data.txt", 'r')
    lines = file.readlines()
    matrix = []
    for line in lines:
        matrix.append(line.split(' '))
    for line in matrix:
        line[-1] = line[-1].strip('\n')
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = int(matrix[i][j])
    #print(matrix)
            
    first_vals = []
    for line in matrix:
        first_val = get_first_val(line)
        first_vals.append(first_val)
    print(sum(first_vals))
    
    

def get_first_val(line):
    matrix = []
    matrix.append(line)
    while (not(is_all_zero(matrix[-1]))):
        add_line = []
        for i in range(1, len(matrix[-1])):
            add_line.append(matrix[-1][i] - matrix[-1][i - 1])
        matrix.append(add_line)
    matrix[-1].insert(0, 0)
    for i in range(2, len(matrix) + 1):
        length = len(matrix)
        matrix[length - i].insert(0, matrix[length - i][0] - matrix[length - i + 1][0])
    
    return matrix[0][0]


def is_all_zero(nums):
    for num in nums:
        if(num != 0):
            return False
    return True

if __name__ == '__main__':
    main()