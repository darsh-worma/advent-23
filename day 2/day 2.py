def main():
  f = open("data.txt", 'r')
  data = f.readlines()
  games = []
  for line in data:
    game = split_to_games(line)
    games.append(game)

  moves = []
  for game in games:
    moves.append(game[1])
  #print(moves)

  subgames = []
  for move in moves:
    subgames.append(split_to_subgames(move))
  #print(subgames)

  arr = []
  for subgame in subgames:
    arr.append(split_to_color(subgame))
    
  total = []
  for i in range(len(arr)):
    smalltotal = []
    for j in range(len(arr[i])):
      nums = [0, 0, 0]
      for k in range(len(arr[i][j])):
        digit = ""
        for char in arr[i][j][k]:
          if (char.isdigit()):
            digit += char
        if ("red" in arr[i][j][k]):
          nums[0] = int (digit)
        elif ("green" in arr[i][j][k]):
          nums[1] = int (digit)
        elif ("blue" in arr[i][j][k]):
          nums[2] = int (digit)
      smalltotal.append(nums)
    total.append(smalltotal)

  #this was all to clean the data to be in the form of a 3d array of values rgb
  #print(total)
  
  #print(getTotal(total))

  print(getPowerSum(total))
  

def split_to_games(game):
  return game.split(':')

def split_to_subgames(move):
  return move.split(';')

def split_to_color(subgame):
  arr = []
  for colors in subgame:
    arr.append(colors.split(','))
  return arr

def getTotal(total):
  sum = 0
  for i in range(len(total)):
    sum += (i+1)
    for j in range(len(total[i])):
        if (total[i][j][0] > 12) or (total[i][j][1] > 13) or (total[i][j][2] > 14):
          sum -= (i+1)
          break
  return sum

def getPowerSum(total):
  sum = 0
  for i in range(len(total)):
    min_red = 0
    min_green = 0
    min_blue = 0
    for j in range (len(total[i])):
      if (total[i][j][0] > min_red):
        min_red = total[i][j][0]
      if (total[i][j][1] > min_green):
        min_green = total[i][j][1]
      if (total[i][j][2] > min_blue):
        min_blue = total[i][j][2]
    power = (min_red * min_green * min_blue)
    sum += power
  return sum

if __name__ == '__main__':
    main()