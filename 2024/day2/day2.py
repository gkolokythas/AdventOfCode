filename='day2.input'

lines=[]

with open(filename) as f:
  for l in f:
    lines.append(list(int(item)for item in l.split()))

def is_line_valid(line: list[int]) -> bool:
  direction="asc"
  if line[0] > line[1]:
    direction="desc"

  for index,_ in enumerate(line):
    if index==len(line)-1:
      return True

    num_1=line[index]
    num_2=line[index+1]

    if direction=="asc" and num_1 > num_2:
      return False
    if direction=="desc" and num_1 < num_2:
      return False

    diff=abs(num_1-num_2)
    if diff<1 or diff>3:
      return False

  return False

def line_iterations(line: list[int])->list[list[int]]:
  return [line[:i] + line[i+1:] for i in range(len(line))]

def part1():
  return sum(1 for line in lines if is_line_valid(line))

def part2():
  cnt=0

  for line in lines:
    if is_line_valid(line):
      cnt+=1
    else:
      for l in line_iterations(line):
        if is_line_valid(l):
          cnt+=1
          break

  return cnt

if __name__ == "__main__":
  cnt=part1()
  print(f'The safe reports shall be: {cnt}')

  cnt2=part2()
  print(f'The safe reports, using the Dampener, shall be: {cnt2}')
