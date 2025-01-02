import re

# for input to work on part2 I removed the new lines
filename='day3.input'

lines=[]

with open(filename) as f:
  for l in f:
    lines.append(l)

def calc_line_sum(line)-> int:
  sum=0

  # parse line to find legit muls
  pattern=re.compile(r'mul\(\d{1,3},\d{1,3}\)')
  matches=pattern.findall(line)

  # parse each mul to calculate the multiplication
  for match in matches:
    num_pattern=re.compile(r'\d{1,3}')
    nums=num_pattern.findall(match)
    sum+=int(nums[0])*int(nums[1])

  return sum

def calc_line_sum_do_dont(line)-> int:
  sum=0

  pattern=re.compile(r'mul\(\d{1,3},\d{1,3}\)')
  matches_all=pattern.findall(line)

  pattern_ignore=re.compile(r'don\'t\(\)(.*?(mul\(\d{1,3},\d{1,3}\))+.*?)do\(\)')
  matches_dont_do=pattern_ignore.findall(line)

  matches_remove=[]
  for m in matches_dont_do:
    for item in m:
      for i in pattern.findall(item):
        matches_remove.append(i)

  matches = [x for x in matches_all if x not in matches_remove]

  # parse each mul to calculate the multiplication
  for match in matches:
    num_pattern=re.compile(r'\d{1,3}')
    nums=num_pattern.findall(match)
    sum+=int(nums[0])*int(nums[1])

  return sum

def part2_alt():
  file_sum=0

  for l in lines:
    pattern=re.compile(r'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)')

    mul_enabled=True
    for match in re.finditer(pattern, l):
      match_text=match.group(0)
      if match_text=="don't()":
        mul_enabled=False
      elif match_text=="do()":
        mul_enabled=True
      else:
        if mul_enabled:
          num_pattern=re.compile(r'\d{1,3}')
          nums=num_pattern.findall(match_text)
          file_sum+=int(nums[0])*int(nums[1])

  return file_sum

def part1():
  file_sum=0
  for l in lines:
    line_sum=calc_line_sum(l)
    file_sum+=line_sum

  return file_sum

def part2():
  file_sum=0

  for l in lines:
    line_sum=calc_line_sum_do_dont(l)
    file_sum+=line_sum

  return file_sum


if __name__ == "__main__":
  sum=part1()
  print(sum)

  sum2=part2()
  print(sum2)
