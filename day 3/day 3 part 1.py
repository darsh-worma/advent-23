def main():
  file = open("data.txt", 'r')
  data = file.readlines()
  data_arr = []
  for line in data:
    row = []
    for char in line:
      if (char != '\n'):
        row.append(char)
    data_arr.append(row)
  #print(data_arr)

  print(getSum(data_arr))
      
      
def getSum(data):
  big_data = []
  symbols = ['%', '*', '#', '&', '$', '@', '/', '=', '+', '-']
  sum = 0
  num = []
  is_adj = False
  for i in range(len(data)):
    for j in range(len(data[i])):
      big_data.append(data[i][j]) 
      if (not(data[i][j].isdigit())):
        if (is_adj and len(big_data) > 1 and big_data[len(big_data) - 2].isdigit()):
          num_to_add = ""
          for number in num:
            num_to_add += number
          num.clear()
          #print(num_to_add)
          sum += int(num_to_add)
        elif(not(is_adj)):
          num.clear()
        is_adj = False
      elif(data[i][j].isdigit()):
        num.append(data[i][j])
        if (not(is_adj) and 
            (i >= 1 and j >= 1 and data[i-1][j-1] in symbols) or 
            (i >= 1 and data[i-1][j] in symbols) or 
            (i >= 1 and j < (len(data[i]) - 1) and data[i-1][j+1] in symbols) or 
            (j >= 1 and data[i][j-1] in symbols) or 
            (j < (len(data[i]) - 1) and data[i][j+1] in symbols) or 
            (i < (len(data) - 1) and j >= 1 and data[i+1][j-1] in symbols) or 
            (i < (len(data) - 1) and data[i+1][j] in symbols) or 
            (i < (len(data) - 1) and j < (len(data[i]) - 1) and data[i+1][j+1] in symbols)
            ):
          is_adj = True

  return sum
if __name__ == "__main__":
  main()