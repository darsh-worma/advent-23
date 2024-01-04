def main():
    path = "LRRLRRRLRRRLLRRLRRLRLRLRRLLRRLRRLRRRLLLRRRLRRRLRRRLLRRRLRRLLRRLRRLRLRRRLRRLRLRRLRRRLLRRLLRLRRRLLRRLRRLLLRLRRRLRLRLRLLRRRLRLLRRRLRLRRRLRRRLLRRLRRRLLRRLRLLRLRRLLLRRLRRLLLRLLRLRRRLRLRLRRRLRRLLRRRLRLRLRRLRRRLRLRRLRRLRRRLRRRLRRRLRRRLRRLLRRLRLLRRLLRRRLRLLRLRLRRLRRLRLRLRRRLRLRLRRLRLRRLRRRR"
    file = open("data.txt", 'r')
    lines = file.readlines()
    nodes = []
    nct = [] #nodes_connected_to
    for line in lines:
        nodes.append(line.split('=')[0].strip(' '))
        nct_to_add = []
        nct_to_add.append(((line.split(' = ')[1]).split(', ')[0]).strip('('))
        nct_to_add.append(((line.split(' = ')[1]).split(', ')[1]).strip(')\n'))
        nct.append(nct_to_add)
    
    print(get_steps(path, nodes, nct))

    
def get_steps(path, nodes, nct):
    steps = 0
    steps_arr = []
    current_nodes = []
    for node in nodes:
        if (node[-1] == 'A'):
            current_nodes.append(node)

    for node in current_nodes:
        while (node[-1] != 'Z'):
            for i in range(len(path)):
                index = nodes.index(node)
                current_move = path[i]
                if (current_move == 'L'):
                    node = nct[index][0]
                elif (current_move == 'R'):
                    node = nct[index][1]
            steps += len(path)
        steps_arr.append(steps)
        steps = 0
    #print(steps_arr)
        
    import math
    from math import lcm
    return math.lcm(*steps_arr)

if __name__ == '__main__':
    main()