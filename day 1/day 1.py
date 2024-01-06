def main():
  f = open("data.txt", 'r')
  lines = f.readlines()
  nums = []
  for line in lines:
    first_num = extract_first_num(line)
    second_num = extract_second_num(line)
    num = combine_nums(first_num, second_num)
    nums.append(num)

  print(getSum(nums))
  
  
def extract_first_num(input_list):
  wordToNum = {"one" : "1" , 
               "two" : "2" , 
               "three" : "3" , 
               "four" : "4", 
               "five" : "5", 
               "six" : "6", 
               "seven" : "7", 
               "eight" : "8", 
               "nine" : "9"}
  first_num = ""
  check = ""
  for let in input_list:
    if (let.isdigit()):
      first_num = let
      return first_num
    else:
      check += let
      for word, num in wordToNum.items():
        if (word in check):
          first_num = num
          return first_num
          
def extract_second_num(input_list):
  wordToNum = {"one" : "1" , 
     "two" : "2" , 
     "three" : "3" , 
     "four" : "4", 
     "five" : "5", 
     "six" : "6", 
     "seven" : "7", 
     "eight" : "8", 
     "nine" : "9"}
  second_num = ""
  check = ""
  i = len(input_list) - 1
  while (i >= 0):
    if (input_list[i].isdigit()):
      second_num = input_list[i]
      return second_num
    else:
      check = input_list[i] + check
      for word, num in wordToNum.items():
        if (word in check):
          second_num = num
          return second_num
    i -= 1

def combine_nums(num1, num2):
  num = num1 + num2
  return int(num)
  
def getSum(nums):
  sum = 0
  for num in nums:
    sum += num
  return sum

if __name__ == "__main__":
  main()