def main():
    times = [54,81,70,88]
    distances = [446,1292,1035,1007]
    ways = []

    for i in range(len(times)):
        ways.append(get_ways(times[i], distances[i]))
    product = 1
    
    for way in ways:
        product *= way
    print(product)

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