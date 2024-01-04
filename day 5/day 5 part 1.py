import copy

def main():
  #seed = [79, 14, 55, 13]
  seed = [3489262449, 222250568, 2315397239, 327729713, 1284963, 12560465, 1219676803, 10003052, 291763704, 177898461, 136674754, 107182783, 2917625223, 260345082, 1554280164, 216251358, 3900312676, 5629667, 494259693, 397354410]

  soil = copy.deepcopy(seed)
  #print(seed)
  seed_to_soil = open("seed-to-soil.txt", 'r')
  lines = seed_to_soil.readlines()
  soil = update_map(seed, soil, lines)
  seed_to_soil.close()
  #print(soil)
  
  soil_to_fertilizer = open("soil-to-fertilizer.txt", 'r')
  lines = soil_to_fertilizer.readlines()
  fertilizer = copy.deepcopy(soil)
  fertilizer = update_map(soil, fertilizer, lines)
  soil_to_fertilizer.close()
  #print(fertilizer)
  
  fertilizer_to_water = open("fertilizer-to-water.txt", 'r')
  lines = fertilizer_to_water.readlines()
  water = copy.deepcopy(fertilizer)
  water = update_map(fertilizer, water, lines)
  fertilizer_to_water.close()
  #print(water)

  water_to_light = open("water-to-light.txt", 'r')
  lines = water_to_light.readlines()
  light = copy.deepcopy(water)
  light = update_map(water, light, lines)
  water_to_light.close()
  #print(light)

  light_to_temperature = open("light-to-temperature.txt", 'r')
  lines = light_to_temperature.readlines()
  temperature = copy.deepcopy(light)
  temperature = update_map(light, temperature, lines)
  light_to_temperature.close()
  #print(temperature)

  temperature_to_humidity = open("temperature-to-humidity.txt", 'r')
  lines = temperature_to_humidity.readlines()
  humidity = copy.deepcopy(temperature)
  humidity = update_map(temperature, humidity, lines)
  temperature_to_humidity.close()
  #print(humidity)

  humidity_to_location = open("humidity-to-location.txt", 'r')
  lines = humidity_to_location.readlines()
  location = copy.deepcopy(humidity)
  location = update_map(humidity, location, lines)
  humidity_to_location.close()
  #print(location)

  print(min(location))
  


#...........................................................................
def update_map(source_arr, destination_arr, lines):
  for line in lines:
    #print(line)
    line = line.split(' ')
    line[-1] = line[-1].strip('\n')
    #print(line)
    for i in range(len(line)):
      line[i] = int(line[i])
    #print(line)
    destination = line[0]
    source = line[1]
    range_length = line[2]
    #print(destination, source, range_length)
    for i in range(len(source_arr)):
      if (source_arr[i] >= source and source_arr[i] < (source + range_length)):
        difference = source_arr[i] - source
        destination_arr[i] = destination + difference
  return destination_arr
      

if __name__ == '__main__':
    main()