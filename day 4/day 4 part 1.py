def main():
  myfile = open("data.txt", 'r')
  lines = myfile.readlines()
  sum = 0
  for line in lines:
    card = line.split(': ')[1]
    winnings = card.split(' | ')[0]
    winnings = winnings.split(' ')
    final_winnings = ['', '', '', '', '', '', '', '', '', '']
    j = 0
    for i in range(len(winnings)):
      if (winnings[i].isdigit()):
        final_winnings[j] = winnings[i]
        j += 1
      if (j == 10):
        break
        
    options = card.split(' | ')[1]
    options = options.split(' ')
    options[-1] = options[-1].strip('\n')
    #print(options)
    final_options = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
    j = 0
    for i in range(len(options)):
      if (options[i].isdigit()):
        final_options[j] = options[i]
        j += 1
      if (j == 25):
        break
        
    #print(final_winnings)
    #print(final_options)
    matches = 0
    for winning in final_winnings:
      for option in final_options:
        if (winning == option):
          matches += 1
    #print(matches)
    if (matches != 0):
      sum += 2 ** (matches - 1)
  print(sum)

if __name__ == "__main__":
    main()