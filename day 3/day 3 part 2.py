class Number:
  def __init__(self, num, gear_row, gear_col):
    self.num = num
    self.gear_row = gear_row
    self.gear_col = gear_col

  def get_num(self):
    return self.num

  def get_gear_row(self):
    return self.gear_row

  def get_gear_col(self):
    return self.gear_col

#.........................................................................................

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

  obj_nums = get_obj_nums(data_arr)
  #for num in obj_nums:
    #print(f"number is {num.num}, x-coor is {num.coordinate.x}, y-coor is {num.coordinate.y}")
  gears = []
  for i in range(len(obj_nums)):
    coordinate_count = 0
    for j in range(len(obj_nums)):
      if (obj_nums[j].gear_row == obj_nums[i].gear_row and 
          obj_nums[j].gear_col == obj_nums[i].gear_col):
        coordinate_count += 1
    if (coordinate_count == 2):
      gears.append(obj_nums[i])
  sum = 0
  for i in range(len(gears)):
    for j in range(len(gears)):
      if (gears[i] != gears[j] and 
          gears[i].gear_row == gears[j].gear_row and 
          gears[i].gear_col == gears[j].gear_col):
        sum += (gears[i].num * gears[j].num)

  print(sum//2)


#.........................................................................................
def get_obj_nums(data):
  big_data = []
  int_numbers = []
  obj_numbers = []
  gear_row = None
  gear_col = None
  is_adj = False
  for i in range(len(data)):
    for j in range(len(data[i])):
      big_data.append(data[i][j]) 
      if (not(data[i][j].isdigit())):
        if (is_adj and len(big_data) > 1 and big_data[len(big_data) - 2].isdigit()):
          num_to_add = ""
          for number in int_numbers:
            num_to_add += number
          int_numbers.clear()
          #print(num_to_add)
          obj_numbers.append(Number(int(num_to_add), gear_row, gear_col))
        elif(not(is_adj)):
          int_numbers.clear()
        is_adj = False
      elif(data[i][j].isdigit()):
        int_numbers.append(data[i][j])
        if (not(is_adj) and (i >= 1 and j >= 1 and data[i-1][j-1] == '*')):
          gear_row = i - 1
          gear_col = j - 1
          is_adj = True
        elif (not(is_adj) and (i >= 1 and data[i-1][j] == '*')):
          gear_row = i - 1
          gear_col = j
          is_adj = True
        elif (not(is_adj) and (i >= 1 and j < (len(data[i]) - 1) and data[i-1][j+1] == '*')):
          gear_row = i - 1
          gear_col = j + 1
          is_adj = True
        elif (not(is_adj) and  (j >= 1 and data[i][j-1] == '*')):
          gear_row = i
          gear_col = j - 1
          is_adj = True
        elif (not(is_adj) and (j < (len(data[i]) - 1) and data[i][j+1] == '*')):
          gear_row = i
          gear_col = j + 1
          is_adj = True
        elif (not(is_adj) and (i < (len(data) - 1) and j >= 1 and data[i+1][j-1] == '*')):
          gear_row = i + 1
          gear_col = j - 1
          is_adj = True
        elif (not(is_adj) and  (i < (len(data) - 1) and data[i+1][j] == '*')):
          gear_row = i + 1
          gear_col = j
          is_adj = True
        elif (not(is_adj) and 
              (i < (len(data) - 1) and 
               j < (len(data[i]) - 1) and 
               data[i+1][j+1] == '*')):
          gear_row = i + 1
          gear_col = j + 1
          is_adj = True

  return obj_numbers


if __name__ == "__main__":
  main()