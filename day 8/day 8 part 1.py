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
    count = 0
    node = "AAA"
    while(node != "ZZZ"):
        for i in range(len(path)):
            index = nodes.index(node)
            current_move = path[i]
            if (current_move == 'L'):
                node = nct[index][0]
                count += 1
            elif (current_move == 'R'):
                node = nct[index][1]
                count += 1
    return count


if __name__ == '__main__':
    main()

