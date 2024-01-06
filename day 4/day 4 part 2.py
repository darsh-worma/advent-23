def main():
  myfile = open("data.txt", 'r')
  lines = myfile.readlines()
  matches = []
  for line in lines:
    card = line.split(': ')[1]
    winnings = card.split(' | ')[0]
    winnings = winnings.split(' ')
    final_winnings = [''] * 10
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
    final_options = [''] * 25
    j = 0
    for i in range(len(options)):
      if (options[i].isdigit()):
        final_options[j] = options[i]
        j += 1
      if (j == 25):
        break
        
    #print(final_winnings)
    #print(final_options)
    num_matches = 0
    for winning in final_winnings:
      for option in final_options:
        if (winning == option):
          num_matches += 1
    matches.append(num_matches)
  #print(matches)
  #print(len(matches))

  copies = [1] * 196
  #print(copies)
  for i in range(len(copies)):
    m = matches[i]
    for j in range(i+1, i+1+m):
      copies[j] += copies[i]

  print(sum(copies))
  
if __name__ == "__main__":
    main()