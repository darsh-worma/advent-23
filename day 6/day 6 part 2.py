def main():
    print(get_ways(54817088, 446129210351007))

def get_ways(time, max_distance):
    count = 0
    for i in range(time):
        time_held = i
        time_left = time - time_held
        speed = time_held
        distance = speed * time_left
        if (distance > max_distance):
            count += 1
    return count

if __name__ == '__main__':
    main()