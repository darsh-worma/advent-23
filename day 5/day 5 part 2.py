import copy

def main():
  #seed = [79, 14, 55, 13]
  seed = [3489262449, 222250568, 2315397239, 327729713, 1284963, 12560465, 1219676803, 10003052, 291763704, 177898461, 136674754, 107182783, 2917625223, 260345082, 1554280164, 216251358, 3900312676, 5629667, 494259693, 397354410]
  print(get_min(seed))
  
#...........................................................................
def update_map(initial, final, lines):
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
    if (initial >= source and initial < (source + range_length)):
        difference = initial - source
        final = destination + difference
  return final
      
def get_min(seeds):
  min_location = None
  for i in range(0, len(seeds), 2):
    for j in range(seeds[i+1]):
      initial = seeds[i] + j
      final = None
      seed_to_soil = open("seed-to-soil.txt", 'r')
      lines = seed_to_soil.readlines()
      seed_to_soil.close()
      final = update_map(initial, final, lines)
      
      initial = copy.deepcopy(final)
      soil_to_fertilizer = open("soil-to-fertilizer.txt", 'r')
      lines = soil_to_fertilizer.readlines()
      soil_to_fertilizer.close()
      final = update_map(initial, final, lines)

      initial = copy.deepcopy(final)
      fertilizer_to_water = open("fertilizer-to-water.txt", 'r')
      lines = fertilizer_to_water.readlines()
      fertilizer_to_water.close()
      final = update_map(initial, final, lines)

      initial = copy.deepcopy(final)
      water_to_light = open("water-to-light.txt", 'r')
      lines = water_to_light.readlines()
      water_to_light.close()
      final = update_map(initial, final, lines)

      initial = copy.deepcopy(final)
      light_to_temperature = open("light-to-temperature.txt", 'r')
      lines = light_to_temperature.readlines()
      light_to_temperature.close()
      final = update_map(initial, final, lines)

      initial = copy.deepcopy(final)
      temperature_to_humidity = open("temperature-to-humidity.txt", 'r')
      lines = temperature_to_humidity.readlines()
      temperature_to_humidity.close()
      final = update_map(initial, final, lines)

      initial = copy.deepcopy(final)
      humidity_to_location = open("humidity-to-location.txt", 'r')
      lines = humidity_to_location.readlines()
      humidity_to_location.close()
      final = update_map(initial, final, lines)
      
      if (i == 0 and j == 0):
        min_location = copy.deepcopy(final)
        #print(min_location)
      else:
        if (final < min_location):
          min_location = copy.deepcopy(final)
          #print(min_location)
  return min_location

if __name__ == '__main__':
    main()