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
            
    next_vals = []
    for line in matrix:
        next_val = get_next_num(line)
        next_vals.append(next_val)
    print(sum(next_vals))

def get_next_num(line):
    matrix = []
    matrix.append(line)
    while (not(is_all_zero(matrix[-1]))):
        add_line = []
        for i in range(1, len(matrix[-1])):
            add_line.append(matrix[-1][i] - matrix[-1][i - 1])
        matrix.append(add_line)
    matrix[-1].append(0)
    for i in range(2, len(matrix) + 1):
        length = len(matrix)
        matrix[length - i].append(matrix[length - i][-1] + matrix[length - i + 1][-1])
    
    return matrix[0][-1]


    


def is_all_zero(nums):
    for num in nums:
        if(num != 0):
            return False
    return True

if __name__ == '__main__':
    main()