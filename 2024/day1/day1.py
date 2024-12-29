filename='day1.input'

left=[]
right=[]

with open(filename) as f:
  for line in f:
    items=line.split()
    left.append(int(items[0]))
    right.append(int(items[1]))

def part1():
  print(sum([abs(l-r) for l,r in zip(sorted(left), sorted(right))]))

def part2():
  occurrences_right=dict((x,right.count(x))for x in set(right))
  similarity=[item * occurrences_right.get(item,0) for item in left]

  print(sum(similarity))


if __name__ == "__main__":
 part1()
