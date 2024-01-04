def main():
    #print(get_strength("32T3K"))
    
    hands = []
    bids = []
    file = open("data.txt", 'r')
    lines = file.readlines()
    for line in lines:
        hands.append(line.split(' ')[0])
        bids.append(line.split(' ')[1].strip())

    for i in range(len(hands)):
        hands[i]= hands[i].replace('T', 'D')
        hands[i]= hands[i].replace('J', '1')
        hands[i]= hands[i].replace('Q', 'F')
        hands[i]= hands[i].replace('K', 'G')
        hands[i]= hands[i].replace('A', 'H')
    
    #print(hands)
    #print(get_ranked(hands))
    
    ranked_hands = get_ranked(hands)
    print(get_total_winnings(hands, ranked_hands, bids))
    
    
def get_strength(hand):
    dict = {}
    j_count = 0
    for i in range(len(hand)):
        if (i == 0 and hand[i] != '1'):
            dict[hand[i]] = 1
        elif (hand[i] == '1'):
            j_count += 1
        else:
            is_found = False
            key_copy = tuple(dict.keys())
            for key in key_copy:
                if (str(hand[i]) == key):
                    dict[key] += 1
                    is_found = True
                    break
            if (not(is_found)):
                dict[hand[i]] = 1
    #return dict
    
    if (hand == "11111"):
        counts = [j_count]
    else:
        counts = []
        for key in dict.keys():
            counts.append(dict[key])
        counts = sorted(counts)
        counts[-1] += j_count
        #return counts

    if (sum(counts) != 5):
        print("oops")
        
    strength = None
    if (counts == [1,1,1,1,1]): #high card
        strength = 0 
    elif (counts == [1,1,1,2]): #one pair
        strength = 1
    elif (counts == [1,2,2]): #two pair
        strength = 2
    elif (counts == [1,1,3]): #three of a kind
        strength = 3 
    elif (counts == [2,3]): #full house
        strength = 4
    elif (counts == [1,4]): #four of a kind
        strength = 5
    elif (counts == [5]): #five of a kind
        strength = 6
    
    return strength

def get_ranked(hands):
    ranked_hands = []
    strengths = []
    for hand in hands:
        strengths.append(get_strength(hand))
    indices = []
    for i in range(7):
        indices_to_add = []
        for j in range(len(strengths)):
            if (strengths[j] == i):
                indices_to_add.append(j)
        indices.append(indices_to_add)
    
    for indices_set in indices:
        hands_to_sort = []
        for index in indices_set:
            hands_to_sort.append(hands[index])
        sorted_hands = sorted(hands_to_sort)
        for sorted_hand in sorted_hands:
            ranked_hands.append(sorted_hand)
    
    return ranked_hands

    
def get_total_winnings(hands, ranked_hands, bids):
    sum = 0
    for i in range(len(ranked_hands)):
        index = hands.index(ranked_hands[i])
        sum += (i+1) * int(bids[index])
    return sum


if __name__ == '__main__':
    main()